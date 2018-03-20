routes = []


def ping_bar():
    return 'Ping bar'


routes.append(dict(
    rule='/ping-bar/',
    view_func=ping_bar))


def save_bar():
    return 'Save bar'


routes.append(dict(
    rule='/save-bar/',
    view_func=save_bar,
    options=dict(methods=['POST',])))
