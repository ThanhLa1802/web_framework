from .extension import ma
class ProductSchema(ma.Schema):
    class Meta:
        fields = ('product_id', 'product_name', 'description', 'sale_price', 'add_date', "category_id")
class CatSchema(ma.Schema):
    class Meta:
        fields = ('category_id', 'category_name')


