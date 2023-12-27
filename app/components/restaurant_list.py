import logging

from component import BaseComponent
from stubs import fetch_template


class RestaurantList(BaseComponent):
    props = ["restaurants", "filter"]

    def __init__(self, restaurants=None, filter=None) -> None:
        super().__init__()
        self.restaurants = restaurants
        self.filter = filter
        self.logger = logging.getLogger("component.restaurant_list")

    @property
    def filtered_restaurants(self):
        return self.restaurants

    @staticmethod
    async def template():
        return await fetch_template("templates/restaurant-list.html")
