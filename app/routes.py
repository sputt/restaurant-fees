from org.transcrypt.stubs.browser import __new__
from third_party import VueRouter


HomeComponent = {
    "template": """
<home></home>
"""
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

router = None
if VueRouter:
    router = __new__(VueRouter({"routes": routes}))
