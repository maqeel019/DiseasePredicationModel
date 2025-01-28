# Health Risk Prediction System

## Overview
The **Health Risk Prediction System** is a machine learning application built to predict health risks based on various body measurements. It classifies an individual's risk level for diseases such as **Heart Disease**, **Diabetes**, **Osteoporosis**, etc., based on physical parameters such as **body fat percentage**, **age**, **weight**, and more.

This project leverages a **Decision Tree Classifier** model trained on historical health data, which allows users to enter their details (e.g., body fat, age, weight, etc.) and receive a prediction of their health risk.

## Features
- **User Input Interface:** A web-based application built with Streamlit where users can input their body measurements and receive predictions.
- **Disease Classification:** Based on input data, the system predicts the risk level for various diseases such as **Heart Disease**, **Diabetes**, **Osteoporosis**, etc.
- **Preprocessing:** The system applies necessary transformations including **scaling** and **label encoding** to prepare the data for prediction.
- **Model Performance:** The decision tree model is fine-tuned using **cross-validation** and **hyperparameter tuning** to ensure high accuracy.

## Technologies Used
- **Python**: Core programming language.
- **Streamlit**: Framework for building the interactive web interface.
- **scikit-learn**: Machine learning library for training the **Decision Tree Classifier** model.
- **Pandas**: Data manipulation and preprocessing.
- **Joblib**: Used for saving and loading the trained model and other preprocessed objects.
  
## Installation

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/maqeel019/DiseasePredicationModel/.git
   ```

2. **Install Dependencies:**

   Ensure that you have `pip` installed, and then run the following to install required libraries:

   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Application:**

   After installing the dependencies, you can run the Streamlit application using:

   ```bash
   streamlit run app.py
   ```

   This will open a local web server where you can interact with the app.

## How It Works
1. **Data Input:** The user is prompted to enter their personal details such as **body fat percentage**, **age**, **weight**, **height**, etc.
2. **Data Preprocessing:** The input data is preprocessed, including **scaling** continuous variables and **encoding** categorical variables.
3. **Prediction:** The processed data is passed through the trained Decision Tree model, which classifies the risk level for various diseases.
4. **Result:** The predicted disease risk (e.g., **Heart Disease - High Risk**) is displayed to the user.

## Files in the Repository

- `app.py`: Streamlit application file where the UI is implemented.
- `model.py`: Python file containing the code for training the Decision Tree model.
- `health_data.csv`: Example dataset used for training the model.
- `decision_tree_model.joblib`: Saved model for disease prediction.
- `disease_encoder.joblib`: Saved label encoder for converting disease labels.
- `scaler.joblib`: Saved scaler used for scaling input data.
- `requirements.txt`: A file listing the required Python packages for the project.

## Model Training
- The model is trained using a **Decision Tree Classifier**, and the data is preprocessed to handle missing values and scale continuous features.
- Hyperparameter tuning is done using **GridSearchCV** to find the optimal model parameters.
  
## Example Input
Here’s an example of the input fields that a user will be required to fill out:

- **Density:** 1.1
- **Body Fat (%):** 18.7
- **Age:** 45
- **Weight (kg):** 75
- **Height (cm):** 180
- **Neck (cm):** 37
- **Chest (cm):** 102
- **Abdomen (cm):** 90
- **Hip (cm):** 98
- **Thigh (cm):** 65
- **Knee (cm):** 43
- **Ankle (cm):** 22
- **Biceps (cm):** 36
- **Forearm (cm):** 30
- **Wrist (cm):** 18
- **Gender:** Female

## Example Output
After the user provides the inputs and clicks **Predict**, the model will predict the disease risk level, such as:

```
Predicted Disease Class: No Significant Risk
```

## Contributing
Feel free to contribute by submitting a **pull request** with any improvements or suggestions. You can also open an **issue** for bugs or feature requests.
