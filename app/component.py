import logging

from org.transcrypt.stubs.browser import __pragma__, __envir__, __new__, window

__pragma__("alias", "do_watch", "$watch")
__pragma__("alias", "do_emit", "$emit")
__pragma__("alias", "do_force_update", "$forceUpdate")


from third_party import Vue

ALL_CLASSES = []

__pragma__("tconv")  # Enable truth conversion


def instance_wrapper(func):
    if __envir__.executor_name == "transcrypt":

        def wrapper(arg1, arg2, arg3, arg4):
            wrapped_args = []
            if arg1 != __pragma__("js", "undefined"):
                wrapped_args.append(arg1)
            if arg2 != __pragma__("js", "undefined"):
                wrapped_args.append(arg2)
            if arg3 != __pragma__("js", "undefined"):
                wrapped_args.append(arg3)
            if arg4 != __pragma__("js", "undefined"):
                wrapped_args.append(arg4)
            return func(this, *wrapped_args)

        return wrapper
    else:
        return func


class DataSubscriptions:
    """Container class"""


class ComponentMeta(type):
    def __new__(meta, name, bases, attribs):
        result = type.__new__(meta, name, bases, attribs)
        if name not in ("BaseComponent", "HydraComponent", "HydraDuplexComponent"):
            result.register()
            ALL_CLASSES.append(result)
        return result


class BaseComponent(metaclass=ComponentMeta):
    """
    Base class for Python classes implementing Vue components

    Properties:
        props: The props that this Vue component should accept
    """

    props = []
    subscriptions = {}

    def __init__(self, **kwargs):
        self._watches = {}
        self.logger = logging.getLogger("component").getChild(
            self.__class__.__name__.lower()
        )

    def _create_state(self, component, methods, computed):
        if __envir__.executor_name == "transcrypt":
            data_subscriptions = __new__(Object())
        else:
            data_subscriptions = DataSubscriptions()
            data_subscriptions.__class__ = self.__class__

        # Add all remaining attributes of the python object to the "data" for the Vue component
        for data in dir(self):
            if data in ("props",):
                continue

            if data.startswith("__") or data.startswith("_get_"):
                continue

            if data in methods or data in computed or data in self.__class__.props:
                continue

            setattr(data_subscriptions, data, getattr(self, data))

        return data_subscriptions

    def watch(self, prop_or_data, meth, deep=False):
        options = {"deep": deep}
        self.do_watch(prop_or_data, instance_wrapper(meth), options)

    def emit(self, event_name, value):
        self.do_emit(event_name, value)

    def force_update(self):
        self.do_force_update()

    @classmethod
    def register(cls):
        all_methods = {}
        all_computed = {}

        def _create_state(component=None):
            """Create the state for this instance of the component. Called each time a component is created"""
            if not component:
                component = this

            kwargs = {}
            for prop in cls.props:
                kwargs[prop] = getattr(component, prop)

            self = cls(**kwargs)
            self.logger.info("Calling create state")

            result = self._create_state(component, all_methods, all_computed)
            if __envir__.executor_name != "transcrypt":
                for prop in cls.props:
                    setattr(result, prop, getattr(component, prop, None))
            return result

        async def _creator(resolve, reject):
            """Creator for the vue component. Resolved once, asynchronously and is cached by Vue"""
            # Build a list of all methods and all "python" properties
            try:
                for attr in dir(cls):
                    if attr.startswith("__"):
                        continue
                    if hasattr(cls, "_get_" + attr):
                        continue

                    if callable(getattr(cls, attr)):
                        meth = getattr(cls, attr)

                        # @property generates a helper method that starts with _get_.
                        # Add this as a computed method (and choose the friendly name). Delete
                        # the friendly name from the object
                        if attr.startswith("_get_"):
                            prop_name = attr.replace("_get_", "")
                            all_computed[prop_name] = meth
                        else:
                            all_methods[attr] = instance_wrapper(meth)

                    if __envir__.executor_name != "transcrypt":
                        if isinstance(getattr(cls, attr), property):
                            all_computed[attr] = getattr(cls, attr).fget

                print("Resolving creator: {}".format(cls.__name__))
                resolved_template = await cls.template()
                if not resolved_template:
                    reject(ValueError("Must provide a template"))
                    return

                resolve(
                    {
                        "props": cls.props,
                        "mounted": all_methods.get("mounted", lambda: None),
                        "created": all_methods.get("created", lambda: None),
                        "destroyed": all_methods.get("destroyed", lambda: None),
                        "methods": all_methods,
                        "computed": all_computed,
                        "data": _create_state,
                        "watch": {
                            "$route": all_methods.get(
                                "route_changed", lambda *args: None
                            ),
                        },
                        "template": resolved_template,
                    }
                )
            except:
                reject("FAILURE")

        Vue.component(cls.__name__, _creator)

    @staticmethod
    async def template():
        raise NotImplementedError
