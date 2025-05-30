from flask import render_template
from app import app
from app.models import Element

@app.route('/')
def index():
    elements = Element.query.all()
    return render_template('index.html', elements=elements)

@app.route('/element/<int:atomic_number>')
def element_details(atomic_number):
    element = Element.query.get_or_404(atomic_number)
    return render_template('element_details.html', element=element)
