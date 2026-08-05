from schema.models import ProductSchema


def parse_product(data: dict) -> ProductSchema:
    
    return ProductSchema.model_validate(data)
