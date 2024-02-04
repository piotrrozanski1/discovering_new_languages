from configuration.database import db


class ProductProperty(db.Model):
    __tablename__ = "product_property"
    id = db.Column(db.Integer, primary_key=True)
    weight = db.Column(db.String)
    country_of_origin = db.Column(db.String)
    quality = db.Column(db.String)

    def __init__(self, weight, country_of_origin, quality):
        self.weight = weight
        self.country_of_origin = country_of_origin
        self.quality = quality
