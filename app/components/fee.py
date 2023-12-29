from component import BaseComponent
from fee import process_fees
from stubs import fetch_template, fetch


class FeePill(BaseComponent):
    props = ["fee"]

    def __init__(self, fee=None):
        super().__init__()
        self.fee = fee

    @staticmethod
    async def template():
        return await fetch_template("templates/fee.html")

    @property
    def label(self):
        fee = self.process_fee(self.fee)
        if fee and fee[0]:
            return fee[0]
        else:
            return None

    @property
    def value(self):
        fee = self.process_fee(self.fee)
        if fee:
            return fee[1]
        return None

    def process_fee(self, fee):
        """Process a raw fee from the data into displayable strings."""
        fee_description = None
        fee_value = ""
        if "percentage" in fee:
            percentage = fee["percentage"]
            if not percentage:
                return None
            if "$" in percentage or "?" in percentage or percentage == "see comment":
                fee_value = percentage
            else:
                fee_value = "{}%".format(percentage)
        if "name" in fee:
            fee_description = fee["name"]
        return fee_description, fee_value
