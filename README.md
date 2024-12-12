# Diabetes Prediction - Deployment

# Project Overview
The Diabetes Prediction Web App is a machine learning-based web application built using Flask and deployed on Heroku. The application uses a Random Forest Classifier model to predict the likelihood of an individual having diabetes based on various health factors. It is designed to help users input their health data and get an instant prediction on whether they have diabetes.

The model was trained on a well-known diabetes dataset, and the web app provides an easy-to-use interface for predicting diabetes risk. With this tool, users can quickly assess their risk by entering information such as their age, BMI, blood pressure, and other health metrics.

# Technologies Used

Flask: A micro web framework used to create the web application.
Random Forest Classifier: A machine learning algorithm used for classification tasks to predict the diabetes outcome.
Heroku: A cloud platform used for deploying the web app.
Pickle: For serializing the trained machine learning model so it can be used in the Flask app.
HTML/CSS: For front-end development, including form inputs and result display.
JavaScript (optional): For any dynamic interactions on the front-end (e.g., displaying results).
Features
Web Interface: The app provides a simple and clean interface where users can input their health data.
Prediction: After submitting the form, the app uses the trained model to predict whether the user is likely to have diabetes or not.
Result Visualization: The prediction is displayed with a clear message and an appropriate image indicating whether the user is at risk or not.
Responsive Design: The app is designed to be responsive, ensuring that it works on both desktop and mobile devices.

# Workflow
Model Training:

The model was trained on the Pima Indians Diabetes Database, which includes the following features:
Number of Pregnancies
Glucose Level
Blood Pressure
Skin Thickness
Insulin Level
Body Mass Index (BMI)
Diabetes Pedigree Function (DPF)
Age
The data was cleaned and pre-processed by replacing zeros in certain columns (which could be invalid entries) with the mean or median values, depending on the distribution of the data.
After pre-processing, the Random Forest Classifier was trained on the dataset, and the model was serialized using Pickle for later use in the web application.
Web App:

The Flask framework was used to build the web app.
The user interface includes a form where users can enter their health metrics.
Upon form submission, the app uses the trained Random Forest Classifier to predict whether the user has diabetes or not.
The prediction is displayed in a user-friendly format, with a message and an image indicating the result.
Deployment:

The app is deployed on Heroku, making it accessible to anyone with a web browser.
The machine learning model is stored in a Pickle file and loaded into the Flask app to generate predictions.
How It Works
When the user accesses the web app, they are greeted with a form that prompts them to enter their health data (e.g., pregnancies, glucose level, BMI).
After submitting the form, the app processes the input data and makes a prediction using the trained Random Forest model.
The app then displays the result with a clear message indicating whether the user has diabetes or not, along with an image to reinforce the result.




![Kaggle](https://img.shields.io/badge/Dataset-Kaggle-blue.svg) ![Python 3.6](https://img.shields.io/badge/Python-3.6-brightgreen.svg) ![scikit-learnn](https://img.shields.io/badge/Library-Scikit_Learn-orange.svg)

• This repository consists of files required to deploy a ___Machine Learning Web App___ created with ___Flask___ on ___Heroku___ platform.

• If you want to view the deployed model, click on the following link:<br />
Deployed at: _https://predicting-diabetes.herokuapp.com/_

• If you are searching for __Code__, __Algorithms used__ and __Accuracy__ of the model.. you won't find it here. Click the link mentioned below for the same:<br />
Link: _https://github.com/anujvyas/Machine-Learning-Projects/tree/master/Diabetes%20Prediction_

• Please do ⭐ the repository, if it helped you in anyway.

• A glimpse of the web app:

![GIF](readme_resources/diabetes-predictor-web-app.gif)

_**----- Important Note -----**_<br />
• If you encounter this webapp as shown in the picture given below, it is occuring just because **free dynos for this particular month provided by Heroku have been completely used.** _You can access the webpage on 1st of the next month._<br />
• Sorry for the inconvenience.

![Heroku-Error](readme_resources/application-error-heroku.png)
