# from django.contrib.auth import authenticate

import requests
from pprint import pprint
from matplotlib import pyplot as plt

loggedin =""

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

def create_image(state_data):
    data = []
    print(state_data)
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

    plt.show()
    # pprint(data)
    # plt.savefig('information/static/information/assets/img/s1.png')

if __name__ == '__main__':
    data_dict = download_data()
    country_data = data_dict['totals']
    state_list = data_dict['states']


    create_image(state_list)