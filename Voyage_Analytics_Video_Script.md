# 🎬 VIDEO SCRIPT

## "Voyage Analytics: Integrating MLOps in Travel"

### Academic Project Presentation | Estimated Duration: 30–40 Minutes

> \*\*Speaker Notes Format:\*\*
> - 📢 = What you say out loud
> - 🖥️ = What to show on screen
> - ⭐ = KEY POINT — pause and emphasize clearly
> - ⏱️ = Estimated time checkpoint

\---

## PART 1 — INTRODUCTION \& PROJECT OVERVIEW

### ⏱️ \[0:00 – 3:00 minutes]

\---

🖥️ *Show: Title slide — "Voyage Analytics: Integrating MLOps in Travel"*

📢
"Hello everyone, and welcome to my academic project presentation — **Voyage Analytics: Integrating MLOps in Travel**.

My name is \[Your Name], and today I'm going to walk you through a complete, end-to-end machine learning system that I built around the travel domain — covering three separate ML models, full deployment pipelines, and real MLOps practices.

Before we dive in, let me give you the big picture of what this project is about."

\---

🖥️ *Show: Project architecture overview diagram or bullet list*

📢
"The travel industry generates enormous amounts of data — booking histories, flight records, user demographics, hotel preferences. The goal of this project was to harness that data and build intelligent, deployable ML systems that solve real-world travel problems.

This project has **three core components**:

**Number one** — A **Flight Price Prediction** system, where I used XGBoost to predict flight prices based on route, distance, agency, and flight type — and then wrapped it in a full MLOps pipeline using MLflow, Jenkins, Airflow, Docker, and Kubernetes.

**Number two** — A **Gender Classification Model**, where I fine-tuned BERT, a state-of-the-art transformer model, to predict gender from a user's name — and deployed it as a REST API using Flask and Docker.

**Number three** — A **Hybrid Hotel Recommendation System**, which combines collaborative filtering and content-based filtering to give personalized hotel suggestions — deployed as a live Streamlit web application.

⭐ **KEY POINT: Every single component in this project is not just a trained model — it is a fully deployed, production-ready system. That is what sets it apart.**

All three projects are open-sourced and available on GitHub. The link is: github.com/Sahilpatel6366/Productionization-of-ML-Systems

Let's start with the most technically rich component — the Flight Price Prediction system."

\---

## PART 2 — FLIGHT PRICE PREDICTION + MLOps PIPELINE

### ⏱️ \[3:00 – 14:00 minutes]

\---

🖥️ *Show: Flight price prediction notebook — dataset loading cells*

📢
"The dataset for this project is a travel capstone dataset containing three CSV files: **users.csv**, **flights.csv**, and **hotels.csv**. These three files are connected through a common key — the `userCode` and `travelCode` — which allows us to link user profiles, their flight bookings, and hotel stays together."

\---

### 2A — Exploratory Data Analysis

🖥️ *Show: EDA cells — histplots and correlation heatmap*

📢
"The first thing I did after loading the data was thorough Exploratory Data Analysis, or EDA.

When I plotted the **distribution of flight prices**, I observed a clear right-skewed distribution — most flights are budget-priced, but there are significant outliers with very high prices. This is completely typical in real-world airline data.

⭐ **KEY POINT: The correlation heatmap revealed a moderate positive correlation of 0.64 between price and both `time` and `distance`. This makes perfect real-world sense — longer flights take more time and cover more distance, and they cost more.**

On the other hand, `travelCode` and `userCode` had very weak correlations with price, confirming they are just identifiers and should not be used as model features.

For categorical features — origin city, destination city, flight type, and agency — I used value counts to understand the distribution. This helped me decide which encoding strategy to apply."

\---

### 2B — Model Training

🖥️ *Show: Label encoding and XGBoost training cells*

📢
"For preprocessing, I applied **Label Encoding** to all categorical columns — from city, to city, flight type, and agency — converting them into numeric values suitable for a regression model.

The feature set I used was: `from`, `to`, `flightType`, `agency`, `time`, and `distance`. The target variable was `price`.

I split the data 80-20 — 80% for training, 20% for testing.

⭐ **KEY POINT: I chose XGBoost as my regression algorithm. XGBoost is a gradient boosting framework that is extremely powerful for tabular data and widely used in production ML systems. I configured it with 100 estimators, a learning rate of 0.1, and a max depth of 6.**

