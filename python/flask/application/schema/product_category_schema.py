from configuration.database import ma

class ProductCategorySchema(ma.Schema):
    class Meta:
        fields = ('id', 'category')


product_category_schema = ProductCategorySchema(strict=True)
products_categories_schema = ProductCategorySchema(many=True, strict=True)
