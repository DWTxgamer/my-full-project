import eel

# Set web files folder and optionally specify which file types to check for
eel.init('web', allowed_extensions=['.js', '.html', '.css', '.png'])

# Define a function to open a local HTML file
@eel.expose
def open_html_file():
    with open('index.html', 'r') as f:
        html = f.read()
    return html

# Start the Eel app
eel.start('main.html', size=(800, 600))