from org.transcrypt.stubs.browser import __envir__

deepcopy = None

if __envir__.executor_name == "transcrypt":

    def _deepcopy(obj):
        result = None
        __pragma__("js", "{}", "result = JSON.parse(JSON.stringify(obj))")
        return result

    deepcopy = _deepcopy

else:
    __pragma__("skip")

    import copy

    deepcopy = copy.deepcopy
