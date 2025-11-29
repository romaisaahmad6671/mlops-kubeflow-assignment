# MLOps Pipeline with DVC, Kubeflow Pipelines, and Jenkins

This repository contains the implementation of Assignment 4 for the Cloud MLOps course.  
The project demonstrates a complete MLOps workflow including data versioning, pipeline component creation, Kubeflow-based orchestration, and CI using Jenkins.

---

## 1. Project Overview
This project implements a full Machine Learning Operations (MLOps) pipeline using:

- **DVC** for dataset versioning  
- **Kubeflow Pipelines on Minikube** for pipeline orchestration  
- **Random Forest model** trained on the Boston Housing dataset  
- **Jenkins** for CI automation  

The pipeline includes:
1. Data Extraction  
2. Data Preprocessing  
3. Model Training  
4. Model Evaluation  

Each step is written as a Kubeflow component.

---

## 2. Repository Structure
mlops-kubeflow-assignment/
│
├── data/
│ ├── raw_data.csv
│ └── raw_data.csv.dvc
│
├── src/
│ ├── pipeline_components.py
│ ├── model_training.py
│ └── utils.py
│
├── components/
│ ├── data_extraction.yaml
│ ├── data_preprocessing.yaml
│ ├── model_training.yaml
│ └── model_evaluation.yaml
│
├── pipeline.py
├── boston_housing_pipeline.yaml
├── requirements.txt
├── Dockerfile
└── Jenkinsfile


---

## 3. Setup Instructions

### 3.1 Clone the Repository
```bash
git clone https://github.com/<your-username>/mlops-kubeflow-assignment.git
cd mlops-kubeflow-assignment
3.2 Install Python Dependencies
pip install -r requirements.txt

---
4. DVC Setup
4.1 Initialize DVC
dvc init

4.2 Add Dataset

Place your dataset inside data/raw_data.csv and run:

dvc add data/raw_data.csv
git add data/raw_data.csv.dvc .gitignore
git commit -m "Added dataset with DVC tracking"

4.3 Configure Remote Storage

(E.g., local remote folder)

dvc remote add -d storage ./dvc_storage

4.4 Push Data
dvc push

5. Kubeflow Pipeline
5.1 Compile the Pipeline
python pipeline.py


This generates:

boston_housing_pipeline.yaml

5.2 Running on Kubeflow

Start Minikube

Deploy Kubeflow Pipelines

Open the UI

Upload boston_housing_pipeline.yaml

Run the pipeline

6. CI/CD with Jenkins

Install Jenkins

Create a new Pipeline job

Connect it to this GitHub repo

Jenkins will automatically run the Jenkinsfile:

Stage 1: Environment Setup

Stage 2: Pipeline Compilation (syntax check)

Stage 3: Completion

7. Final Deliverables

DVC versioning proof

Kubeflow run screenshots

Jenkins successful build

Full working repository

