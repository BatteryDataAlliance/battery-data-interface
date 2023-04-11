import yaml
from modules.drivers.pymacnet import PyMacNet
from modules.configurator import Configurator

# Read the YAML file into a Python object
with open("sampleConfig.yaml", "r") as file:
    sampleConfig = yaml.safe_load(file)


configurator = Configurator(sampleConfig, "maccor")

# print(configurator.cyclerConfig.to_dict())

maccor_driver = configurator.get_driver_config()

print(maccor_driver.to_dict())



