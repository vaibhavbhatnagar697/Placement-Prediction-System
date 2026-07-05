# Placement Package Prediction System

## Overview

The Placement Package Prediction System is a Machine Learning project that predicts a student's expected placement package (LPA) based on academic performance, technical skills, and extracurricular achievements.

The project demonstrates a complete Machine Learning workflow, including data preprocessing, exploratory data analysis (EDA), feature selection, model training, evaluation, and deployment using Streamlit.

---

## Features

* Data Cleaning

  * Missing Value Handling
  * Duplicate Removal
  * Outlier Detection and Treatment

* Exploratory Data Analysis (EDA)

  * Correlation Analysis
  * Distribution Visualization
  * Box Plots and Scatter Plots

* Feature Selection

  * Sequential Feature Selection using MLXtend

* Machine Learning Models

  * Linear Regression
  * Ridge Regression (L2 Regularization)
  * Lasso Regression (L1 Regularization)

* Model Evaluation

  * R² Score
  * Mean Absolute Error (MAE)
  * Mean Squared Error (MSE)
  * Root Mean Squared Error (RMSE)

* Deployment

  * Interactive Streamlit Web Application

---

## Dataset Features

The dataset contains the following features:

| Feature             | Description                         |
| ------------------- | ----------------------------------- |
| CGPA                | Academic Performance                |
| DSA_Score           | Data Structures & Algorithms Score  |
| Aptitude_Score      | Aptitude Test Score                 |
| Internships         | Number of Internships               |
| Projects            | Number of Projects                  |
| Hackathons          | Number of Hackathons Participated   |
| Certifications      | Number of Certifications            |
| Communication_Score | Communication Skill Rating          |
| Package_LPA         | Target Variable (Placement Package) |

---

## Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn
* Scikit-Learn
* MLXtend
* Joblib
* Streamlit

---

## Project Workflow

1. Load Dataset
2. Data Cleaning
3. Exploratory Data Analysis
4. Feature Selection
5. Train-Test Split
6. Linear Regression
7. Ridge Regression
8. Lasso Regression
9. Model Comparison
10. Model Saving
11. Streamlit Deployment

---

## Model Comparison

The following models were trained and evaluated:

* Linear Regression
* Ridge Regression
* Lasso Regression

The final model was selected based on:

* Highest R² Score
* Lowest MAE
* Lowest RMSE

---


## Project Structure

```text
PlacementPredictionSystem/
│
├── file.ipynb
├── data.csv
├── placement_model.pkl
├── app.py
└── README.md
```

---

## Future Improvements

* Hyperparameter Tuning
* Cross Validation
* Advanced Regression Models
* Model Explainability
* Cloud Deployment
* Real Placement Dataset Integration

---

## Author

Vaibhav Bhatnagar

Machine Learning and Artificial Intelligence Enthusiast
