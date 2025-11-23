import pandas as pd

excel_tiedosto = "gbsdata/rawdata2.xls"       # tai .xlsx
csv_tiedosto = "gbsdata/rawdata2.csv"

# Lue Excel-tiedosto
df = pd.read_excel(excel_tiedosto)

# Kirjoita CSV-muotoon
df.to_csv(csv_tiedosto, index=False, encoding="utf-8")

print("Muunnettu onnistuneesti!")
