from component import BaseComponent
from fee import process_fees
from stubs import fetch_template, fetch


class Restaurant(BaseComponent):
    props = ["ident"]

    def __init__(self, ident=None):
        super().__init__()
        self.ident = ident
        self.restaurant = None

    async def mounted(self):
        await self.fetch_listing()

    async def fetch_listing(self):
        self.fetching = True
        resp = await fetch("los_angeles_restaurants.json")
        listing_data = await resp.json()
        self.fetching = False
        for item in listing_data:
            if item["name"] == self.ident:
                self.restaurant = item
                break

    @property
    def processed_fees(self):
        return process_fees(self.restaurant["fees"])

    @staticmethod
    async def template():
        return await fetch_template("templates/restaurant.html")
