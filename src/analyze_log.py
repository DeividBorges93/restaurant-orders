import csv
from collections import Counter


def log_to_dict(path_to_file, field_names):
    if path_to_file[-4:] != ".csv":
        raise FileNotFoundError(f"Extensão inválida: '{path_to_file}'")

    try:
        with open(path_to_file, "r") as file:
            reader = csv.DictReader(file, fieldnames=field_names)
            return list(reader)
    except FileNotFoundError:
        raise FileNotFoundError(f"Arquivo inexistente: '{path_to_file}'")


def filter_by_customer(orders, customer):
    return [order for order in orders if order.get("customer") == customer]


def get_most_requested_food(orders):
    counter = Counter([order.get("food") for order in orders])
    return counter.most_common(1)[0][0]


def count_food_requests(orders, food):
    return len([order for order in orders if order.get("food") == food])


def count_client_never_requested_foods(orders, customer):
    client_orders = filter_by_customer(orders, customer)
    client_foods = set([order.get("food") for order in client_orders])
    all_food = set([order.get("food") for order in orders])
    never_requested_foods = all_food - client_foods

    return never_requested_foods


def get_client_never_attended_days(orders, customer):
    client_orders = filter_by_customer(orders, customer)
    client_days = set([order.get("day") for order in client_orders])
    all_days = set([order.get("day") for order in orders])
    never_attended_days = all_days - client_days

    return never_attended_days


def analyze_log(path_to_file):
    orders = log_to_dict(path_to_file, ["customer", "food", "day"])

    maria_orders = filter_by_customer(orders, "maria")
    maria_consumes = get_most_requested_food(maria_orders)

    arnaldo_orders = filter_by_customer(orders, "arnaldo")
    arnaldo_ask_hamburguer = count_food_requests(arnaldo_orders, "hamburguer")

    joao_never_asks = count_client_never_requested_foods(orders, "joao")
    joao_didnot_come = get_client_never_attended_days(orders, "joao")

    with open("data/mkt_campaign.txt", "w") as file:
        file.write(
            f"{maria_consumes}\n"
            f"{arnaldo_ask_hamburguer}\n"
            f"{joao_never_asks}\n"
            f"{joao_didnot_come}\n"
        )
