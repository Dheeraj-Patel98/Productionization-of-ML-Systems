# -Productionization-of-ML-Systems
🏨 Hybrid Hotel Recommendation System
This project is a part of a Travel Capstone Project which implements a Hotel Recommendation System using a hybrid approach combining Collaborative Filtering and Content-Based Filtering. The final model is deployed as a Streamlit web application, allowing users to enter their user ID and receive top hotel recommendations.

📁 Dataset Overview
The dataset contains real user hotel bookings with the following features:

travelCode: Unique travel transaction ID
userCode: Unique identifier for the user
name: Hotel name
place: Hotel location
days: Duration of stay
price: Cost per day
total: Total cost paid
date: Booking date
✅ Key Features
1. Data Cleaning & Preprocessing
Removed missing or duplicated entries
Converted date strings to proper datetime format
Normalized textual and numerical values
Counted number of unique users and hotels
2. Collaborative Filtering (CF)
Used Surprise library's KNNBasic algorithm
Treated the total cost as an implicit rating
Evaluated with RMSE (Root Mean Squared Error)
Final model achieved RMSE ≈ 0.97
3. Content-Based Filtering (CBF)
Vectorized hotel names and places using TF-IDF
Computed hotel similarity using cosine similarity
Identified similar hotels based on user history
4. Hybrid Recommender System
Combined CF and CBF with a weighted score
Final score = 70% CF prediction + 30% CBF similarity
Produced better personalized hotel recommendations
5. Streamlit Web Application
Simple UI: Input user ID and get top hotel suggestions
Built using streamlit and deployed via ngrok
Real-time hotel recommendation system
🚀 How to Run Locally
Step 1: Install dependencies
pip install pandas numpy scikit-learn streamlit pyngrok scikit-surprise



# Save the README content as a markdown file

readme_content = """
# 👤2. Gender Classification API using BERT

This project is part of a larger **Travel & Tourism Capstone**, and focuses on predicting **gender from a person's name** using a deep learning model. The final system is accessible via a **REST API built with Flask**, trained in **Google Colab**, and deployed using **Docker**, **ngrok**, and **Jenkins**.

---

## 🧠 Project Highlights

| Component         | Tool/Tech Used               |
|------------------|------------------------------|
| Model             | BERT (`bert-base-uncased`)   |
| Training          | Google Colab (PyTorch)       |
| API               | Flask REST API               |
| Deployment        | Ngrok + Docker               |
| CI/CD Automation  | Jenkins (with Jenkinsfile)   |
| Monitoring        | Console + Screenshot Logs    |

---

## 📁 Dataset Overview

The dataset includes:
- `name`: First name or full name
- `gender`: Label (`Male` or `Female`)

Data Cleaning Steps:
- Removed null/duplicate values
- Normalized genders (lowercased)
- Label-encoded gender: `0 = Female`, `1 = Male`

---

## 🧪 Model Training

- **Tokenizer**: `BertTokenizer`
- **Model**: `BertForSequenceClassification`
- **Accuracy Achieved**: ✅ **> 60%**
- Fine-tuned on short name sequences
- Trained in **Google Colab** using GPU (if available)

---

## 🚀 How to Run This Project (Colab Flow)

### 1️⃣ Train & Save Model
```python
# Load dataset, preprocess
# Tokenize names using BERT tokenizer
# Train using BERT classifier head
# Save model and tokenizer




# ✈️ 3.Flight Price Prediction – Machine Learning Project

This project aims to predict airline ticket prices using various features like airline, source, destination, total stops, and flight duration. The model was trained using **XGBoost Regressor** in Google Colab and deployed using **Gradio** on **Hugging Face Spaces**.

---

## 🚀 Project Highlights

- ✅ Trained using real-world flight data
- ✅ Cleaned and preprocessed in Colab
- ✅ Trained with XGBoost Regressor
- ✅ REST API using Flask (for local testing)
- ✅ Frontend powered by Gradio
- ✅ Deployed live on Hugging Face Spaces
- ✅ Optional: Docker, Kubernetes, Jenkins, and MLflow compatible

---

## 🧠 Technologies Used

- Python
- Pandas, Numpy
- Scikit-learn, XGBoost
- Gradio (for Hugging Face app)
- Flask (for local REST API)
- Docker (optional)
- Kubernetes, Jenkins, MLflow (optional)

---

## 🗂️ Project Structure
