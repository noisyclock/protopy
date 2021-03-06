import types
from enum import Enum
from functools import partial

from .entity import (BooleanField, Entity, EnumField, IntegerField, ListField,
                     Method, Service, StringField)
from .plyproto import parser as plyproto


class TypeNotFound(Exception):
    def __init__(self, name):
        Exception.__init__(self, 'Type<{}> not found'.format(name))


class Loader(object):
    type_transform = {
        'int32': IntegerField,
        'int64': IntegerField,
        'uint32': IntegerField,
        'uint64': IntegerField,
        'sint32': IntegerField,
        'sint64': IntegerField,
        'bool': BooleanField,
        'string': StringField,
        'bytes': StringField,
    }

    def __init__(self):
        pass

    def load_file(self, fobj, name):
        return self.load(fobj.read(), name)

    def load(self, src, name):
        parser = plyproto.ProtobufAnalyzer()
        result = parser.parse_string(src)
        print(result)
        module = types.ModuleType(name, 'Generated by protoby on the fly')
        self.proto = result
        self.module = module
        # self._gen_enums()
        # self._gen_imports()
        self._gen()
        return self.module

    def _on_elem(self, elem):
        t = type(elem)
        method = '_on_{}'.format(t.__name__)
        print('Call', method)
        method = getattr(self, method)
        return method(elem)

    def _gen(self):
        for elem in self.proto.body:
            name, cls = self._on_elem(elem)
            print('Attr', name, cls)
            setattr(self.module, name, cls)

    def _on_MessageDefinition(self, define):
        attrs = {}
        m_name = define.name.value.pval
        print('MessageDefine', m_name)
        # print(define, attrs)
        for field in define.body:
            if type(field) is plyproto.EnumDefinition:
                e_name, cls = self._on_elem(field)
                attrs[e_name] = cls
                continue

            name = field.name.value.pval
            modifier = field.field_modifier and field.field_modifier.pval
            field_type = None
            if type(field.ftype) is plyproto.DotName:
                ftype = field.ftype.value
                if ftype in attrs and issubclass(attrs[ftype], Enum):
                    field_type = partial(EnumField, attrs[ftype])
                elif issubclass(getattr(self.module, ftype, None), Enum):
                    field_type = partial(EnumField, getattr(self.module, ftype))
                else:
                    raise TypeNotFound(name)
            else:
                ftype = field.ftype.name.pval
                fid = field.fieldId.pval
                print(modifier, ftype, name)
                field_type = self.type_transform[ftype] 

            required = True if modifier not in ('optional', 'singular') else False
            repeated = modifier == 'repeated'
            field_obj = field_type(required=required)

            if repeated:
                field_obj = ListField(field_obj)
            attrs[name] = field_obj
        cls = type(m_name, (Entity,), attrs)
        print('MessageDefine', m_name, cls)
        return m_name, cls

    def _on_MethodDefinition(self, define):
        name = define.name.value.pval
        param = define.name2.value.pval
        ret = define.name3.value.pval
        param = getattr(self.module, param)
        ret = getattr(self.module, ret)
        print(name, param, ret)
        return name, Method(name, param, ret)

    def _on_ServiceDefinition(self, define):
        name = define.name.value.pval
        service = Service(name)
        for _def in define.body:
            _name, prop = self._on_elem(_def)
            setattr(prop, 'service', service)
            setattr(service, _name, prop)
        return name, service

    def _on_EnumDefinition(self, define):
        name = define.name.value.pval
        attrs = {}
        for _def in define.body:
            _name = _def.name.value.pval
            _id = _def.fieldId.pval
            attrs[_name] = _id

        cls = Enum(name, attrs)
        print(name, cls)
        return name, cls 

if __name__ == '__main__':
    define = '''
message Person {
  required string name = 1;
  required int32 id = 2;
  optional string email = 3;
}
message HelloRequest {
  optional string greeting = 1;
}
enum Beauty {
    GAOYUANYUAN = 1;
    LINZHILING = 2;
}
message HelloResponse {
  optional string reply = 1;
}

service HelloService {
  rpc SayHello(HelloRequest) returns(HelloResponse)
}
'''

    m = Loader().load(define, 'test')
    print(m)
