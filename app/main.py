from datetime import datetime

from itertools import groupby

from org.transcrypt.stubs.browser import __pragma__, __new__, alert

__pragma__("alias", "S", "$")

import logging

from third_party import Vue, VueRouter
from component import BaseComponent

from components.restaurant import *
from components.home import *
from components.restaurant_list import *

from routes import router

logging.basicConfig()
logging.getLogger().setLevel(logging.DEBUG)


TIMEZONE = "UTC"


__pragma__("tconv")  # Enable truth conversion


class Version(BaseComponent):
    props = ["session"]

    @staticmethod
    async def template():
        return """
            <span>
                1.0
            </span>
            """


class RootObject:
    """Root object for the app."""


def _filter_datetime(value):
    time_obj = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
    return time_obj.strftime("%Y-%m-%d %H:%M:%S") + " " + str(TIMEZONE)


def _filter_json(value):
    result = None
    __pragma__("js", "{}", "result = JSON.stringify(value, null, 2)")
    return result


def main():
    root = RootObject()
    router.afterEach(root.on_route_change)

    Vue.filter("datetime", _filter_datetime)
    Vue.filter("pretty", _filter_json)

    app = __new__(
        Vue(
            {
                "el": "#app",
                "data": root,
                "methods": {
                    "toggle_menu": lambda: root.toggle_menu(),
                },
                "router": router,
            }
        )
    )
