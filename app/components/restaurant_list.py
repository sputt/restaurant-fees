import logging

from component import BaseComponent
from stubs import fetch_template

from routes import router


class RestaurantList(BaseComponent):
    props = ["restaurants"]

    def __init__(self, restaurants=None) -> None:
        super().__init__()
        self.restaurants = restaurants
        self.filtered_restaurants = []
        self.filter = None
        self.logger = logging.getLogger("component.restaurant_list")
        self.current_sort = "name"
        self.current_sort_order = "asc"

    def created(self) -> None:
        self.filtered_restaurants = list(self.restaurants)

    def on_select(self, item) -> None:
        router.push("/restaurant/{}".format(item["name"]))

    def custom_sort(self, value):
        reverse = self.current_sort_order == "desc"
        if self.current_sort == "name":
            value.sort(
                key=lambda val: val["name"].lower(),
                reverse=reverse,
            )
        elif self.current_sort == "fees":

            def _fee_key(val) -> float:
                largest_fee = 0.0
                for fee in val["fees"]:
                    largest_fee = max(largest_fee, float(fee["percentage"]))
                return largest_fee

            value.sort(
                key=_fee_key,
                reverse=reverse,
            )
        return value

    def search_table(self):
        self.filtered_restaurants = [
            restaurant
            for restaurant in self.restaurants
            if self.filter is None or self.filter.lower() in restaurant["name"].lower()
        ]

    @staticmethod
    async def template():
        return await fetch_template("templates/restaurant-list.html")
