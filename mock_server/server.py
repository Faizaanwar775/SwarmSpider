from aiohttp import web
import random


async def home(request):
    return web.Response(text="SwarmSpider Mock Server Running")


async def product(request):
    product_id = int(request.match_info["id"])

    return web.json_response(
        {
            "id": product_id,
            "name": f"Product {product_id}",
            "price": round(random.uniform(20, 1000), 2),
            "category": random.choice(
                [
                    "Electronics",
                    "Books",
                    "Sports",
                    "Clothing",
                ]
            ),
            "url": f"http://127.0.0.1:8000/product/{product_id}",
        }
    )


app = web.Application()

app.router.add_get("/", home)
app.router.add_get("/product/{id}", product)

web.run_app(app, host="127.0.0.1", port=8000)
