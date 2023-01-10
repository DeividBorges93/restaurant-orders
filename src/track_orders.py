from collections import Counter


class TrackOrders:
    def __init__(self):
        self.__orders = []

    def __len__(self):
        return len(self.__orders)

    def add_new_order(self, customer, order, day):
        self.__orders.append(
            {"customer": customer, "order": order, "day": day}
        )

    def get_most_ordered_dish_per_customer(self, customer):
        counter = Counter(
            [
                order.get("order")
                for order in self.__orders
                if order.get("customer") == customer
            ]
        )
        return counter.most_common(1)[0][0]

    def get_never_ordered_per_customer(self, customer):
        client_orders = [
            order
            for order in self.__orders
            if order.get("customer") == customer
        ]
        client_dishes = set([order.get("order") for order in client_orders])
        all_dishes = set([order.get("order") for order in self.__orders])
        never_requested_dishes = all_dishes - client_dishes

        return never_requested_dishes

    def get_days_never_visited_per_customer(self, customer):
        client_orders = [
            order
            for order in self.__orders
            if order.get("customer") == customer
        ]
        client_days = set([order.get("day") for order in client_orders])
        all_days = set([order.get("day") for order in self.__orders])
        never_attended_days = all_days - client_days

        return never_attended_days

    def get_busiest_day(self):
        counter = Counter([order.get("day") for order in self.__orders])
        return counter.most_common(1)[0][0]

    def get_least_busy_day(self):
        counter = Counter([order.get("day") for order in self.__orders])
        return counter.most_common()[-1][0]
