from component import BaseComponent
from stubs import fetch_template, fetch


class Home(BaseComponent):
    def __init__(self) -> None:
        super().__init__()
        self.fetching = False
        self.restaurants = []

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

    @staticmethod
    async def template():
        return await fetch_template("templates/home.html")
