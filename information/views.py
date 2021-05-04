from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
import requests

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