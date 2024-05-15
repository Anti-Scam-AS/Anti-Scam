from django.shortcuts import render, redirect
from datetime import datetime

import uuid

from main.models import Vacant, Vacant_report, delete_vacante_command, update_vacante_command

from nltk.sentiment import SentimentIntensityAnalyzer

from spellchecker import SpellChecker

spell = SpellChecker(language='es')
import nltk
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('vader_lexicon')

# Create your views here.

vacant = ""

def report_vacant(request):
    fil = Vacant_report.objects.all()

    contex = {"fil": fil}

    if request.method == 'GET':
        return render(request, "verify_report.html", contex)
    else:
        order = request.POST

        vacant = Vacant_report.objects.get(Titula_c = order["titulo_reportado"])

        if order["orden"] == "actualizar":
            if order["verification"] != None:
                ver = False
            else:
                ver = True
            command = update_vacante_command(vacant, order["report"], ver)
            command.execute()

        if order["orden"] == "borrar":
            command = delete_vacante_command(vacant)
            command.execute()

        return render(request, "verify_report.html", contex)



def analyze_description(description):

    words = description.split()

    errors = spell.unknown(words)

    # Análisis de sentimientos
    sia = SentimentIntensityAnalyzer()
    result = sia.polarity_scores(description)

    return {
        'result': result,
        'errors': errors,
        "word_quantity": len(words)
    }

verification_points = 0
verification_results = {}


def insert_vacant(request):
    if request.method == 'GET':
        return render(request, "insert_V.html")
    
    else:
        global vacant
        vacant = ""
        vacant = request.POST
        return redirect("verify/")
    

def verify_vacant(request):
    global vacant
    fil = Vacant.objects.all()
    values = list(vacant.values())[1:]
    dateV = ""
    email_verificator = False
    tel_verificator = False


    for i in fil:
        if i.Correo_org == values[1]:
            email_verificator = True

        if i.telefono == values[4]:
            tel_verificator = True


    contex = {"fil": fil, "values": values}

    if values[5] != "":
        dateV = datetime.strptime(values[5], '%Y-%m-%d').date()


    contex = {"fil": fil, "values": values, "date": dateV, "Ev": email_verificator, "Tv": tel_verificator}

    if request.method == 'POST' and 'reportar' in request.POST:
        titulo_reportado = request.POST.get('titulo_reportado')

        original = Vacant.objects.get(Titula=titulo_reportado)

        prototype = original.clone()


        new_report = Vacant_report.objects.create(
            id = prototype.id,
            Fecha_envio_c=prototype.Fecha_envio,
            Correo_dest_c=prototype.Correo_dest,
            Correo_org_c=prototype.Correo_org,
            Titula_c=prototype.Titula,
            telefono_c=prototype.telefono,
            nom_empresa_c=prototype.nom_empresa,
            descripcion_c=prototype.descripcion,
            texto_t_c=prototype.texto_t,
            url_vacante_c=prototype.url_vacante,
            url_empresa_c=prototype.url_empresa,
            Report='',
            verification=False
        )

        new_report.save()

        
    if values[1] != "":
        return render(request, "verify_vacant_email.html", contex)
    elif values[4] != "":
        return render(request, "verify_vacant_tel.html", contex)
    else:
        return render(request, "verify_vacant_none.html", contex)

    

def analyzed_vacant(request):
    global vacant

    c_det = False
    c_org = False
    titulo = False
    nombre = False
    tel = False
    fecha = False
    descrip = False
    text = False
    graphy = False

    tele = False
    email = False


    fil = Vacant.objects.all()
    values = list(vacant.values())[1:]
    dateV = ""
       

    if values[5] != "":
        dateV = datetime.strptime(values[5], '%Y-%m-%d').date()

    for i in fil:
        verification_points = 0
        if values[0] == i.Correo_dest and values[0] != "":
            verification_points = verification_points + 1
            c_det = True

        if values[1] == i.Correo_org and values[1] != "":
            verification_points = verification_points + 1
            c_org = True
        
        if values[2] == i.Titula and values[2] != "":
            verification_points = verification_points + 1
            titulo = True

        if values[3] == i.nom_empresa and values[3] != "":
            verification_points = verification_points + 1
            nombre = True

        if values[4] == i.telefono and values[4] != "":
            verification_points = verification_points + 1
            tel = True

        if dateV == i.Fecha_envio and values[5] != "":
            verification_points = verification_points + 1
            fecha = True

        verification_results[i.Titula] = verification_points

    verification_points = 0

    if values[6] != "":
        email = True
        Result_description = analyze_description(values[6])

        print("Análisis de sentimientos:", Result_description['result']["compound"])

        if Result_description['result']["compound"] >= 0.0 and Result_description['result']["compound"] < 0.5 and len(Result_description['errors']) <= Result_description['word_quantity']-(Result_description['word_quantity']/2):
            verification_points = verification_points + 2
            descrip = True
            graphy = True

        elif Result_description['result']["compound"] >= 0.0 and Result_description['result']["compound"] < 0.5:
            verification_points = verification_points + 1
            descrip = True

        else:
            verification_points = verification_points - 2
            descrip = False

    if values[7] != "":
        tele = True
        Result_description = analyze_description(values[7])

        print("Análisis de sentimientos:", Result_description['result'])

        if Result_description['result']["compound"] >= 0.0 and Result_description['result']["compound"] < 0.5 and len(Result_description['errors']) <= Result_description['word_quantity']-(Result_description['word_quantity']/2):
            verification_points = verification_points + 2
            text = True
            graphy = True

        elif Result_description['result']["compound"] >= 0.0 and Result_description['result']["compound"] < 0.5:
            verification_points = verification_points + 1
            text = True

        else:
            verification_points = verification_points - 2
            text = False

    results = []

    results.append(c_det)
    results.append(c_org)
    results.append(titulo)
    results.append(nombre)
    results.append(tel)
    results.append(fecha)
    results.append(descrip)
    results.append(text)
    results.append(graphy)
    results.append(email)
    results.append(tele)

    print(descrip)
    print(email)
    print(text)

    if c_det:
        verification_points = verification_points + 1

    if c_org:
        verification_points = verification_points + 1

    if titulo:
        verification_points = verification_points + 1

    if nombre:
        verification_points = verification_points + 1

    if tel:
        verification_points = verification_points + 1

    if fecha:
        verification_points = verification_points + 1

    print(verification_points)

    contex = {"fil": fil, "values": values, "results": results, "verification": verification_points}

    return render(request, "verify_vacant.html", contex)