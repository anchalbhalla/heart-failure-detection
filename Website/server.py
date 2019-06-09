from flask import Flask, jsonify, request, render_template,json
import urllib3, requests

app = Flask(__name__)
#HOST = '0.0.0.0'
PORT = 8080

wml_credentials={
  "url": "https://us-south.ml.cloud.ibm.com",
"username": "59f50ecd-4ee3-4410-a687-077315fa06c3",
"password": "31dbf7ca-13bc-4b59-97ad-93db13a5c5f3"
}

@app.route('/', methods=['GET'])
def index():
	return render_template('index.html')

@app.route('/watson', methods=['POST','GET'])
def api_call():

	if request.method == 'POST':
		# PassengerId = request.args.get('passengerid')
		AVGHEARTBEATSPERMIN = request.form.get('AVGHEARTBEATSPERMIN')
		PALPITATIONSPERDAY = request.form.get('PALPITATIONSPERDAY')
		CHOLESTEROL = request.form.get('CHOLESTEROL')
		BMI = request.form.get('BMI')
		HEARTFAILURE = request.form.get('HEARTFAILURE')
		AGE = request.form.get('AGE')
		SEX = request.form.get('SEX')
		FAMILYHISTORY = request.form.get('FAMILYHISTORY')
		SMOKERLAST5YRS = request.form.get('SMOKERLAST5YRS')
		EXERCISEMINPERWEEK = request.form.get('EXERCISEMINPERWEEK')

		# print(income)
		# print(applied)
		# print(residence)
		# print(address)
		# print(employer)
		# print(cards)
		# print(debt)
		# print(loans)
		# print(amount)
		# print(price)
		# print(location)



		headers = urllib3.util.make_headers(basic_auth='{username}:{password}'.format(username=wml_credentials['username'], password=wml_credentials['password']))
		url = '{}/v3/identity/token'.format(wml_credentials['url'])
		response = requests.get(url, headers=headers)
		mltoken = json.loads(response.text).get('token')
		header = {'Content-Type': 'application/json', 'Authorization': 'Bearer ' + mltoken}
		# NOTE: manually define and pass the array(s) of values to be scored in the next line
		payload_scoring = {"fields": ["AVGHEARTBEATSPERMIN", "PALPITATIONSPERDAY", "CHOLESTEROL", "BMI", "HEARTFAILURE", "AGE", "SEX", "FAMILYHISTORY", "SMOKERLAST5YRS", "EXERCISEMINPERWEEK"], "values": [[int(AVGHEARTBEATSPERMIN), int(PALPITATIONSPERDAY), int(CHOLESTEROL), int(BMI), HEARTFAILURE, int(AGE), SEX, FAMILYHISTORY, SMOKERLAST5YRS,int(EXERCISEMINPERWEEK)]]}
		print(payload_scoring)
		response_scoring = requests.post('https://us-south.ml.cloud.ibm.com/v3/wml_instances/1f796ca3-54a1-494b-8e35-6dde99cf5888/deployments/9f5897dc-41ec-46f9-8a45-2e8a357e251b/online', json=payload_scoring, headers=header)

		jsonResult = json.loads(response_scoring.text) 
		print (jsonResult)
		print (jsonResult['values'][0][11]) 

		if (jsonResult['values'][0][11]) == 'Y':
			prob = (jsonResult['values'][0][12])*100 
			finalResult = "The patient will get a heart attack with " + str(prob) + "% confidence"
			return render_template('result.html', value = finalResult)
			# return ("The customer is approved to get a mortgage with " + str(prob) + " probabilty") 

		elif (jsonResult['values'][0][11]) == 'N': 
			probb = (jsonResult['values'][0][12])*100 
			finalResult = "The patient will not get a heart attack with " + str(probb) + "% confidence"
			return render_template('result.html', value = finalResult)
			# return ("The customer is not approved for a mortgage with " + str(probb) + " probabilty")

		return (json.dumps(jsonResult))



if __name__ == '__main__':
	app.run(debug=True, port=PORT)