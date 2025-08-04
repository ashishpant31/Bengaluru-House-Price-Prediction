# 🏠 Bengaluru House Price Prediction

This repository contains an interactive machine learning project built with [Streamlit](https://streamlit.io/) and Python, designed to **predict house prices in Bengaluru, India** based on property features such as location, size, and amenities.

---

## 📖 About

**Bengaluru House Price Prediction** is an open-source analytics and prediction tool for homebuyers, sellers, and real estate professionals. It leverages regression models to estimate property prices, helping users make informed decisions in the Bengaluru real estate market.

Key capabilities:
- **Automated price prediction** based on user input (location, BHK, bathrooms, area)
- **Data cleaning and feature engineering** for robust modeling
- **Interactive web app** for instant predictions
- **Jupyter Notebook** for full workflow, EDA, and model development
- **Exportable cleaned data and trained model**

---

## 🌟 Project Overview

**Context:**  
Bengaluru is a rapidly growing city with a dynamic real estate market. Accurate price estimation is crucial for buyers, sellers, and agents to make data-driven decisions.

**Objective:**  
Build a reproducible pipeline to clean data, engineer features, train regression models, and deploy an interactive app for house price prediction.

---

## ✨ Features

- **Data Preprocessing:**
  - Cleans raw data ([Bengaluru_House_Data.csv](Bengaluru_House_Data.csv)), handles missing values, and removes outliers
  - Feature engineering: BHK extraction, price per sqft, location grouping

- **Modeling:**
  - Trains and evaluates regression models (Linear, Lasso, Ridge)
  - Uses pipelines with `OneHotEncoder` and `StandardScaler`
  - Saves the best model (`RidgeModel.pkl`) for deployment

- **Interactive App:**
  - Built with [Streamlit](https://streamlit.io/)
  - Users input property details and receive instant price predictions with confidence range

- **Notebooks & Scripts:**
  - `Untitled.ipynb`: Full EDA, cleaning, modeling, and evaluation
  - `trainmodel.py`: Script for data preprocessing and model training
  - `main.py`: Streamlit app for predictions

---

## 📊 Data

- **Raw Data:** `Bengaluru_House_Data.csv`
- **Cleaned Data:** `Cleaned_data.csv` (generated after preprocessing)
- **Features Used:**  
  - `location`, `total_sqft`, `bath`, `bhk`
- **Target:**  
  - `price` (in lakhs)

---

## 🛠️ Technologies Used

- **Python:** Core programming language
- **Pandas, NumPy:** Data manipulation and analysis
- **scikit-learn:** Machine learning models and pipelines
- **Streamlit:** Interactive web app
- **Jupyter Notebook:** EDA and workflow documentation

---

## 🚀 Installation and Setup

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/ashishpant31/Bengaluru-House-Price-Prediction.git
   cd "Bengaluru-House-Price-Prediction"
   ```

2. **Create a Virtual Environment (Recommended):**
   ```bash
   python -m venv venv
   ```
   - **Windows:** `.\venv\Scripts\activate`
   - **macOS/Linux:** `source venv/bin/activate`

3. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **(Optional) Re-run Data Cleaning/Model Training:**
   ```bash
   python trainmodel.py
   ```
   This will generate `Cleaned_data.csv` and `RidgeModel.pkl`.

5. **Run the Streamlit App:**
   ```bash
   streamlit run main.py
   ```
   The app will open in your browser.

---

## 💡 Usage

- **Web App:**  
  - Enter property details (location, BHK, bathrooms, area) in the sidebar
  - Click "Predict" to get the estimated price range
  - Visualize the prediction and confidence interval

- **Notebook:**  
  - Open `Untitled.ipynb` for full workflow, EDA, and model details

---

## 🖼️ Example Screenshots

<p align="center">
  <strong>Streamlit App – Main Prediction Interface</strong><br>
  <img width="957" height="888" alt="Bengaluru House Price Prediction App" src="https://github.com/user-attachments/assets/d2316bb2-2506-48b5-9d6b-4d7eda375aa1" />
</p>

<p align="center">
  <strong>Streamlit App – Prediction Output Example</strong><br>
  <img width="826" height="878" alt="Prediction Output Example" src="https://github.com/user-attachments/assets/1031c40b-8c42-472e-8b2e-53b8616a6377" />
</p>

---

## 📋 Evaluation Criteria

- **Data Cleaning:** Robust handling of missing values and outliers
- **Feature Engineering:** Extraction and transformation of relevant features
- **Modeling:** Use of regression models and pipelines
- **Deployment:** Functional, user-friendly Streamlit app
- **Documentation:** Clear setup and usage instructions

---

## 🤝 Contributing

Contributions are welcome!
- Fork the repo, create a branch, commit your changes, push, and open a pull request.

---

## 📄 License

This project is licensed under the MIT License. See the `LICENSE` file.

---

## ⚠️ Important: Using `.gitignore` to Exclude Virtual Environments

When using Git, **never commit your virtual environment folder (`venv/`)** or other system/generated files.

**Sample `.gitignore`:**
```
# Python virtual environment
venv/
# Compiled Python files
*.pyc
__pycache__/
# Operating system files
.DS_Store # macOS specific
# Generated data files (optional - remove if you want to track them)
*.csv
```

- `venv/` ensures your virtual environment is ignored.
- `*.pyc`, `__pycache__/` ignore compiled Python files.
- `.ipynb_checkpoints/` for Jupyter notebook checkpoint files.
- `.env` for secrets/environment variables.
- `.DS_Store` for macOS system files.
- `*.csv` skips generated data files (uncomment if you don't want to track them).

---

## 📧 Contact

For questions or feedback, please open an issue in this repository.

---
