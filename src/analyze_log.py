import csv
from collections import Counter


def log_to_dict(path_to_file, field_names):
    with open(path_to_file, "r") as file:
        reader = csv.DictReader(file, fieldnames=field_names)
        return list(reader)


def filter_by_customer(orders, customer):
    return [order for order in orders if order.get("customer") == customer]


def get_most_requested_food(orders):
    counter = Counter([order.get("food") for order in orders])
    return counter.most_common(1)[0][0]


def count_food_requests(orders, food):
    return len([order for order in orders if order.get("food") == food])


def analyze_log(path_to_file):
    orders = log_to_dict(path_to_file, ["customer", "food", "day"])

    maria_orders = filter_by_customer(orders, "maria")
    maria_consumes = get_most_requested_food(maria_orders)

    arnaldo_orders = filter_by_customer(orders, "arnaldo")
    arnaldo_ask_hamburguer = count_food_requests(arnaldo_orders, "hamburguer")

    with open("data/mkt_campaign.txt", "w") as file:
        file.write(
            f"{maria_consumes}\n"
            f"{arnaldo_ask_hamburguer}\n"
        )
