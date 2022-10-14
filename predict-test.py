#!/usr/bin/env python
# coding: utf-8

import requests

url = 'http://locahost:9696/predict'

customer_id =  'xyz-123'

customer = {
   "gender": "female",
   "seniorcitizen": 0,
   "partner": "no",
   "dependents": "no",
   "tenure": 41,  
   "phoneservice": "yes",
   "multiplelines": "no",
   "internetservice": "dsl",
   "onlinesecurity": "yes",
   "onlinebackup": "no",
   "deviceprotection": "yes",
   "techsupport": "yes",
   "streamingtv": "yes",
   "streamingmovies": "yes",
   "contract": "one_year",
   "paperlessbilling": "yes",
   "paymentmethod": "bank_transfer_(automatic)",
   "monthlycharges": 79.85,
   "totalcharges": 3320.75
}

response = requests.post(url, json=customer).json()
print(response)

if response['churn'] == True:
    print('sending email %s' % customer_id)
else:
    print('not sending email %s' % customer_id)




