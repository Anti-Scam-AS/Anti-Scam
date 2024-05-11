from django.shortcuts import render, redirect
from datetime import datetime

from main.models import Vacant

# Create your views here.

vacant = ""




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

    if values[1] != "":
        return render(request, "verify_vacant_email.html", contex)
    elif values[4] != "":
        return render(request, "verify_vacant_tel.html", contex)
    

def analyzed_vacant(request):
    global vacant

    c_det = False
    c_org = False
    titulo = False
    nombre = False
    tel = False
    fecha = False

    fil = Vacant.objects.all()
    values = list(vacant.values())[1:]
    dateV = ""

    if values[5] != "":
        dateV = datetime.strptime(values[5], '%Y-%m-%d').date()

    for i in fil:
        verification_points = 0
        print(i.Correo_dest)
        print(values)
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
            nombre = False

        if values[4] == i.telefono and values[4] != "":
            verification_points = verification_points + 1
            tel = True

        if dateV == i.Fecha_envio and values[5] != "":
            verification_points = verification_points + 1
            fecha = True

        verification_results[i.Titula] = verification_points

    print(f'v: {verification_results}')

    results = []

    results.append(c_det)
    results.append(c_org)
    results.append(titulo)
    results.append(nombre)
    results.append(tel)
    results.append(fecha)
    


    


    contex = {"fil": fil, "values": values, "results": results}

    print(results)

    return render(request, "verify_vacant.html", contex)