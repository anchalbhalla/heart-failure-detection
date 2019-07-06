# heart-failure-detection
This repo showcases the power of data science in the healthcare field. The project uses SPSS to create a machine learning model which predicts whether a patient will get a heart failure or not. The front end of this project is a Flask app.

## Creating the Machine Learning model on IBM Cloud 


### SPSS flow :
This is the SPSS flow that needs to be created in order to deploy the model 

#### Steps: 
1. Import the patients.csv dataset
2. Connect the type node and open it to specify heart failure attribute as the target and rest as input
3. Connect the partition node and specify 80 - training and 20 - testing
4. Connect the random forest node 
5. Hit Run 
6. Connect the Orange model node to a table node
7. Hit Run again 
8. Click on the 3 dots on the table node 
<img src = https://github.com/anchalbhalla/heart-failure-detection/blob/master/pic1.png > 

9. Select Save node as a model and give a name to the model 
10. Once model is deployed go to the project page and you will find the model under Watson machine learning models
11. Click the model and click add deployment, next add a name for the deployment and wait for it to be deployed
12. Copy the scoring end under the test tab which will be used later

## Front end application [Flask]

### Steps: 

1. Edit the predict.py file: 
2. Add your watson machine learning service credentials which you get from cloud.ibm.com 
<img src = "https://github.com/anchalbhalla/heart-failure-detection/blob/master/pics/credentials.png"> 
3. Add the scoring URL of the model created on Watson Studio. This will be present in the deployments tab when you deploy the model. 
<img src = "https://github.com/anchalbhalla/heart-failure-detection/blob/master/pics/url.png">

### Heart Rate Failure Detection Application in Action

<img src = "https://github.com/anchalbhalla/heart-failure-detection/blob/master/gifs/app.gif">
