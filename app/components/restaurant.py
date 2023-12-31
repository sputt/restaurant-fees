from component import BaseComponent
from fee import process_fees
from stubs import fetch_template, fetch


EDIT_FORMS_LINK = "https://docs.google.com/forms/d/e/1FAIpQLScx-IErAbv9aaEqTNshMai6c1E8FPNxJdgzjeK6n-e0KQV0Rg/viewform"
EDIT_FORMS_PARAMS = {
    "name": "entry.1528293531",
    "location": "entry.1373636429",
    "fee_name": "entry.1270879728",
    "fee_value": "entry.417236974",
    "flags": "entry.1686439545",
    "comments": "entry.1919661410",
}

REMOVE_FORMS_LINK = "https://docs.google.com/forms/d/e/1FAIpQLSctx9b-dl0-QhL5FuTEilkqIm_v3ZGMv_mQwlGOy0HuqC6rtA/viewform"
REMOVE_FORMS_PARAMS = {
    "name": "entry.1017872876",
    "location": "entry.1089914684",
}


class Restaurant(BaseComponent):
    props = ["ident"]

    def __init__(self, ident=None):
        super().__init__()
        self.ident = ident
        self.restaurant = None
        self.fetching = True

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

    @property
    def edit_forms_link(self) -> str:
        url_params = [
            (EDIT_FORMS_PARAMS["name"], self.restaurant["name"]),
            (EDIT_FORMS_PARAMS["location"], self.restaurant["location"]),
        ]
        if self.restaurant["autograt"]:
            url_params.append((EDIT_FORMS_PARAMS["flags"], "Counts as a tip"))

        if self.restaurant["removable"]:
            url_params.append((EDIT_FORMS_PARAMS["flags"], "Removable"))

        if len(self.restaurant["fees"]) > 0:
            fee = self.restaurant["fees"][0]
            if "name" in fee and fee["name"]:
                url_params.append((EDIT_FORMS_PARAMS["fee_name"], fee["name"]))
            if "percentage" in fee:
                url_params.append(
                    (EDIT_FORMS_PARAMS["fee_value"], float(fee["percentage"]))
                )

        query_str = "&".join(
            name + "=" + encodeURI(str(val)) for name, val in url_params
        )
        return EDIT_FORMS_LINK + "?" + query_str

    @property
    def remove_forms_link(self) -> str:
        url_params = [
            (REMOVE_FORMS_PARAMS["name"], self.restaurant["name"]),
            (REMOVE_FORMS_PARAMS["location"], self.restaurant["location"]),
        ]
        query_str = "&".join(
            name + "=" + encodeURI(str(val)) for name, val in url_params
        )
        return REMOVE_FORMS_LINK + "?" + query_str

    @staticmethod
    async def template():
        return await fetch_template("templates/restaurant.html")
