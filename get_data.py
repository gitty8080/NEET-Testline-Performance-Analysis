import pandas as pd
import json
import requests

def fetch_data():
    current_quiz = "https://www.jsonkeeper.com/b/LLQT"
    hist_data_link = "https://api.jsonserve.com/XgAgFJ"

    current_quiz_data = requests.get(current_quiz, verify=False).json()
    hist_data = requests.get(hist_data_link, verify=False).json()

    print(json.dumps(current_quiz_data, indent=4))
    print(json.dumps(hist_data, indent=4))

    # Creating Dataframe for given user's pre-existing data
    hist_df = pd.DataFrame(hist_data)

    return current_quiz_data, hist_df