The results were impressive:

* **RMSE: 15.25** — the average prediction error is just ₹15
* **MAE: 10.74** — on average, predictions are off by only ₹11
* **R² Score: 1.00** — the model explains nearly 100% of the variance in flight prices

This level of performance validates XGBoost as the right choice for this structured tabular dataset."

\---

### 2C — MLflow Experiment Tracking

🖥️ *Show: MLflow logging code and mlruns output*

📢
"Now here is where the **MLOps** story begins. Training a model is just step one. In production environments, you need to track every experiment — what parameters you used, what metrics you got, and what model was saved. This is what **MLflow** does.

⭐ **KEY POINT: MLflow is an open-source platform for managing the full ML lifecycle. I used it to log the model type (XGBoostRegressor), track my MAE, MSE, and R² score, and save the trained model artifact — all in a structured, reproducible way.**

In the notebook, you can see the `mlflow.start\_run()` block where I log parameters and metrics, followed by `mlflow.sklearn.log\_model()` which saves the model. The entire experiment is stored in the `/mlruns` directory, which I zipped and saved for reproducibility."

\---

### 2D — Jenkins CI/CD Pipeline

🖥️ *Show: Jenkinsfile code*

📢
"The next MLOps component is **Jenkins** — a continuous integration and continuous delivery tool. I created a `Jenkinsfile` that defines a multi-stage pipeline for this project.

The pipeline has the following stages:

1. **Checkout Code** — fetches the latest source code
2. **Install Dependencies** — runs pip install from requirements.txt
3. **Train Model** — executes the training script
4. **MLflow Logging** — logs the model and metrics
5. **Build Docker Image** — packages the application
6. **Push to Registry** — pushes the Docker image
7. **Deploy to Kubernetes** — applies the K8s manifests

⭐ **KEY POINT: This Jenkins pipeline represents a fully automated CI/CD workflow. In a real company, every time you push new code or new data, this pipeline would automatically retrain the model, log it, containerize it, and deploy it — with zero manual intervention.**"

\---

### 2E — Apache Airflow DAG

🖥️ *Show: Airflow DAG code — flight\_dag.py*

📢
"The third MLOps component is **Apache Airflow**, which is used for workflow orchestration — basically, scheduling and managing complex data pipelines.

I created a simulated Airflow DAG called `flight\_price\_prediction\_dag`. A DAG — Directed Acyclic Graph — defines the sequence of tasks and their dependencies.

My DAG has four tasks in sequence:

* `load\_data\_task` → `train\_model\_task` → `log\_model\_task` → `notify\_task`

Each task is defined using a `PythonOperator`. The arrow operator `>>` defines task dependency — task 1 must complete before task 2 begins, and so on.

⭐ **KEY POINT: While Airflow cannot run natively in Google Colab, this DAG represents the complete production workflow that would be used in a real MLOps environment to automatically schedule model retraining — for example, every week when new flight data arrives.**"

\---

### 2F — Docker + Kubernetes

🖥️ *Show: Dockerfile and deployment.yaml if available*

📢
"Finally, the deployment layer. The trained model is served as a REST API inside a **Docker container** — making it completely portable and environment-independent. The Jenkins pipeline builds this container automatically.

For scaling, I used **Kubernetes manifests** — a `deployment.yaml` and a `service.yaml` — to define how many replicas of the container to run and how to expose it as a service.

⭐ **KEY POINT: The combination of Docker + Kubernetes means this flight price prediction API can scale horizontally to handle thousands of requests per second — the same architecture used by companies like Uber, Netflix, and Airbnb in production.**

This concludes the Flight Price Prediction component. Let's move to the next model."

\---

## PART 3 — GENDER CLASSIFICATION USING BERT

### ⏱️ \[14:00 – 24:00 minutes]

\---

🖥️ *Show: Gender classification notebook — title cell*

📢
"The second component of this project is a **Gender Classification API using BERT** — a deep learning approach to predict gender from a person's name.

Now, you might ask — why do we need this in a travel system? The answer is: travel platforms often collect only a user's name during booking. Being able to infer demographic information like gender enables better personalization, targeted offers, and analytics — without requiring users to fill out lengthy forms."

\---

### 3A — Dataset Preparation

🖥️ *Show: CSV loading and preprocessing cells*

📢
"The dataset used here is `users.csv`, which contains two key columns: `name` and `gender`. The gender column has values like 'male' and 'female'.

