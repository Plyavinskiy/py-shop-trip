from typing import TypedDict

from app.car import Car
from app.shop import Shop


class CarData(TypedDict):
    brand: str
    fuel_consumption: float


class Customer:
    def __init__(
        self,
        name: str,
        product_cart: dict[str, int],
        location: list[int],
        money: float,
        car: CarData
    ) -> None:
        self.name = name
        self.product_cart = product_cart
        self.location = location
        self.money = money
        self.car = Car(
            brand=car["brand"],
            fuel_consumption=car["fuel_consumption"]
        )

    def pay(self, amount: float) -> None:
        self.money = round(self.money - amount, 2)

    def has_all_products(self, shop: Shop) -> bool:
        return set(self.product_cart).issubset(shop.products)

    def calculate_distance_to_shop(self, shop: Shop) -> float:
        x1, y1 = self.location
        x2, y2 = shop.location
        return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5

    def calculate_fuel_cost_to_shop(
        self,
        shop: Shop,
        fuel_price: float
    ) -> float:
        distance = self.calculate_distance_to_shop(shop)
        fuel_used = (distance * self.car.fuel_consumption) / 100
        return fuel_used * fuel_price

    def calculate_products_cost(self, shop: Shop) -> float:
        return sum(
            shop.products[product] * quantity
            for product, quantity in self.product_cart.items()
        )

    def calculate_trip_cost(
        self,
        shop: Shop,
        fuel_price: float
    ) -> float:
        if not self.has_all_products(shop):
            return float("inf")

        fuel_cost = self.calculate_fuel_cost_to_shop(shop, fuel_price) * 2
        products_cost = self.calculate_products_cost(shop)
        return round(fuel_cost + products_cost, 2)
