"""
Copyright 2024 Intelligent Automations LLC
@author Jerome Boyer
"""
import os, yaml, logging
from functools import lru_cache
from pydantic_settings import BaseSettings
from pydantic import ConfigDict
from pydantic_yaml import parse_yaml_raw_as
from importlib import import_module

class AppSettings(BaseSettings):
    model_config = ConfigDict(extra='allow')  # authorize adding attributes dynamically
    api_route: str = "/api/v1"
    version: str = "v0.0.1"
    env_path: str = "../.env"
    data_path: str = "data"
    logging_level: str = "INFO"
    logging_level_int: int = 0
    owl_agent_tool_factory_class: str = "athena.llm.tools.tool_mgr.BaseToolInstanceFactory"

    def get_tool_factory(self):
        module_path, class_name = self.owl_agent_tool_factory_class.rsplit('.',1)
        mod = import_module(module_path)
        klass = getattr(mod, class_name)
        return klass()
        
        
_config = None

# configuration is loaded only once and subsequent requests will use the cached configuration
@lru_cache
def get_config():
    global _config
    if _config is None:
        
        CONFIG_FILE= os.getenv("CONFIG_FILE")
        if CONFIG_FILE:
            print(f"reload config from file:{CONFIG_FILE}")
            with open(CONFIG_FILE, 'r') as file:
                _config = parse_yaml_raw_as(AppSettings,file.read())
        else:
            _config = AppSettings()
        if _config.logging_level == "INFO":
            _config.logging_level_int = logging.INFO
        if _config.logging_level == "DEBUG":
            _config.logging_level_int = logging.DEBUG
        else:
            _config.logging_level_int = logging.WARNING
    return _config

# mostly for testing
def set_config(config):
    global _config
    _config = config
    
    
