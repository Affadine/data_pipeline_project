import pandas as pd
import json


def read_drugs_csv(csv_file):
    """Lire le fichier CSV contenant les données des médicaments."""
    try:
        df = pd.read_csv(csv_file)
        return df
    except FileNotFoundError:
        raise FileNotFoundError(f"Le fichier {csv_file} n'a pas été trouvé.")
    except Exception as e:
        raise Exception(f"Erreur lors de la lecture de {csv_file}: {str(e)}")


def read_pubmed_csv(csv_file):
    """Lire le fichier CSV contenant les données PubMed."""
    try:
        df = pd.read_csv(csv_file)
        return df
    except FileNotFoundError:
        raise FileNotFoundError(f"Le fichier {csv_file} n'a pas été trouvé.")
    except Exception as e:
        raise Exception(f"Erreur lors de la lecture de {csv_file}: {str(e)}")


def read_pubmed_json(json_file):
    """Lire le fichier JSON contenant les données PubMed au format JSON."""
    try:
        with open(json_file, 'r') as file:
            data = json.load(file)
        return data
    except FileNotFoundError:
        raise FileNotFoundError(f"Le fichier {json_file} n'a pas été trouvé.")
    except Exception as e:
        raise Exception(f"Erreur lors de la lecture de {json_file}: {str(e)}")


def read_clinical_trials_csv(csv_file):
    """Lire le fichier CSV contenant les données des essais cliniques."""
    try:
        df = pd.read_csv(csv_file)
        return df
    except FileNotFoundError:
        raise FileNotFoundError(f"Le fichier {csv_file} n'a pas été trouvé.")
    except Exception as e:
        raise Exception(f"Erreur lors de la lecture de {csv_file}: {str(e)}")
