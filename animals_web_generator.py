import data_fetcher

def generate_html(animal_data):
    if not animal_data:
        return '<h2>The animal "{}" doesn\'t exist.</h2>'.format(animal_name)
    output = ''
    for animal in animal_data:
        # create a div to hold the animal title
        output += '<li class="cards__item">\n'
        output += f'  <div class="card__title">{animal["name"]}</div>\n'
        output += '  <p class="card__text">\n'
        output += f'      <strong>Location:</strong> {animal["locations"][0]}<br/>\n'
        output += f'      <strong>Type:</strong> {animal["characteristics"].get("type", "Unknown")}<br/>\n'
        output += f'      <strong>Diet:</strong> {animal["characteristics"].get("diet", "Unknown")}<br/>\n'
        output += '  </p>\n'
        output += '</li>\n'
    html = f'''
    <html>
        <head>
            <title>{animal_data[0]['name']}</title>
        </head>
        <body>
            <h1>{animal_data[0]['name']}</h1>
            <ul class="cards">
                {output}
            </ul>
        </body>
    </html>
    '''
    return html

# Get animal name from user
animal_name = input("Enter the name of an animal: ")
animal_data = data_fetcher.fetch_data(animal_name)
html_content = generate_html(animal_data)
with open("animals.html", "w") as file:
    file.write(html_content)
print("Website was successfully generated to the file animals.html.")
