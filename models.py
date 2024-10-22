from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# Table Flavor
class Flavor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    seasonal = db.Column(db.String, nullable=False)  # e.g. "Winter", "Summer"
    ingredients = db.relationship("Ingredient", back_populates="flavor")
    suggestions = db.relationship("CustomerSuggestion", back_populates="flavor")

# Table Ingredient
class Ingredient(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    flavor_id = db.Column(db.Integer, db.ForeignKey('flavor.id'))
    flavor = db.relationship("Flavor", back_populates="ingredients")

# Table CustomerSuggestion
class CustomerSuggestion(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    flavor_id = db.Column(db.Integer, db.ForeignKey('flavor.id'))
    suggestion = db.Column(db.Text, nullable=False)
    flavor = db.relationship("Flavor", back_populates="suggestions")