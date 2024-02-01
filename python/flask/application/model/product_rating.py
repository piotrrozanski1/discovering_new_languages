from configuration.database import db


class ProductRating(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    rating = db.Column(db.Integer)
    description = db.Column(db.String)

    def __init__(self, rating, description):
        self.rating = rating
        self.description = description
