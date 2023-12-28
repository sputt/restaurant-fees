from component import BaseComponent
from stubs import fetch_template


class About(BaseComponent):
    def __init__(self) -> None:
        super().__init__()

    @staticmethod
    async def template():
        return await fetch_template("templates/about.html")
