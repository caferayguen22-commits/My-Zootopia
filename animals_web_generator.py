import json


def load_data(file_path):
    """Lädt die JSON-Daten aus einer Datei."""
    with open(file_path, "r") as handle:
        return json.load(handle)


def serialize_animal(animal_obj):
    """Konvertiert ein einzelnes Tier-Objekt in ein HTML-Listen-Element."""
    output = '<li class="cards__item">\n'

    # Name des Tieres
    name = animal_obj.get("name")
    output += f'  <div class="card__title">{name}</div>\n'

    # Merkmale
    output += '  <p class="card__text">\n'
    characteristics = animal_obj.get('characteristics', {})

    if 'diet' in characteristics:
        output += f'      <strong>Diet:</strong> {characteristics["diet"]}<br/>\n'

    locations = animal_obj.get('locations')
    if locations:
        output += f'      <strong>Location:</strong> {locations[0]}<br/>\n'

    if 'type' in characteristics:
        output += f'      <strong>Type:</strong> {characteristics["type"]}<br/>\n'

    output += '  </p>\n'
    output += '</li>\n'
    return output


def main():
    """Hauptfunktion zur Steuerung des Web-Generators."""
    # 1. Daten laden
    animals_data = load_data('animals_data.json')

    # 2. HTML-String für alle Tiere generieren
    animals_html = ""
    for animal_obj in animals_data:
        animals_html += serialize_animal(animal_obj)

    # 3. Vorlage lesen
    with open("animals_template.html", "r") as f:
        template_content = f.read()

    # 4. Platzhalter ersetzen
    final_html = template_content.replace("__REPLACE_ANIMALS_INFO__", animals_html)

    # 5. Finale HTML-Datei schreiben
    with open("animals.html", "w") as f:
        f.write(final_html)

    print("Website wurde erfolgreich in 'animals.html' generiert!")


if __name__ == "__main__":
    main()