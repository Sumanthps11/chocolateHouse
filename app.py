from flask import Flask, render_template, request, redirect, url_for
from models import db, Flavor, Ingredient, CustomerSuggestion

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///chocolate_house.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)


# Initialize Database   
with app.app_context():
    db.create_all()

@app.route('/')
def index():
    flavors = Flavor.query.all()
    return render_template('index.html', flavors=flavors)

@app.route('/add_flavor', methods=['GET', 'POST'])
def add_flavor():
    if request.method == 'POST':
        name = request.form['name']
        seasonal = request.form['seasonal']
        new_flavor = Flavor(name=name, seasonal=seasonal)
        db.session.add(new_flavor)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('add_flavor.html')

@app.route('/add_ingredient', methods=['GET', 'POST'])
def add_ingredient():
    if request.method == 'POST':
        flavor_id = request.form['flavor_id']
        name = request.form['name']
        new_ingredient = Ingredient(flavor_id=flavor_id, name=name)
        db.session.add(new_ingredient)
        db.session.commit()
        return redirect(url_for('index'))
    flavors = Flavor.query.all()
    return render_template('add_ingredient.html', flavors=flavors)

@app.route('/suggestion', methods=['GET', 'POST'])
def suggestion():
    if request.method == 'POST':
        flavor_id = request.form['flavor_id']
        suggestion_text = request.form['suggestion']
        new_suggestion = CustomerSuggestion(flavor_id=flavor_id, suggestion=suggestion_text)
        db.session.add(new_suggestion)
        db.session.commit()
        return redirect(url_for('index'))
    flavors = Flavor.query.all()
    return render_template('suggestions.html', flavors=flavors)

@app.route('/ingredients')
def get_ingredients():
    ingredients = Ingredient.query.all()
    return render_template('ingredient.html', ingredients = ingredients)

@app.route('/suggestions')
def get_suggestions():
    suggestions = CustomerSuggestion.query.all()
    return render_template('allsuggestions.html', suggestions=suggestions)

if __name__ == '__main__':
    app.run(debug=True)
