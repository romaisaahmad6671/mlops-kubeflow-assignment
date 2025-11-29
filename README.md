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
```bash
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
```

### Pipeline Walkthrough

1. Compile the pipeline:
   python pipeline.py

2. Upload boston_housing_pipeline.yaml to Kubeflow UI.

3. Create a new Experiment and start a Run.

4. You should see four steps:
   - data-extraction
   - data-preprocessing
   - model-training
   - model-evaluation

5. When the run finishes, check:
   - Metrics tab (model accuracy)
   - Artifacts section (saved model outputs)

---


## 3. Setup Instructions

### 3.1 Clone the Repository
```bash
git clone https://github.com/<your-username>/mlops-kubeflow-assignment.git
cd mlops-kubeflow-assignment
```

### 3.2 Install Python Dependencies
pip install -r requirements.txt

---
## 4. DVC Setup
### 4.1 Initialize DVC
dvc init

### 4.2 Add Dataset

Place your dataset inside data/raw_data.csv and run:

dvc add data/raw_data.csv
git add data/raw_data.csv.dvc .gitignore
git commit -m "Added dataset with DVC tracking"

### 4.3 Configure Remote Storage

(E.g., local remote folder)

dvc remote add -d storage ./dvc_storage

### 4.4 Push Data
dvc push

### 4.5 Configure DVC Remote Storage

mkdir dvc_storage
dvc remote add -d storage ./dvc_storage
dvc push

## 5. Kubeflow Pipeline
### 5.1 Compile the Pipeline
python pipeline.py


This generates:

boston_housing_pipeline.yaml

### 5.2 Running on Kubeflow

Start Minikube

Deploy Kubeflow Pipelines

Open the UI

Upload boston_housing_pipeline.yaml

Run the pipeline


### 5.3 Kubeflow Pipelines Setup

1. Deploy Kubeflow Pipelines:
   kubectl apply -k "github.com/kubeflow/pipelines/manifests/kustomize/cluster-scoped-resources?ref=1.8.5"

2. Wait for services:
   kubectl wait --for=condition=available --timeout=600s deployment/ml-pipeline -n kubeflow

3. Open the UI:
   kubectl port-forward -n kubeflow svc/ml-pipeline-ui 8080:80

4. Access in browser:
   http://localhost:8080/

## 6. CI/CD with Jenkins

Install Jenkins

Create a new Pipeline job

Connect it to this GitHub repo

Jenkins will automatically run the Jenkinsfile:

Stage 1: Environment Setup

Stage 2: Pipeline Compilation (syntax check)

Stage 3: Completion

### 6.1 Jenkins Setup

1. Start Jenkins:
   docker run -p 8081:8080 -p 50000:50000 jenkins/jenkins:lts

2. Open Jenkins at:
   http://localhost:8081/

3. Create a new Pipeline job:
   - Choose “Pipeline”
   - Select “Pipeline from SCM”
   - Add GitHub repo URL

4. Jenkins will run the Jenkinsfile automatically.

