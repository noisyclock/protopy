from functools import partial
from .entity import Entity
import json


def get_flask_decorator():
    from flask import request
    from flask import Response
    def grpc(route, method, f):
        service_name = method.service.name
        method_name = method.name
        path = '/{}/{}'.format(service_name, method_name)
        # print(route, path, f, path)
        def __wrap__(*args, **kwargs):
            accept = request.headers['Accept']
            print(request.args, accept)
            param = None
            if request.method == 'GET':
                _args = dict((k, v[0] if len(v) == 1 else v) for k, v in request.args.items())
                param = method.param(**_args)
            else:
                param = method.param(**request.json)
            ret = f(param, *args, **kwargs)
            if isinstance(ret, Entity):
                resp = json.dumps(ret.asdict())
                return resp, '200', {'Content-Type': 'application/json'}
            else:
                return ret
        return route(path)(__wrap__)
    return lambda route, method: partial(grpc, route, method)


