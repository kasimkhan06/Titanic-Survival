# Titanic Survival Prediction 🚢

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python Version](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![Made with Streamlit](https://img.shields.io/badge/made%20with-Streamlit-red.svg)](https://streamlit.io)

An end-to-end machine learning project that predicts passenger survival on the Titanic. This repository covers the entire data science workflow, from exploratory data analysis and feature engineering to model training, hyperparameter tuning, and deployment as an interactive web application using Streamlit.

---

## 🚀 Live Application

**[➡️ Click here to view the deployed Streamlit app!](YOUR_DEPLOYMENT_LINK_HERE)**

*(Note: Replace `YOUR_DEPLOYMENT_LINK_HERE` with the actual URL from your hosting service.)*

---

## 🖼️ Demo

<img width="1917" height="907" alt="image" src="https://github.com/user-attachments/assets/86b8a444-dcb3-4a4e-98fd-948d4b425a8e" />


---

## ✨ Key Features

* **In-depth EDA:** Comprehensive exploratory data analysis to uncover insights from the dataset.
* **Advanced Feature Engineering:** Creation of new, impactful features like `Title`, `FamilyGroup`, and `Deck` using custom Scikit-learn transformers.
* **Robust ML Pipeline:** Use of `sklearn.pipeline.Pipeline` to create a reproducible, end-to-end workflow from raw data to prediction.
* **Hyperparameter Tuning:** `GridSearchCV` is used to find the optimal parameters for the final model.
* **Interactive Web App:** A user-friendly interface built with Streamlit to make live predictions.

---

## 🛠️ Technology Stack

* **Data Analysis & ML:** pandas, NumPy, scikit-learn
* **Data Visualization:** Matplotlib, Seaborn
* **Web App:** Streamlit
* **Development:** Jupyter Notebook, joblib

---

## 📂 Project Structure

```
.
├── app.py
├── requirements.txt
├── requirements-dev.txt
├── data/
├── models/
├── notebooks/
├── src/
└── README.md
```

---

## 🏁 Getting Started

Follow these steps to set up and run the project locally.

### 1. Clone the Repository
```sh
git clone https://github.com/kasimkhan06/Titanic-Survival.git
cd titanic-survival-prediction
```

### 2. Create and Activate a Virtual Environment
It's recommended to use a virtual environment to manage dependencies.
```sh
python -m venv .venv
source .venv/bin/activate  # On Windows, use `.venv\Scripts\activate`
```

### 3. Install Dependencies
This project includes separate requirements files for running the app and for development.
* **To run the app:**
    ```sh
    pip install -r requirements.txt
    ```
* **For development (to run notebooks, etc.):**
    ```sh
    pip install -r requirements-dev.txt
    ```

### 4. Run the Streamlit App
Launch the interactive web application.
```sh
streamlit run app.py
```

---

## 🔄 Reproducing the Model
To understand the project from scratch and reproduce the final model:

1.  **Explore the Data:** Start with `notebooks/01_EDA.ipynb`.
2.  **Engineer Features:** See how features were created in `notebooks/02_Feature_Engineering.ipynb`.
3.  **Train the Model:** Run `notebooks/03_Modelling.ipynb` to train the model, perform grid search, and export the final pipeline as `models/model.pkl`. This exported model is what the Streamlit app uses.

---

## 📄 License

This project is licensed under the terms of the [MIT License](LICENSE).

---

## 🙏 Acknowledgements

* This project is based on the [Kaggle Titanic - Machine Learning from Disaster](https://www.kaggle.com/c/titanic) competition.
* Built with the incredible [Streamlit](https://streamlit.io/) and [scikit-learn](https://scikit-learn.org/) libraries.
