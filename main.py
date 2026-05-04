import json

def load_data(file_path):
    """ Lädt die JSON_Tierdaten aus der Datei """
    with open(file_path, "r") as handle:
        return json.load(handle)

# Daten Laden
animals_data = load_data("animals_data.json")

for animal in animals_data:
    print(f"Name: {animal.get('name')}")

    characteristics = animal.get("characteristics", {})
    if "diet" in characteristics:
        print(f"Diet {characteristics.get['diet']}")

    if "type" in characteristics:
        print(f"Type {characteristics.get['type']}")


    print("")