import json
import os
from typing import TypedDict


class CustomerData(TypedDict):
    name: str
    product_cart: dict[str, int]
    location: tuple[int, int]
    money: float
    car: dict[str, float]


class ShopData(TypedDict):
    name: str
    location: tuple[int, int]
    products: dict[str, float]


def get_config_path() -> str:
    return os.path.join(os.path.dirname(__file__), "config.json")


def load_config(path: str) -> dict:
    try:
        with open(path, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError) as e:
        raise RuntimeError(f"Error loading config: {e}")


def extract_config_values(
    data: dict
) -> tuple[float, list[CustomerData], list[ShopData]]:
    try:
        fuel_price = data["FUEL_PRICE"]
        customers_data = data["customers"]
        shops_data = data["shops"]
        return fuel_price, customers_data, shops_data
    except KeyError as e:
        raise KeyError(f"Missing key in config file: {e}")
