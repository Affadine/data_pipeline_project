import unittest
import pandas as pd

from etl import transform_data


class TestEtl(unittest.TestCase):

    def test_transform_data(self):
        drugs_df = pd.DataFrame({
            "drug": ["DrugA", "DrugB", "DrugC"],
            "id": [1, 2, 3]
        })
        pubmed_df = pd.DataFrame({
            "title": ["Title 1 with DrugA", "Title 2 with DrugB", "Title 3 without drugs"],
            "journal": ["JournalA", "JournalB", "JournalC"],
            "date": ["2021-01-01", "2021-02-01", "2021-03-01"]
        })
        clinical_trials_df = pd.DataFrame({
            "scientific_title": ["Clinical Trial 1 with DrugA", "Clinical Trial 2 with DrugC", "Trial 3 without drugs"],
            "journal": ["JournalA", "JournalC", "JournalD"],
            "date": ["2021-04-01", "2021-05-01", "2021-06-01"]
        })

        result = transform_data(drugs_df, pubmed_df, clinical_trials_df)

        # Checks that the result has the expected structure
        self.assertIn("drugs", result)
        self.assertIsInstance(result["drugs"], list)

        # Checks that drugs and their indications are correct
        drug_a_info = next(drug for drug in result["drugs"] if drug["name"] == "DrugA")
        self.assertEqual(drug_a_info["name"], "DrugA")
        self.assertEqual(len(drug_a_info["mentions"]), 2)  # DrugA mentioned in two publications
        self.assertEqual(len(drug_a_info["mentioned_by_journals"]), 2)  # DrugA mentioned by two journals

        drug_b_info = next(drug for drug in result["drugs"] if drug["name"] == "DrugB")
        self.assertEqual(drug_b_info["name"], "DrugB")
        self.assertEqual(len(drug_b_info["mentions"]), 1)  # DrugB mentioned in one publication
        self.assertEqual(len(drug_b_info["mentioned_by_journals"]), 1)  # DrugB mentioned by one journal


if __name__ == '__main__':
    unittest.main()
