NAMES_DATABASE = ["kunal", "nirali"]

def get_names():
    return NAMES_DATABASE


def name_exists(given_name):
    return given_name in NAMES_DATABASE
