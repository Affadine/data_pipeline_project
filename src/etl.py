import json
import pandas as pd

from data_processing import read_drugs_csv, read_pubmed_csv, read_pubmed_json, read_clinical_trials_csv


def extract_data():
    """Data extraction from source files."""
    drugs_df = read_drugs_csv("data/drugs.csv")
    pubmed_df = read_pubmed_csv("data/pubmed.csv")
    pubmed_json_data = read_pubmed_json("data/pubmed.json")
    clinical_trials_df = read_clinical_trials_csv("data/clinical_trials.csv")

    # Concatenation des données pubmed
    pubmed_df = pd.concat([pubmed_df, pd.DataFrame(pubmed_json_data)])

    return drugs_df, pubmed_df, clinical_trials_df


def transform_data(drugs_df, pubmed_df, clinical_trials_df):
    # Filtering of drugs mentioned in PubMed titles.
    pubmed_drugs_mentions = set()
    for _, row in pubmed_df.iterrows():
        title = row['title']
        for _, drug_row in drugs_df.iterrows():
            drug_name = drug_row['drug']
            if drug_name.lower() in title.lower():
                pubmed_drugs_mentions.add(drug_name)

    # Filtering of drugs mentioned in clinical trial titles.
    clinical_trials_drugs_mentions = set()
    for _, row in clinical_trials_df.iterrows():
        title = row['scientific_title']
        for _, drug_row in drugs_df.iterrows():
            drug_name = drug_row['drug']
            if drug_name.lower() in title.lower():
                clinical_trials_drugs_mentions.add(drug_name)

    # Creating the JSON model
    drug_graph = {
        "drugs": []
    }

    # Add each drug to the JSON template with its mentions and newspaper mentions
    for _, drug_row in drugs_df.iterrows():
        drug_name = drug_row['drug']

        drug_info = {
            "name": drug_name,
            "mentions": [],
            "mentioned_by_journals": []
        }

        # Add mentions in PubMed publications
        if drug_name in pubmed_drugs_mentions:
            publication_info = {
                "source": "PubMed",
                "publications": []
            }
            for _, pubmed_row in pubmed_df.iterrows():
                title = pubmed_row['title']
                journal = pubmed_row['journal']
                if drug_name.lower() in title.lower():
                    publication_info["publications"] .append({
                        "title": title,
                        "date": pubmed_row['date']
                    })
                    drug_info["mentioned_by_journals"].append({
                        "journal_name": journal,
                        "date": pubmed_row['date']
                    })
            drug_info["mentions"].append(publication_info)


        # Add mentions in clinical trials
        if drug_name in clinical_trials_drugs_mentions:
            publication_info = {
                "source": "Essai_clinique",
                "publications": []
            }
            for _, clinical_trial_row in clinical_trials_df.iterrows():
                title = clinical_trial_row['scientific_title']
                journal = clinical_trial_row['journal']
                if drug_name.lower() in title.lower():
                    publication_info["publications"].append({
                        "title": title,
                        "date": clinical_trial_row['date']
                    })
                    drug_info["mentioned_by_journals"].append({
                        "journal_name": journal,
                        "date": clinical_trial_row['date']
                    })
            drug_info["mentions"].append(publication_info)

        drug_graph["drugs"].append(drug_info)
    return drug_graph


def load_data(data, output_file):
    """Loading transformed data into a JSON file."""
    try:
        with open(output_file, 'w') as file:
            json.dump(data, file, indent=4)  # Écrire les données au format JSON
    except Exception as e:
        raise Exception(f"Error loading data : {str(e)}")
