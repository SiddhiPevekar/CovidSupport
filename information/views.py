from django.contrib.auth import authenticate
from . import models
# Create your views here.
from django.shortcuts import render, redirect
from django.http import HttpResponse
import requests
from .models import Supplier
from . import views

def download_data() -> dict:
    """
        Downloads currently available data from scraped from 
        'https://www.mohfw.gov.in/' website.
    """
    r = requests.get('https://covid19-mohfw.herokuapp.com/', auth=('user', 'pass'))

    if(r.status_code == 200):
        print('Request Successful!')
    else:
        print('Request Failed!')

    data = r.json()
    return data

# Create your views here.
def homepage(request):
    data_dict = download_data()
    country_data = data_dict['totals']
    state_data = data_dict['states']

    d = { 
            'active_cases' : country_data["cases"] , 
            'recovered' : country_data["recoveries"], 
            'deaths' : country_data["deaths"], 
            'state_list' : state_data                 # List of states(table-rows)
        }

    return render(request, 'information/index.html' , d)


def s_loginpage(request):
    if request.method == "POST":
        username = request.POST.get('s_emailid', False)
        password= request.POST.get('s_password', False)
        print(username)
        print(password)

        bool_ans = models.Supplier.objects.filter(s_emailid=username, s_password=password).exists()#condition to match values are equal or not

        if bool_ans == True:
            sup= models.Supplier.objects.filter(s_emailid = username)
            supval = {
                "supplier": sup #to get particular object
            }

            return render(request, 'information/supplier_home.html',supval)

        if bool_ans == False:

            return render(request, 'information/index.html')

    return render(request, 'information/index.html')#where the form is present


def patient_register(request):
   if request.method == "POST":
        p_username = request.POST.get('p_username', False)
        p_firstname = request.POST.get('p_firstname', False)
        p_lastname = request.POST.get('p_lastname ', False)
        p_emailid = request.POST.get('p_emailid', False)
        p_pass1 = request.POST.get('p_pass1', False)
        p_pass2 = request.POST.get('p_pass2', False)
        patient_record = models.Patient(p_username=p_username, p_firstname=p_firstname, p_lastname=p_lastname, p_emailid=p_emailid, p_pass1=p_pass1, p_pass2=p_pass2)
        patient_record.save()
        print("Data has been saved")
   return render(request, 'information/patient_homepage.html')
# def s_loginpage(request):
#     if request.method == "POST":
#         username = request.POST.get('s_emailid', False)
#         password= request.POST.get('s_password', False)
#         print(username)
#         print(password)

#         bool_ans = models.Supplier.objects.filter(s_emailid=username, s_password=password).exists()#condition to match values are equal or not

#         if bool_ans == True:
#             sup= models.Supplier.objects.filter(s_emailid = username)
#             supval = {
#                 "supplier": sup #to get particular object
#             }

#             return render(request, 'information/supplier_home.html',supval)

#         if bool_ans == False:

#             return render(request, 'information/index.html')

#     return render(request, 'information/index.html')#where the form is present
def patient_login(request):
    # global user_g
    if request.method == "POST":
        p_username = request.POST.get('p_username', False)
        p_pass1= request.POST.get('p_pass1', False)
        # user_g = username
        print(p_username)
        print(p_password)

        bool_ans = models.Patient.objects.filter(p_username=p_username, p_pass1=p_pass1).exists()

        if bool_ans == True:
            pat= models.Patient.objects.filter(p_username=p_username)
            patval = {
                "patient": pat
            }

            return render(request, 'information/patient_homepage.html',patval)

        if bool_ans == False:

            return render(request, 'information/index.html')
    return render(request, 'information/index.html')


