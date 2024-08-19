from flask import Flask, request, render_template
from PIL import Image
import pytesseract
import spacy

app = Flask(__name__)
nlp = spacy.load('en_core_web_sm')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        file = request.files['file']
        if file:
            image = Image.open(file)
            text = pytesseract.image_to_string(image)
            doc = nlp(text)
            entities = [(ent.text, ent.label_) for ent in doc.ents]
            return render_template('result.html', text=text, entities=entities)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)