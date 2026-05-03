import json

def load_data(file_path):
    """ Lädt die JSON_Tierdaten aus der Datei """
    with open(file_path, "r") as handle:
        return json.load(handle)

# Daten Laden
animals_data = load_data("animals_data.json")

print(animals_data[0])