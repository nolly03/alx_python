import importlib.util

def import_variable_from_file(module_name, variable_name):
    spec = importlib.util.spec_from_file_location(module_name, f"{module_name}.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return getattr(module, variable_name)

if __name__ == "__main__":
    a = import_variable_from_file("variable_load_2", "a")
    print("Value of 'a':", a)
