import tomli as tomllib

with open("D:\\poetry\\pyproject.toml", "rb") as file:
    config = tomllib.load(file)
    data = config['tool']['poetry']['dependencies']
    list_of_keys = [key for key in data.keys()]
    my_new_dict = dict(dependencies=list_of_keys)
    print(my_new_dict)