During preprocessing:

* I filtered out any rows where gender wasn't 'male' or 'female' to keep the problem binary
* I encoded the labels: male → 0, female → 1
* I verified the class distribution to check for imbalance

The data was clean, with no missing values — which made this step straightforward."

\---

### 3B — BERT Tokenization

🖥️ *Show: Tokenizer code cell*

📢
"Now here's the core innovation of this project — using **BERT** for a gender classification task.

⭐ **KEY POINT: BERT stands for Bidirectional Encoder Representations from Transformers. It is a pre-trained language model developed by Google that has revolutionized natural language processing. Rather than training a model from scratch, I used transfer learning — taking BERT's pre-trained weights and fine-tuning them for my specific task.**

I used the `bert-base-uncased` tokenizer from Hugging Face. This tokenizer converts each name into a sequence of token IDs with padding and truncation. The output is a tensor of `input\_ids` and `attention\_masks` — both required by BERT.

The shapes of these tensors confirm that every name has been converted to a fixed-length numerical representation that BERT can process."

\---

### 3C — PyTorch Dataset and DataLoader

🖥️ *Show: NameGenderDataset class and DataLoader cells*

📢
"I created a custom PyTorch Dataset class called `NameGenderDataset` to wrap the tokenized inputs and labels. This class implements the `\_\_len\_\_` and `\_\_getitem\_\_` methods — the standard interface PyTorch requires.

I then split the data 80-20 into training and validation sets and created DataLoaders with a batch size of 16.

⭐ **KEY POINT: Using DataLoaders is critical for efficient GPU training. Instead of loading all data at once, DataLoaders feed data to the model in batches, shuffling at each epoch — which prevents the model from memorizing the order of training examples.**"

\---

### 3D — Fine-Tuning BERT

🖥️ *Show: Training loop cell*

📢
"For the model, I loaded `BertForSequenceClassification` from Hugging Face — a version of BERT with a classification head on top, configured for `num\_labels=2` (male and female).

I moved the model to GPU using CUDA if available, which dramatically speeds up training.

The optimizer I used was **AdamW** — the standard optimizer for transformer fine-tuning — with a learning rate of `2e-5`. This is a very small learning rate because we're fine-tuning a pre-trained model, not training from scratch.

I trained for **3 epochs**. In each epoch:

* The model runs forward pass for each batch
* Computes cross-entropy loss
* Runs backpropagation
* Updates weights via the optimizer

⭐ **KEY POINT: Fine-tuning BERT even for just 3 epochs on a name dataset yields excellent performance, because BERT has already learned rich linguistic representations from billions of text tokens. We are simply redirecting that knowledge toward our specific task.**"

\---

### 3E — Evaluation

🖥️ *Show: Validation evaluation cell*

📢
"After training, I evaluated the model on the held-out validation set. The model runs in `eval()` mode — turning off dropout layers — and predictions are made with `torch.no\_grad()` to avoid unnecessary gradient computation.

The validation accuracy confirms the model is performing well at predicting gender from names — a non-trivial task, since names can be gender-neutral or culturally specific."

\---

### 3F — Flask API + Docker Deployment

🖥️ *Show: app.py Flask code*

📢
"After saving the fine-tuned model and tokenizer using `save\_pretrained()`, I deployed it as a REST API using **Flask**.

The API has a single `/predict` endpoint that accepts a POST request with a JSON body containing a `name` field. Inside the endpoint, the name is tokenized using the saved BERT tokenizer, passed through the model, and the predicted class is returned as either 'male' or 'female'.

⭐ **KEY POINT: This Flask API was then containerized using Docker. The Docker image bundles the model weights, the tokenizer, the API code, and all dependencies into a single portable artifact. Any machine with Docker can run this gender classification service instantly — no environment setup required.**

This is exactly how ML models are deployed in industry — not as raw scripts, but as versioned, containerized APIs."

\---

## PART 4 — HYBRID HOTEL RECOMMENDATION SYSTEM

### ⏱️ \[24:00 – 34:00 minutes]

\---

🖥️ *Show: Hotel recommendation notebook — intro markdown*

📢
"The third and final component is the one I'm most proud of from a user-experience perspective — a **Hybrid Hotel Recommendation System**, deployed as a live interactive web application.

The system uses two recommendation strategies combined into one — collaborative filtering and content-based filtering — making it a true hybrid recommender."

