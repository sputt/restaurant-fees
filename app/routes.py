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
        "meta": {"title": "Los Angeles", "scroll_to": {"top": 0}},
    },
    {
        "path": "/restaurant/:ident",
        "component": RestaurantComponent,
        "props": True,
        "meta": {
            "title": "",
        },
    },
    {
        "path": "/faq",
        "component": FAQComponent,
        "meta": {
            "title": "FAQ",
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


def scroll_behavior(to_route, from_route, saved_position):
    el = document.querySelector(".md-app-container")
    if not el:
        return
    if "meta" in to_route and "scroll_to" in to_route["meta"]:
        el.scrollTop = to_route["meta"]["scroll_to"]["top"]


def before_each(to_route, from_route, next_route):
    el = document.querySelector(".md-app-container")
    if not el:
        return next_route()
    if "meta" in from_route and "scroll_to" in from_route["meta"]:
        from_route["meta"]["scroll_to"]["top"] = el.scrollTop
    return next_route()


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
    router.beforeEach(before_each)
