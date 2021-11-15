import requests

params =  {"username": "GuestUser","password": "password123"}
url='http://157.245.247.53/projects/dallas-permits/login/'

re = requests.post(url,data=params)

#format token
token = "Bearer " + re.json()['token']

## Get Permits by Date...

date_params ={
    "beg_date": "2020-07-01"
    ,"end_date": "2020-07-02"
}

print(token)

url = 'http://157.245.247.53/projects/dallas-permits/permits/begdate={}&enddate={}'.format(date_params['beg_date'],date_params['end_date'])
print(url)
re = requests.get(url, headers= {'Authorization': token})
print(re.json()['permits'][0:2])


#Get Specifc Permit by ID... 
permit_id ='2005211027'
url= 'http://157.245.247.53/projects/dallas-permits/permit/{}'.format(permit_id)
re = requests.get(url, headers= {'Authorization': token})
print(re.json())
