import inspect
from pprint import pprint

def introspection_info(obj):
    type_o = type(obj)
    atributs_o = dir(obj)
    module_o = obj.__class__.__module__
    id_o = id(obj)

    return {'type': type_o, 'attributes': atributs_o, 'module': module_o, 'id': id_o}


number_info = introspection_info(42)
pprint(number_info)

number_info = introspection_info("__init__")
pprint(number_info)
