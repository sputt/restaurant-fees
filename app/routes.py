from org.transcrypt.stubs.browser import __new__
from third_party import VueRouter


HomeComponent = {
    "name": "home",
    "template": """
    <restaurant-list></restaurant-list>
""",
}
RestaurantComponent = {
    "props": ["ident"],
    "template": """
    <restaurant :ident="ident"></restaurant>
""",
}
FAQComponent = {
    "template": "<frequently-asked-questions></frequently-asked-questions>",
}
AboutComponent = {
    "template": "<about></about>",
}
routes = [
    {
        "name": "home",
        "path": "*",
        "component": HomeComponent,
        "meta": {"title": "Restaurant Fees"},
    },
    {
        "path": "/restaurant/:ident",
        "component": RestaurantComponent,
        "props": True,
        "meta": {
            "title": "Restaurant Fees",
        },
    },
    {
        "path": "/faq",
        "component": FAQComponent,
        "meta": {
            "title": "Restaurant Fees - FAQ",
        },
    },
    {
        "path": "/about",
        "component": AboutComponent,
        "meta": {
            "title": "About",
        },
    },
]


def scroll_behavior(scroll_to, scroll_from, saved_position):
    if saved_position:
        return saved_position

    return {"top": 0}


router = None
if VueRouter:
    router = __new__(
        VueRouter(
            {
                "routes": routes,
                "scrollBehavior": scroll_behavior,
            }
        )
    )
