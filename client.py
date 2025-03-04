
import os
import io
import boto3 
import json 
import csv 

ENDPOINT_NAME = 'bikeshare-sagemaker-regression-v1'
runtime = boto3.client('runtime.sagemaker')

#conver categorical data field
observation = "229,2011-08-17,3,0,8,0,3,1,1,0.723333,0.666671,0.575417,0.143667,668,4026 "
observation = observation.replace("-","")

data = {"data":observation}
actual = {"data":"4694"}
payload = data['data']

#print(payload)

response = runtime.invoke_endpoint(EndpointName=ENDPOINT_NAME, 
                                   ContentType='text/csv', 
                                   Body=payload)

#print(response)
result = json.loads(response['Body'].read().decode())
print('predictions: ', result['predictions'][0]['score'], '\t\tactual: ', str(actual['data']))