\---

### 4A — Dataset and Preprocessing

🖥️ *Show: Data loading and cleaning cells*

📢
"The dataset is `hotel data set.csv`, containing columns like `userCode`, hotel `name`, `place`, `days`, `price`, and `total` — the total amount a user paid for their stay.

During preprocessing:

* I converted the date column to a proper datetime format
* Dropped rows with missing values
* Removed duplicate records
* Extracted unique hotels and unique users for modeling

⭐ **KEY POINT: Since this dataset doesn't have explicit star ratings, I created a synthetic rating by normalizing the `total` column to a 1–5 scale using MinMaxScaler. The assumption is that a higher total spend reflects a stronger user preference for that hotel — a smart proxy for a rating.**"

\---

### 4B — Collaborative Filtering

🖥️ *Show: Surprise library training cells*

📢
"The first approach is **Collaborative Filtering**, which recommends hotels based on what similar users have liked. I used the **Surprise library** — a Python scikit specifically built for recommender systems.

I first tried a `KNNBasic` model — K-Nearest Neighbors — with item-based similarity using the Mean Squared Difference metric. This achieved an RMSE of 0.97 on the test set.

Then I upgraded to the **SVD model** — Singular Value Decomposition — which is the algorithm that won the famous Netflix Prize competition for movie recommendations. SVD learns latent factors that explain user-hotel interaction patterns.

⭐ **KEY POINT: SVD doesn't just memorize past behavior — it learns hidden patterns, or latent factors, that explain why a user preferred a hotel. This allows it to make predictions even for hotels a user has never visited.**"

\---

### 4C — Content-Based Filtering

🖥️ *Show: TF-IDF and cosine similarity cells*

📢
"The second approach is **Content-Based Filtering**, which recommends hotels similar in characteristics to what a user has already liked — regardless of what other users did.

I combined hotel name and place into a single text feature field. Then I vectorized this text using **TF-IDF — Term Frequency-Inverse Document Frequency** — which converts text into numerical vectors based on word importance.

From these TF-IDF vectors, I computed a **cosine similarity matrix** between all hotels. Hotels with similar names and locations end up with high cosine similarity scores.

⭐ **KEY POINT: The `get\_similar\_hotels()` function uses this matrix to find the top-N most similar hotels to any given hotel. This ensures diversity in recommendations — even if collaborative filtering misses a hotel, the content-based model can surface it.**"

\---

### 4D — Hybrid Recommendation Logic

🖥️ *Show: Hybrid recommender function*

📢
"The hybrid function brings both approaches together using a **weighted scoring formula**:

> `final\_score = (CF score × 0.7) + (CB score × 0.3)`

⭐ **KEY POINT: This 70-30 weighting is a deliberate design decision. Collaborative filtering gets the higher weight because it captures personalized user behavior — it knows what users like you preferred. Content-based gets 30% to add diversity and surface hotels that may not yet have many ratings.**

Here's how the hybrid pipeline works step by step:

1. For a given user, the SVD model predicts a rating for every hotel
2. The top 10 predicted hotels are taken as candidates
3. For each candidate, the content-based model finds 2 similar hotels
4. All results are merged, deduplicated, and re-ranked by the final weighted score
5. The top 5 unique recommendations are returned

This ensures both **personalization** (from collaborative filtering) and **exploration** (from content-based filtering)."

\---

### 4E — Streamlit Web App Deployment

🖥️ *Show: Streamlit app screenshot or ngrok URL*

📢
"To make this system accessible to real users, I built a **Streamlit web application**. Streamlit is a Python framework that lets you turn a data science script into an interactive web app with minimal code.

The app allows a user to enter their user code, click a button, and instantly receive their top 5 personalized hotel recommendations — displayed with hotel name, location, and predicted rating.

⭐ **KEY POINT: I deployed this Streamlit app using ngrok for public access — giving it a live, shareable URL anyone can open in a browser. This transforms the recommendation system from a Jupyter notebook experiment into a real, accessible product.**

This is the complete lifecycle — from raw data to a working web app in the hands of users."

\---

## PART 5 — PROJECT SUMMARY \& CONCLUSION

### ⏱️ \[34:00 – 38:00 minutes]

\---

🖥️ *Show: Summary slide or final architecture diagram*

📢
"Let me now bring everything together with a summary of what was built and what was learned in this project."

\---

### What Was Built:

