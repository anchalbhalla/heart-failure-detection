import urllib3, requests, json

# retrieve your wml_service_credentials_username, wml_service_credentials_password, and wml_service_credentials_url from the
# Service credentials associated with your IBM Cloud Watson Machine Learning Service instance

wml_credentials={
"url": "https://us-south.ml.cloud.ibm.com",
"username": "59f50ecd-4ee3-4410-a687-077315fa06c3",
"password": "31dbf7ca-13bc-4b59-97ad-93db13a5c5f3"
}

headers = urllib3.util.make_headers(basic_auth='{username}:{password}'.format(username=wml_credentials['username'], password=wml_credentials['password']))
url = '{}/v3/identity/token'.format(wml_credentials['url'])
response = requests.get(url, headers=headers)
mltoken = json.loads(response.text).get('token')

header = {'Content-Type': 'application/json', 'Authorization': 'Bearer ' + mltoken}

# NOTE: manually define and pass the array(s) of values to be scored in the next line 
array_of_values_to_be_scored = [93, 22, 163, 25, "NO", 49, 'F', 'N', 'N', 110]
payload_scoring = {"fields": ["AVGHEARTBEATSPERMIN", "PALPITATIONSPERDAY", "CHOLESTEROL", "BMI", "HEARTFAILURE", "AGE", "SEX", "FAMILYHISTORY", "SMOKERLAST5YRS", "EXERCISEMINPERWEEK"], "values": [array_of_values_to_be_scored]}

response_scoring = requests.post('https://us-south.ml.cloud.ibm.com/v3/wml_instances/1f796ca3-54a1-494b-8e35-6dde99cf5888/deployments/9f5897dc-41ec-46f9-8a45-2e8a357e251b/online', json=payload_scoring, headers=header)
print("Scoring response")
print(json.loads(response_scoring.text))