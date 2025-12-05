import pandas as pd

FILE_NAME = "data/cantonese.csv"

def load_data():
    """
    Load flashcard data from csv into a list of dictionaries.
    Handles missing values and UTF-8 encoding
    """
    try:
        df = pd.read_csv(FILE_NAME, encoding="UTF-8", low_memory=False)
        df.fillna("")
        df.sort_values(by="Frequency", ascending=False, inplace=True)

        return df.to_dict(orient="records")

    except FileNotFoundError:
        print(f"Error. \nFile {FILE_NAME} does not exist!")
        return []
    except Exception as e:
        print(f"Error \n{e}")

