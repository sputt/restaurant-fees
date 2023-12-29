import logging

from component import BaseComponent
from fee import process_fees
from stubs import fetch_template, fetch

from routes import router


class RestaurantList(BaseComponent):
    def __init__(self) -> None:
        super().__init__()
        self.restaurants = []
        self.filtered_restaurants = []
        self.fetching = False
        self.filter = None
        self.not_yet_filtered = True
        self.logger = logging.getLogger("component.restaurant_list")
        self.current_sort = "name"
        self.current_sort_order = "asc"

    async def mounted(self):
        await self.fetch_listing()

    async def fetch_listing(self):
        self.fetching = True
        resp = await fetch("restaurants.json")
        listing_data = await resp.json()
        self.restaurants.extend(listing_data)
        self.fetching = False
        self.logger.info(
            "Downloaded restaurant list, total {}".format(len(self.restaurants))
        )

    def show_all(self) -> None:
        self.not_yet_filtered = False
        self.filter = None
        self.filtered_restaurants = list(self.restaurants)

    def fee_display(self, value):
        results = process_fees(value["fees"])
        if len(results) < 1:
            return ""
        return results[0]

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
                    if not fee["percentage"].strip():
                        continue
                    if "$" in fee["percentage"]:
                        continue
                    try:
                        largest_fee = max(largest_fee, float(fee["percentage"]))
                    except:
                        pass
                return largest_fee

            value.sort(
                key=_fee_key,
                reverse=reverse,
            )
        return value

    def search_table(self):
        self.not_yet_filtered = False
        self.filtered_restaurants = [
            restaurant
            for restaurant in self.restaurants
            if self.filter is None or self.filter.lower() in restaurant["name"].lower()
        ]

    @staticmethod
    async def template():
        return await fetch_template("templates/restaurant-list.html")
