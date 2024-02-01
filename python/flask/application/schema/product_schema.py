from configuration.database import ma


class ProductSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'price', 'quantity')


product_schema = ProductSchema(strict=True)
products_schema = ProductSchema(many=True, strict=True)
