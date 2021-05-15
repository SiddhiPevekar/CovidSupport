# from django.contrib.auth import authenticate
from . import models
# Create your views here.
from django.shortcuts import render
import requests
from .models import Supplier
from matplotlib import pyplot as plt

user_s =""
user_p =""

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
    create_image(state_data)
    
    return render(request, 'information/index.html' , d)

def create_image(state_data):
    data = []
    # print(state_list)
    for state in state_data:
        cur = [ state['cases'] ,state['recoveries'] ,state['deaths'] , state['state'] ]

        data.append(cur)

    data.sort(reverse = True)
    data = data[:10]

    print(len(data))

    y = [d[0] for d in data]
    x = [d[-1] for d in data]

    # print(x, y)
    plt.figure(figsize=(15, 5))
    print(x)
    plt.bar(x,y,color='#2222AF')
    plt.xlabel('States')
    plt.ylabel('Active Cases')

    # plt.show()
    # pprint(data)
    plt.savefig('information/static/information/assets/img/s1.png')

if __name__ == '__main__':
    data_dict = download_data()
    country_data = data_dict['totals']
    state_list = data_dict['states']
    create_image(state_list)


def s_loginpage(request):
    global user_s
    if request.method == "POST":
        username = request.POST.get('s_emailid', False)
        password= request.POST.get('s_password', False)
        print(username)
        print(password)

        user_s = username
        print(user_s)

        bool_ans = models.Supplier.objects.filter(s_emailid=username, s_password=password).exists()#condition to match values are equal or not

        if bool_ans == True:
            sup= models.Supplier.objects.filter(s_emailid = username)
            supval = {
                "supplier": sup #to get particular object
            }           

            return render(request, 'information/supplier_home.html',supval)            

        if bool_ans == False:

            return render(request, 'information/index.html')

    return render(request, 'information/supplier_home.html')#where the form is present

def patient_register(request):
   if request.method == "POST":
        p_username = request.POST.get('p_username')
        p_firstname = request.POST.get('p_firstname')
        p_lastname = request.POST.get('p_lastname')
        p_emailid = request.POST.get('p_emailid')
        p_pass1 = request.POST.get('p_pass1')
        p_pass2 = request.POST.get('p_pass2')
        patient_record = models.Patient(p_username=p_username, p_firstname=p_firstname, p_lastname=p_lastname, p_emailid=p_emailid, p_pass1=p_pass1, p_pass2=p_pass2)
        patient_record.save()
        print("Data has been saved")
   return render(request, 'information/index.html')

def patient_login(request):
    global user_p
    data = Supplier.objects.all()
    print(data)
    if request.method == "POST":
        p_username = request.POST.get('p_username', False)
        p_pass1= request.POST.get('p_pass1', False)
        
        print(p_username)
        user_p = p_username
        print(user_p)

        bool_ans = models.Patient.objects.filter(p_username=p_username, p_pass1=p_pass1).exists()

        if bool_ans == True:
            pat= models.Patient.objects.filter(p_username=p_username)
            patval = {
                "patient": pat,
                "supplier_info": data
            }

            return render(request, 'information/patient_homepage.html',patval)

        if bool_ans == False:

            return render(request, 'information/index.html')
    return render(request, 'information/patient_homepage.html')

def profile_patient(request):
    return render(request, 'information/patient_profile.html')

def update_patient(request):
    global user_p
    if user_p!="":
        print(user_p)
        pat = models.Patient.objects.filter(p_username=user_p)
        if request.method == 'POST':
            # s_id = request.POST.get('s_id')
            p_username = request.POST.get('p_username')
            p_firstname = request.POST.get('p_firstname')
            p_lastname = request.POST.get('p_lastname')
            p_emailid = request.POST.get('p_emailid')
            p_pass1 = request.POST.get('p_pass1')
            p_pass2 = request.POST.get('p_pass2')
            for i in pat:
                i.p_username = p_username
                i.save()
                i.p_firstname = p_firstname
                i.save()
                i.p_lastname = p_lastname
                i.save()
                i.p_emailid = p_emailid
                i.save()
                i.p_pass1 = p_pass1
                i.save()
                i.p_pass2 = p_pass2
                i.save()
            print("Details saved")
            patient = {
                "pat_d": pat
            }

        return render(request,'information/patient_homepage.html', patient)

    return render(request, 'information/patient_homepage.html')

def update_supplier(request):
    global user_s 
    if user_s!="":
        print(user_s)
        #supp is kind array of object
        supp = models.Supplier.objects.filter(s_emailid=user_s)
        if request.method == 'POST':
            # s_id = request.POST.get('s_id')
            s_agency_name = request.POST.get('s_agency_name')
            s_state = request.POST.get('s_state')
            s_emailid = request.POST.get('s_emailid')
            s_password = request.POST.get('s_password')
            s_district = request.POST.get('s_district')
            icu_beds = request.POST.get('icu_beds')
            ventilator_beds= request.POST.get('ventilator_beds')
            icu_ventilator_beds = request.POST.get('icu_ventilator_beds')
            oxygen = request.POST.get('oxygen')
            for i in supp:
                i.s_agency_name = s_agency_name
                i.save()
                i.s_state = s_state
                i.save()
                i.s_emailid = s_emailid
                i.save()
                i.s_password = s_password
                i.save()
                i.s_district = s_district
                i.save()
                i.icu_beds = icu_beds
                i.save()
                i.ventilator_beds = ventilator_beds
                i.save()
                i.icu_ventilator_beds = icu_ventilator_beds
                i.save()
                i.oxygen = oxygen
                i.save() 
            print("Details saved")
            supplier = {
                "sup": supp
            }
        return render(request, 'information/index.html', supplier)
    return render(request, 'information/index.html')
           
