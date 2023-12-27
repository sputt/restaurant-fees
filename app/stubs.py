from org.transcrypt.stubs.browser import __envir__, window, __new__, __pragma__

fetch = None
fetch_template = None
io = None
Promise = None
AsyncPromise = None

if __envir__.executor_name == "transcrypt":
    fetch = window.fetch
    io = window.io
    if io:
        io.connect = lambda: None
    Promise = window.Promise
    AsyncPromise = window.Promise
    if not window.TEMPLATE_BASE:
        window.TEMPLATE_BASE = ""

    async def _fetch_template(template):
        response = await fetch(window.TEMPLATE_BASE + template)
        return await response.text()

    fetch_template = _fetch_template
else:
    __pragma__("skip")
    from sx_autotest_utils import AttrDict
    import asyncio
    import aiohttp

    def attr_wrap(obj):
        if isinstance(obj, dict):
            result = {}
            for key, value in obj.items():
                if isinstance(value, dict):
                    value = attr_wrap(value)
                result[key] = value
            return AttrDict(result)
        elif isinstance(obj, list):
            result = []
            for item in obj:
                result.append(attr_wrap(item))
            return result
        else:
            return obj

    class ResponseWrapper:
        def __init__(self, response, session):
            self.response = response
            self.session = session

        async def json(self):
            result = attr_wrap(await self.response.json())
            await self.session.close()
            return result

        async def text(self):
            result = await self.response.text()
            await self.session.close()
            return result

    async def _async_get(url):
        session = aiohttp.ClientSession()
        if not url.startswith("http"):
            url = "http://127.0.0.1:5000" + url
        resp_ctx = session.get(url)
        response = await resp_ctx.__aenter__()
        return ResponseWrapper(response, session)

    fetch = _async_get
    import engineio

    import threading

    def _patched_sbt(self, target, *args, **kwargs):
        th = threading.Thread(target=target, args=args, kwargs=kwargs)
        th.daemon = True
        th.start()
        return th

    engineio.Client.start_background_task = _patched_sbt
    import socketio

    connected_ios = []

    class PySocketIO:
        def __init__(self):
            self.sio = socketio.AsyncClient()

        async def connect(self):
            await self.sio.connect("http://127.0.0.1:5000")
            connected_ios.append(self.sio)

        def on(self, event, handler):
            @self.sio.on(event)
            def _on_wrapper(data):
                handler(attr_wrap(data))

        async def emit(self, event, data, callback=None):
            wrapped_callback = None
            if callback is not None:

                def _callback_wrapper(data):
                    if data:
                        return callback(attr_wrap(data))
                    else:
                        return callback({})

                wrapped_callback = _callback_wrapper
            await self.sio.emit(event, data, callback=wrapped_callback)

        async def disconnect(self):
            await self.sio.disconnect()

    io = PySocketIO

    class AsyncioPromise(asyncio.Future):
        def __init__(self, satisfier):
            super().__init__()
            satisfier(self.success, self.failure)

        def success(self, value):
            self.set_result(value)

        def failure(self, ex):
            self.set_exception(ex)

    async def AsyncAsyncioPromise(satisfier):
        promise = asyncio.Future()

        def success(value):
            promise.set_result(value)

        def failure(ex):
            promise.set_exception(ex)

        await satisfier(success, failure)
        return await promise

    Promise = AsyncioPromise
    AsyncPromise = AsyncAsyncioPromise

    def cleanup():
        for sio in connected_ios:
            sio.disconnect()
        connected_ios.clear()

    __pragma__("noskip")
