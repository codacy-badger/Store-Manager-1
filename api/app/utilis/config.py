import os
import secrets
basedir = os.path.abspath(os.path.dirname(__file__))


class BaseConfig:
    """ Project environment configurations """
    DEBUG = False
    TESTING = False
    SECRET_KEY = secrets.token_hex(45)


class DevelopmentConfig(BaseConfig):
    """ enables development environment """
    DEBUG = True


class TestingConfig(BaseConfig):
    """ enables testing environment """
    TESTING = True

class ProductionConfig(BaseConfig):
    pass


env_config = dict(
    development = DevelopmentConfig,
    tesing = TestingConfig,
    production = ProductionConfig
)