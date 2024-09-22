import inspect

def introspection_info(obj):
    type_o = type(obj)
    atributs_o = inspect.getmembers(obj)
    metod_o = inspect.ismethod(obj)
    module_o = obj.__class__.__module__

    return {'type':type_o, 'attributes':atributs_o, 'methods': metod_o, 'module':module_o}


number_info = introspection_info(42)
print(number_info)

number_info = introspection_info("__init__")
print(number_info)