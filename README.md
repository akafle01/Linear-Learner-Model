# **Bike Share Demand Prediction using Amazon SageMaker**

This project demonstrates the deployment of a regression model using Amazon SageMaker's Linear Learner algorithm to predict bike share demand in Washington, D.C. The model is trained and tested on a dataset from the University of California, Irvine, and deployed as an endpoint for real-time predictions.

---

## **Table of Contents**
1. [Project Overview](#project-overview)
2. [Technologies Used](#technologies-used)
3. [Dataset](#dataset)
4. [Model Deployment](#model-deployment)
5. [Prediction and Accuracy](#prediction-and-accuracy)
6. [Usage](#usage)
7. [Results](#results)
8. [Screenshots](#screenshots)
9. [License](#license)

---

## **Project Overview**
The goal of this project is to predict the number of bike shares for a given day in Washington, D.C., using a regression model built with Amazon SageMaker's Linear Learner algorithm. The model is trained on a dataset containing 511 days of bike share data and tested on 220 days. The model is deployed as an endpoint for real-time predictions, and its accuracy is evaluated using cosine similarity.

---

## **Technologies Used**
- **Amazon SageMaker**: For model training, deployment, and endpoint management.
- **Linear Learner Algorithm**: For regression-based predictions.
- **Python**: For data preprocessing, model evaluation, and client-side prediction.
- **Jupyter Notebook**: For interactive development and testing.
- **NumPy**: For numerical computations and accuracy calculations.
- **CSV Serializer/JSON Deserializer**: For data input/output handling.

---

## **Dataset**
The dataset used in this project is sourced from the [University of California, Irvine](https://archive.ics.uci.edu/ml/datasets/Bike+Sharing+Dataset). It includes the following features:
- Date
- Weather conditions
- Temperature
- Humidity
- Windspeed
- Count of bike shares (target variable)

---

## **Model Deployment**
The model is deployed using Amazon SageMaker with the following steps:
1. **Training**: The Linear Learner algorithm is used to train the model on the training dataset.
2. **Endpoint Creation**: The model is deployed to an endpoint named `bikeshare-sagemaker-regression-v1` on a `C4 Extra Large` instance.
3. **Prediction**: The endpoint is used to generate predictions on the test dataset.

---

## **Prediction and Accuracy**
Predictions are made using the test dataset, and the model's accuracy is evaluated using cosine similarity. The accuracy is calculated as:
''python
'accuracy = (dot(actual, predictions) / (norm(actual) * norm(predictions))) * 100 '

## **Results and Screenshots
Here are some screenshots of the project steps and results in action:
<img width="274" alt="Screenshot 2025-03-03 at 2 36 53 PM" src="https://github.com/user-attachments/assets/b143b521-19c1-4456-a8a6-cfca425e9d63" />
<img width="517" alt="Screenshot 2025-03-03 at 2 36 31 PM" src="https://github.com/user-attachments/assets/80fddd3e-d5ce-4817-8f17-fe03b243ba60" />
<img width="1086" alt="Screenshot 2025-03-03 at 2 36 00 PM" src="https://github.com/user-attachments/assets/edf98d79-58af-4d2e-abbf-97f66ffe6eac" />
<img width="1139" alt="Screenshot 2025-03-03 at 2 35 42 PM" src="https://github.com/user-attachments/assets/369e47ee-3bdb-490a-8da5-d59304dfb6bc" />
<img width="1129" alt="Screenshot 2025-03-03 at 2 35 09 PM" src="https://github.com/user-attachments/assets/ba1afd06-9ea5-4001-8047-52547d5599c2" />
<img width="1132" alt="Screenshot 2025-03-03 at 2 34 57 PM" src="https://github.com/user-attachments/assets/34231311-8114-4bb1-a82b-b3c62c450e5b" />
<img width="1271" alt="Screenshot 2025-03-03 at 2 29 54 PM" src="https://github.com/user-attachments/assets/98805ff0-f6df-4414-9d0f-d2fb5306755c" />
<img width="1199" alt="Screenshot 2025-03-03 at 2 28 55 PM" src="https://github.com/user-attachments/assets/82709a61-49d4-4452-aa5e-a866a8029bf6" />
<img width="1228" alt="Screenshot 2025-03-03 at 2 20 15 PM" src="https://github.com/user-attachments/assets/ccb45e36-cffd-4378-87ab-ecf148394c88" />
