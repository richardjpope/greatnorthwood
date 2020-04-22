import os
import yaml

def get_config():
  file = open("%s/config.yaml" % os.getcwd())
  return yaml.safe_load(file)