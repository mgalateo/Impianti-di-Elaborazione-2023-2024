import pandas as pd
from scipy.stats.mstats import theilslopes

def theil_sen_from_xlsx(filename, sheet_name):

    # Carica i dati da Excel.
    df = pd.read_excel(filename, sheet_name=sheet_name)

    # Seleziona le colonne x e y.
    x = df["observation"]
    y = df["byte sent"]

    # Calcola la pendenza e l'intercetta.
    b, a, _, _ = theilslopes(y, x)

    return b, a

if __name__ == "__main__":
    # Percorso del file Excel.
    filename = "HomeWork_Regression.xls"

    # Nome del foglio da considerare.
    sheet_name = "EXP1"

    # Calcoliamo la pendenza e l'intercetta.
    b, a = theil_sen_from_xlsx(filename, sheet_name)

    # Stampiamo i risultati.
    print("Pendenza:", b)
    print("Intercetta:", a)
