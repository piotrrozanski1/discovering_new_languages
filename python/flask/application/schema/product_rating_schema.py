from configuration.database import ma


class ProductRatingSchema(ma.Schema):
    class Meta:
        fields = ('id', 'rating', 'description')


product_rating_schema = ProductRatingSchema(strict=True)
products_ratings_schema = ProductRatingSchema(many=True, strict=True)
