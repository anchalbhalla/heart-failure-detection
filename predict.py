import urllib3, requests, json

# retrieve your wml_service_credentials_username, wml_service_credentials_password, and wml_service_credentials_url from the
# Service credentials associated with your IBM Cloud Watson Machine Learning Service instance

wml_credentials={
"url": "https://us-south.ml.cloud.ibm.com",
"username": "enter-username",
"password": "enter-password"
}

headers = urllib3.util.make_headers(basic_auth='{username}:{password}'.format(username=wml_credentials['username'], password=wml_credentials['password']))
url = '{}/v3/identity/token'.format(wml_credentials['url'])
response = requests.get(url, headers=headers)
mltoken = json.loads(response.text).get('token')

header = {'Content-Type': 'application/json', 'Authorization': 'Bearer ' + mltoken}

# NOTE: manually define and pass the array(s) of values to be scored in the next line 
array_of_values_to_be_scored = [93, 22, 163, 25, "NO", 30, 'F', 'N', 'N', 110]
payload_scoring = {"fields": ["AVGHEARTBEATSPERMIN", "PALPITATIONSPERDAY", "CHOLESTEROL", "BMI", "HEARTFAILURE", "AGE", "SEX", "FAMILYHISTORY", "SMOKERLAST5YRS", "EXERCISEMINPERWEEK"], "values": [array_of_values_to_be_scored]}

response_scoring = requests.post('enter-scoring-end-point', json=payload_scoring, headers=header)
print("Scoring response")
print(json.loads(response_scoring.text))
