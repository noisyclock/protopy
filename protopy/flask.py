from flask import request
from functools import partial

def _grpc(route, method, f):
    service_name = method.service.name
    method_name = method.name
    path = '/{}/{}'.format(service_name, method_name)
    print(route, path, f)
    def __wrap__(*args, **kwargs):
        print(request.args)
        accept = request
        ret = f(*args, **kwargs)
        return ret
    return route(path)(__wrap__)


flask_grpc = lambda route, method: partial(_grpc, route, method)