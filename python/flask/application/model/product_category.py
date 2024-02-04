import enum
from sqlalchemy import Enum

from configuration.database import db


class ProductCategoryEnum(enum.Enum):
    apples = 1
    oranges = 2
    strawberries = 3
    bananas = 4
    pumpkins = 5


class ProductCategory(db.Model):
    __tablename__ = "product_category"
    id = db.Column(db.Integer, primary_key=True)
    category = db.Column('category', Enum(ProductCategoryEnum))

    def __init__(self, name):
        self.name = name
