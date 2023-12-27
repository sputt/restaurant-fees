from org.transcrypt.stubs.browser import __envir__, window

Vue = None
VueRouter = None
io = None

if __envir__.executor_name == "transcrypt":
    Vue = window.Vue
    VueRouter = window.VueRouter
    io = window.io
