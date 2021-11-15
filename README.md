## **Dallas Building Permits**
Processing [Dallas Bulding Permits](https://developdallas.dallascityhall.com/) has a been an issue for the city Dallas. A massive [backlog](https://www.dallasobserver.com/news/dallas-permit-process-delays-11968181) of pending buidling permits has slowed down the city's ability to add desparately needed limits. The focus of this project is to harvest city permits data and create a Flask-RESTFUL API with city building data. 

## **API Directions**
#### Login (Post): 
Users can access the API only with valid credentials. A general login has been created for users where general calls can be made to the API.
##### **General Access:** 
The credentials for the Guests are the following:
 
 **UserName:** GuestUser
 
 **Password:** password123

The Login EndPoint is the following:
 
 **End Point:** http://157.245.247.53/projects/dallas-permits/login/ 

**Method:** POST

Upon login an JWT Authorization Token will be created. Tokens will automatically expire after 6 minutes. Note that Token must have "Bearer" appended to the access token when performing GET Requests. 

An example of a login can be seen below w/ Python Requests:
```sh
import requests

params =  {"username": "GuestUser","password": "password123"}
url='http://157.245.247.53/projects/dallas-permits/login/'
re = requests.post(url,data=params)
#format token
token = "Bearer " + re.json()['token']
```

#### **Permits by Date (GET)**

Users can retrieve New Construction Building Permits created during a specified date range. A provided JWT Authorizationo token is required to make this call. 

**Header:** JWT Authorization Token
**Parameters:**
- Beg_Date = Begining Date of Permits Created. Dates must be in YYYY-MM-DD format
- End_Date = Ending Date of Permits Created Dates must in YYYY-MM-DD format

**EndPoint:** http://157.245.247.53/projects/dallas-permits/permits/begdate={Beg_Date}&enddate={End_Date}
**Method:** GET

An example of a call requests by dates can be seen below w/ Python Requests:

```sh
#Remember to Format JWT Token
token = "Bearer " + re.json()['token']
# Get Permits by Date...
date_params ={
    "beg_date": "2020-07-01"
    ,"end_date": "2020-07-02"
}
#EndPoint
url = 'http://157.245.247.53/projects/dallas-permits/permits/begdate={}&enddate={}'.format(date_params['beg_date'],date_params['end_date'])
#pass in the Authorization Token
re = requests.get(url, headers= {'Authorization': token})
#View some of the results using the "permits" Key
print(re.json()['permits'][0:2])
```

#### **Permits by Permit ID (GET)**
If a user know the specific Permit ID for a given permit than a specific GET request can be made to retrieve that information for the specified Permit ID.
**Header:** JWT Authorization Token
**Parameters:**
- Permits ID: Dallas Permit ID

**EndPoint:** http://157.245.247.53/projects/dallas-permits/permit/
**Method:** GET

```sh
#Remember to Format JWT Token
token = "Bearer " + re.json()['token']
#Get Specifc Permit by ID... 
permit_id ='2005211027'
url= 'http://157.245.247.53/projects/dallas-permits/permit/{}'.format(permit_id)
re = requests.get(url, headers= {'Authorization': token})
#Print the results of the specific call
print(re.json())
```


### Updates:
11-04-21 - The API is Deployed.Pending DNS Set up. 
