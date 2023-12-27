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
routes = [
    {"path": "*", "component": HomeComponent},
    {"path": "/restaurant/:ident", "component": RestaurantComponent, "props": True},
]

router = None
if VueRouter:
    router = __new__(VueRouter({"routes": routes}))
