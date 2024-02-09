from app import app, db
from application.model import product, product_category, product_rating, product_property


def update_db_schema():
    app.app_context().push()
    db.create_all()
    product.Product("Kalafior", 10, 10)
    db.session.commit()


def add_test_data():
    app.app_context().push()
    new_product = product.Product("Kalafior", 10, 10)
    db.session.add(new_product)
    db.session.commit()
