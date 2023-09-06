# Data Pipeline Project

## Overview
This project is aimed at creating a data pipeline for processing and analyzing pharmaceutical data from various sources, including PubMed articles and clinical trials. The goal is to generate a structured JSON file that represents the relationships between medications and their mentions in publications and journals.

## Project Structure
The project is structured as follows:

- `src/`: Contains the source code for the data pipeline.
  - `etl.py`: The main ETL (Extract, Transform, Load) script.
  - `data_processing.py`: Utility functions for reading and processing data.
- `tests/`: Contains unit tests for the project.
- `data/`: Store your input data files here.
- `results/`: The location where the output JSON file will be saved.

## Installation
1. Clone this repository to your local machine.
2. Create a virtual environment (optional but recommended):
    ```bash
   python -m venv venv
   ```
3. Activate the virtual environment:
   ##### 3.1.  On Windows:
    ```bash
        venv\Scripts\activate
    ```
   ##### 3.2.  On macOS ou  Linux:
    ```bash
        source venv/bin/activate

4. Install the required dependencies:
   ```bash
   pip install -r requirements.txt

## Usage
1. Place your input data files in the data/ directory.
2. Run the data pipeline using the following command:
   ```bash
   python src/main.py
3. The processed data will be saved as a JSON file in the results/ directory.

## Configuration
You can customize the behavior of the data pipeline by modifying the configuration settings in etl.py.

## Unit Tests
To run the unit tests, use the following command:
```bash
  python -m unittest discover -s tests
```

## Dockerization
To run the project in a Docker, follow these steps:
```bash
  docker build -t data-pipeline .
  docker run -v ${PWD}/data:/app/data -v ${PWD}/results:/app/results data-pipeline
```

## Industrialization with Airflow on Google Cloud Platform (GCP)

### 1. Create a GCP project
If you don't already have one, create a GCP project from the GCP Console.
### 2. Set up Google Cloud Composer
On GCP, you can use Cloud Composer, a managed service that supports Apache Airflow. Create a Cloud Composer environment by following [the official GCP documentation](https://cloud.google.com/composer/docs?hl=fr) for configuring and managing Airflow.
### 3. Deploy the pipeline in Airflow
Transfer the file containing the data pipeline to the DAGS folder (containing all dags)

## CI/CD Pipeline


Setting up a CI/CD (Continuous Integration/Continuous Deployment) chain automates the development, testing and deployment process, improving quality and speed of delivery. Here's how you could set up a CI/CD chain for your project:

### 1. Configuration de Google Cloud Build

Create a cloudbuild.yaml configuration file detailing the CI/CD pipeline steps. Cloud Build will automatically run tests whenever a code change is detected.

```
steps:
  - name: 'gcr.io/cloud-builders/git'
    args: ['clone', 'https://github.com/Affadine/data_pipeline_project']

  - name: 'python:3.11'
    entrypoint: 'bash'
    args:
      - '-c'
      - |
        pip install -r requirements.txt
        python -m unittest discover -s tests -p '*_test.py'


```

### 2. Automatic deployment
Once your tests have passed, you can configure Cloud Build , Gitlab, etc. to automatically deploy your application.

### 3. Notifications and alerts
Set up notifications and alerts to be informed in the event of CI/CD chain failure.