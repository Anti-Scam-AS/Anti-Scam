from django.shortcuts import render, redirect
from datetime import datetime

from main.models import Vacant

# Create your views here.

vacant = ""


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