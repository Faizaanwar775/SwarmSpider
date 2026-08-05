from sqlalchemy import select

from db.database import AsyncSessionLocal
from db.models import Product


async def save_product(product):

    async with AsyncSessionLocal() as session:

        existing = await session.execute(
            select(Product).where(
                Product.url == str(product.url)
            )
        )

        if existing.scalar_one_or_none():

            return False

        db_product = Product(
            id=product.id,
            name=product.name,
            price=product.price,
            category=product.category,
            url=str(product.url),
        )

        session.add(db_product)

        await session.commit()

        return True