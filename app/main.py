import json
import os

from app.customer import Customer
from app.shop import Shop
from app.utils import format_money


def shop_trip() -> None:
    config_path = os.path.join(os.path.dirname(__file__), "config.json")

    try:
        with open(config_path, "r") as config_file:
            data = json.load(config_file)
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f"Error loading config: {e}")
        return

    try:
        fuel_price = data["FUEL_PRICE"]
        customers_data = data["customers"]
        shops_data = data["shops"]
    except KeyError as e:
        print(f"Missing key in config file: {e}")
        return

    customers = []
    for info in customers_data:
        x, y = info["location"]
        location = (int(x), int(y))
        customer = Customer(
            name=info["name"],
            product_cart=info["product_cart"],
            location=location,
            money=info["money"],
            car=info["car"]
        )
        customers.append(customer)

    shops = []
    for info in shops_data:
        x, y = info["location"]
        location = (int(x), int(y))
        shop = Shop(
            name=info["name"],
            location=location,
            products=info["products"]
        )
        shops.append(shop)

    for customer in customers:
        initial_cash = customer.count_cash()
        print(f"{customer.name} has {format_money(initial_cash)} dollars")

        affordable_shops = []
        for shop in shops:
            cost = customer.calculate_trip_cost(shop, fuel_price)
            print(
                f"{customer.name}'s trip to the {shop.name} costs "
                f"{format_money(cost)}"
            )
            if cost <= customer.money:
                affordable_shops.append((shop, cost))

        if affordable_shops:
            best_shop, total_cost = customer.choose_best_shop(affordable_shops)
            print(f"{customer.name} rides to {best_shop.name}\n")

            customer.travel_to(best_shop.location)
            customer.pay(total_cost)
            best_shop.handle_purchase(customer)

            customer.travel_to(customer.home_location)
            print(f"{customer.name} rides home")

            cash = customer.count_cash()
            print(f"{customer.name} now has {format_money(cash)} dollars\n")
        else:
            print(
                f"{customer.name} doesn't have enough money to make "
                f"a purchase in any shop"
            )


if __name__ == "__main__":
    shop_trip()
