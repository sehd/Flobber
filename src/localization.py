from settings import get_language

with open(f"assets/{get_language()}/strings.csv") as strings:
    _localized_values = {x.split(",")[0]: x.split(",")[1] for x in strings.readlines()}


def get_localized(key):
    return _localized_values[key]
