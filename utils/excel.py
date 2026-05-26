import pandas as pd

def read_excel():

    try:

        df = pd.read_excel("data.xlsx")
        return df
    
    except Exception as e:

        print(f"Error reading Excel file: {e}")
        return None