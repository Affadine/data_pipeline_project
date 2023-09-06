import json

from etl import extract_data, transform_data, load_data


def journal_with_most_unique_drugs_mentions(json_file_path):
    # Charger le fichier JSON produit par la data pipeline
    with open(json_file_path, "r") as json_file:
        data = json.load(json_file)

    # Initialiser un dictionnaire pour compter le nombre de médicaments par journal
    journal_mentions_count = {}

    # Parcourir la structure JSON pour compter les mentions par journal
    for drug_info in data["drugs"]:
        for mention in drug_info.get("mentioned_by_journals", []):
            journal_name = mention["journal_name"]
            if journal_name not in journal_mentions_count:
                journal_mentions_count[journal_name] = set()
            journal_mentions_count[journal_name].add(drug_info["name"])

    # Trouver le journal avec le plus grand nombre de médicaments mentionnés
    max_journal = max(journal_mentions_count, key=lambda k: len(journal_mentions_count[k]))
    max_mentions_count = len(journal_mentions_count[max_journal])

    print(f"Le journal qui mentionne le plus de médicaments différents est : {max_journal}")
    print(f"Nombre de médicaments mentionnés dans ce journal : {max_mentions_count}")


def main():
    try:
        # Extraction des données depuis les fichiers sources
        drugs_df, pubmed_df, clinical_trials_df = extract_data()

        # Transformation des données pour construire le graphe de liaison
        transformed_data = transform_data(drugs_df, pubmed_df, clinical_trials_df)

        # Chargement des données transformées dans un fichier JSON
        load_data(transformed_data, "results/graph_data.json")

        print("Pipeline de données terminée avec succès.")

        # journal mentionnant le plus de medicaments  différents
        journal_with_most_unique_drugs_mentions("results/graph_data.json")

    except Exception as e:
        print(f"Une erreur s'est produite : {str(e)}")


if __name__ == "__main__":
    main()
