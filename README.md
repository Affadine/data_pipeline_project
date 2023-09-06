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
2. Create a virtual environment (optional but recommended).
3. Install the required dependencies:
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
