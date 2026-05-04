import json

def load_data(file_path):
    """ Lädt die JSON_Tierdaten aus der Datei """
    with open(file_path, "r") as handle:
        return json.load(handle)

# Daten Laden
animals_data = load_data("animals_data.json")

output = ""
for animal in animals_data:
    output += f"Name: {animal.get('name')}\n"

    characteristics = animal.get("characteristics", {})
    if "diet" in characteristics:
        output += f"Diet {characteristics.get('diet')}\n"

    locations = animal.get("locations")
    if locations:
        output += f"Location {locations[0]}\n"

    if "type" in characteristics:
        output += f"Type {characteristics['type']}\n"

    output += "\n"


with open("animals_template.html", "r") as file:
    template_content = file.read()

final_html = template_content.replace("__REPLACE_ANIMALS_INFO__", output)

with open("animals.html", "w") as file:
    file.write(final_html)

print("Erfolg! Die Datei 'animals.html' wurde erstellt.")


