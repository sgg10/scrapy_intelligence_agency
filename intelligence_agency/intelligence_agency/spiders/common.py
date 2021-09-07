import yaml


__config = None

def config():
    global __config
    if not __config:
        with open("./intelligence_agency/spiders/config.yaml", "r") as file:
            __config = yaml.load(file, Loader=yaml.FullLoader)
    return __config