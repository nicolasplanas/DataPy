from pathlib import Path

import win32com.client
import pandas as pd

def open_spreadsheet(file_path):

    excel = win32com.client.Dispatch("Excel.Application")
    excel.Visible = True

    file = str(Path("database/DataPy.xlsx").resolve())
    
    workbook = excel.Workbooks.Open(file)
    workbook.Sheets(file_path).Activate()

def read_excel():

    try:

        df = pd.read_excel("database/DataPy.xlsx")
        return df
    
    except Exception as e:

        print(f"Error reading Excel file: {e}")
        return None