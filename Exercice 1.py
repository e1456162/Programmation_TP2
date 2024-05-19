# Création du fichier data.json

import json

nombres = [
    [2, 3],
    [3, 2],
    [1.0, -5.3]
]

with open('data.json', 'w') as f:
    json.dump(nombres, f)

# Programme qui li les tuples du fichier json et qui les transferts dans un nouveau fichier csv
import json
import csv

with open("nombres.json", "r", encoding="UTF8") as f:
    nombres = json.load(f)

with open("data.csv", "w", newline='', encoding="UTF8") as file_csv:
    nombres_csv = csv.writer(file_csv)

    for tuples in nombres:
        nombres_csv.writerow(tuples)