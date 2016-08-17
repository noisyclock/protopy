from decimal import Decimal


class Field(object):
    def __init__(self, required=True, default=None):
        self.required = required
        self.default = default

    def validate(self, v):
        return True

class BooleanField(object):
    def validate(self, v):
        return type(v) is bool

class IntegerField(Field):
    def validate(self, v):
        if type(v) is int:
            return True
        else:
            try:
                int(v)
                return True
            except:
                return False 


class StringField(Field):
    def validate(self, v):
        return type(v) is str

class FloatField(Field):
    def validate(self, v):
        return type(v) in (int, float, Decimal)


class ListField(Field):
    def __init__(self, field, required=True):
        self.field = field
        if not isinstance(field, Field):
            self.field = field()
        self.required = required

    def validate(self, v):
        return all(self.field.validate(e) for e in v)

class EnumField(Field):
    def __init__(self, enum_cls, required=True):
        self.enum = enum_cls
        self.required = required

    def validate(self, v):
        return v in self.enum.__members__


class FieldMissing(Exception):
    def __init__(self, name):
        Exception.__init__(self, 'required Field `{}` not privode'.format(name))


class FieldNotValid(Exception):
    def __init__(self, name, v):
        Exception.__init__(self, 'Field `{}` not valid: {} of {}'.format(name, v, type(v)))

class Entity(object):
    def __init__(self, **kwargs):
        fields = [(k, getattr(type(self), k)) for k in dir(type(self)) if isinstance(getattr(type(self), k), Field)]
        for name, field in fields:
            if field.required and name not in kwargs:
                raise FieldMissing(name)
            if name in kwargs:
                if not field.validate(kwargs[name]):
                    raise FieldNotValid(name, kwargs[name])
                setattr(self, name, kwargs[name])
            else:
                setattr(self, name, None)

    def asdict(self):
        result = {}
        fields = [(k, getattr(type(self), k)) for k in dir(type(self)) if isinstance(getattr(type(self), k), Field)]
        for name, _ in fields:
            v = getattr(self, name)
            if isinstance(v, Entity):
                v = v.asdict()
            if v is not None:
                result[name] = v
        return result


class Method(object):
    def __init__(self, name, param, ret):
        self.name = name
        self.param = param
        self.ret = ret


class Service(object):
    def __init__(self, name):
        self.name = name
        self.methods = []
        pass

    def add_method(self, m):
        self.methods.append(m)


if __name__ == '__main__':

    class Person(Entity):
        name = StringField(required=True)
        email = StringField(required=False)
        id = IntegerField(required=True)


    p = Person(name='Ma Tao', id=1)
    print(p.asdict())


