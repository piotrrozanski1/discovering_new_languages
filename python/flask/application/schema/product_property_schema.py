from configuration.database import ma


class ProductPropertySchema(ma.Schema):
    class Meta:
        fields = ('id', 'weight', 'country_of_origin', 'quality')


product_property_schema = ProductPropertySchema(strict=True)
products_properties_schema = ProductPropertySchema(many=True, strict=True)
