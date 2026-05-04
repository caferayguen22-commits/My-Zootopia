import json

def load_data(file_path):
    """ Lädt die JSON_Tierdaten aus der Datei """
    with open(file_path, "r") as handle:
        return json.load(handle)

# Daten Laden
animals_data = load_data("animals_data.json")

# HTML_Serialisierung
output = ""
for animal in animals_data:
    output += '<li class="cards__item">\n'

    # Name hinzufügen
    output += f" <div class='card__title'>{animal.get('name')}</div><br/>\n"

    # Details hinzufügen
    characteristics = animal.get("characteristics", {})
    if "diet" in characteristics:
        output += f" <strong>DIET:</strong> {characteristics.get('diet')}<br/>\n"

    locations = animal.get("locations")
    if locations:
        output += f" <strong>Location:</strong> {locations[0]}<br/>\n"

    if "type" in characteristics:
        output += f" <strong>Type: </strong> {characteristics['type']}<br/>\n"

    output += "</li>\n"


with open("animals_template.html", "r") as file:
    template_content = file.read()

final_html = template_content.replace("__REPLACE_ANIMALS_INFO__", output)

with open("animals.html", "w") as file:
    file.write(final_html)

print("Prüfe die 'animals.html' im Browser.")


