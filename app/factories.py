from app.config_loader import CustomerData, ShopData
from app.customer import Customer
from app.shop import Shop


def create_customers(customers_data: list[CustomerData]) -> list[Customer]:
    return [
        Customer(
            name=data["name"],
            product_cart=data["product_cart"],
            location=(int(data["location"][0]), int(data["location"][1])),
            money=data["money"],
            car=data["car"]
        )
        for data in customers_data
    ]


def create_shops(shops_data: list[ShopData]) -> list[Shop]:
    return [
        Shop(
            name=data["name"],
            location=(int(data["location"][0]), int(data["location"][1])),
            products=data["products"]
        )
        for data in shops_data
    ]