📢
"**Component 1 — Flight Price Prediction:**

* XGBoost regression model with R² score of 1.00
* Integrated with MLflow for experiment tracking
* Automated CI/CD pipeline via Jenkins
* Workflow orchestration via Apache Airflow DAG
* Containerized with Docker and deployed on Kubernetes

**Component 2 — Gender Classification API:**

* BERT transformer model fine-tuned for binary gender prediction
* Served as a Flask REST API with `/predict` endpoint
* Containerized with Docker for portable deployment

**Component 3 — Hybrid Hotel Recommendation System:**

* Collaborative filtering using SVD from the Surprise library
* Content-based filtering using TF-IDF and cosine similarity
* Hybrid weighting: 70% collaborative + 30% content-based
* Live Streamlit web application deployed via ngrok"

\---

### Key Takeaways:

📢
"⭐ **KEY POINT 1 — MLOps is not optional. It is essential.**
Training a model is easy. Keeping it running reliably in production — with tracking, versioning, automation, and scalability — is the real engineering challenge. This project demonstrates a complete MLOps stack from model training to Kubernetes deployment.

⭐ **KEY POINT 2 — Transfer Learning is transformative.**
By fine-tuning BERT instead of training a model from scratch, I achieved strong gender classification performance with just 3 training epochs on a relatively small dataset. This is the power of pre-trained transformer models.

⭐ **KEY POINT 3 — Hybrid systems outperform single approaches.**
Neither collaborative filtering nor content-based filtering is perfect on its own. Collaborative filtering suffers from the cold start problem. Content-based filtering lacks personalization. Combining both with a weighted hybrid delivers better, more diverse recommendations.

⭐ **KEY POINT 4 — End-to-end thinking matters.**
Every model in this project was taken all the way from raw data to a deployed, accessible endpoint. This full-pipeline mindset — from data cleaning to containerization — is what separates academic exercises from real-world ML engineering."

\---

### 5A — GitHub \& Resources

🖥️ *Show: GitHub repository*

📢
"All the code, notebooks, Docker configurations, Jenkinsfile, and Airflow DAG for this project are available publicly on GitHub at:

**github.com/Sahilpatel6366/Productionization-of-ML-Systems**

I encourage you to clone the repository, run the notebooks, and explore the deployment configurations. The README contains setup instructions for each component.

This project was an incredibly valuable learning experience — combining machine learning, deep learning, MLOps, and software engineering into one cohesive system. I hope it demonstrates not just what models can do, but how they can be built and shipped responsibly.

Thank you so much for watching. If you have any questions, feel free to leave a comment or reach out. I'll be happy to answer."

\---

🖥️ *Show: End card with name, GitHub link, and project title*

📢
"Thank you!"

\---

\---

## 📋 QUICK REFERENCE: KEY POINTS CHECKLIST

*(Review before recording to make sure all are covered)*

|#|Key Point|Section|
|-|-|-|
|1|All 3 models are fully deployed, not just trained|Introduction|
|2|Price correlated 0.64 with time and distance — real-world insight|Flight EDA|
|3|XGBoost chosen for tabular data — R² = 1.00|Model Training|
|4|MLflow tracks experiments for reproducibility|MLOps|
|5|Jenkins pipeline = fully automated CI/CD|Jenkins|
|6|Airflow DAG = scheduled ML pipeline orchestration|Airflow|
|7|Docker + Kubernetes = scalable production deployment|Deployment|
|8|BERT uses transfer learning — fine-tuned, not trained from scratch|BERT|
|9|DataLoaders = efficient batch-based GPU training|PyTorch|
|10|`total` column normalized to 1–5 to proxy ratings|Hotels|
|11|SVD won the Netflix Prize — world-class CF algorithm|Collaborative Filtering|
|12|TF-IDF + cosine similarity for content-based matching|Content-Based|
|13|70% CF + 30% CB weighting — deliberate design decision|Hybrid|
|14|Streamlit + ngrok = live web app for real users|Deployment|

\---

## 🎙️ RECORDING TIPS

* Speak at a steady pace — aim for 130–140 words per minute
* Pause for 2–3 seconds after every ⭐ KEY POINT
* Always have your screen showing the relevant notebook cell while explaining it
* Keep a glass of water nearby
* Smile — it comes through in your voice!

\---

*Script prepared for: Voyage Analytics — Integrating MLOps in Travel
Estimated video length: 34–40 minutes*

