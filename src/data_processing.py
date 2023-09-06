import pandas as pd
import json


def read_drugs_csv(csv_file):
    """Read the CSV file containing drug data."""
    try:
        df = pd.read_csv(csv_file)
        return df
    except FileNotFoundError:
        raise FileNotFoundError(f"The {csv_file} file was not found.")
    except Exception as e:
        raise Exception(f"Error when reading {csv_file}: {str(e)}")


def read_pubmed_csv(csv_file):
    """Read the CSV file containing PubMed data"""
    try:
        df = pd.read_csv(csv_file)
        return df
    except FileNotFoundError:
        raise FileNotFoundError(f"The {csv_file} file was not found.")
    except Exception as e:
        raise Exception(f"Error when reading {csv_file}: {str(e)}")


def read_pubmed_json(json_file):
    """Read the JSON file containing PubMed data in JSON format."""
    try:
        with open(json_file, 'r') as file:
            data = json.load(file)
        return data
    except FileNotFoundError:
        raise FileNotFoundError(f"The {json_file} file was not found.")
    except Exception as e:
        raise Exception(f"Error when reading {json_file}: {str(e)}")


def read_clinical_trials_csv(csv_file):
    """Read the CSV file containing clinical trial data."""
    try:
        df = pd.read_csv(csv_file)
        return df
    except FileNotFoundError:
        raise FileNotFoundError(f"The {csv_file} file was not found.")
    except Exception as e:
        raise Exception(f"Error when reading {csv_file}: {str(e)}")
