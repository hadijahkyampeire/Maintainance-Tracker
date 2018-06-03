import os


class BaseConfig(object):
    """
    Common configurations
    """
    TESTING = False
    DEBUG = False
    SECRET_KEY = os.urandom(24)
    # Put any configurations here that are common across all environments


class TestingConfig(BaseConfig):
    """Configurations for Testing, with a separate test database."""
    TESTING = True
    DEBUG = True


class DevelopmentConfig(BaseConfig):
    """
    Development configurations
    """

    DEBUG = True


class ProductionConfig(BaseConfig):
    """
    Production configurations
    """

    DEBUG = False


app_config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig
}