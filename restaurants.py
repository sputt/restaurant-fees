from typing import Iterable


class Restaurant:
    def __init__(self, uuid, name) -> None:
        self.uuid = uuid
        self.name = name


class Fee:
    def __init__(self, description: str, percent: float) -> None:
        self.description = description
        self.percent = percent


class RestaurantList:
    def __init__(self, restaurants: Iterable[Restaurant]) -> None:
        self.restaurants = restaurants
        self.visible_restaurants = []


restaurant_list = RestaurantList(
    restaurants=[
        Restaurant(uuid="1234", name="El Torito"),
    ]
)
