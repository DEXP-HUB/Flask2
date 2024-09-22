class Config:
    PORT = 5000


class PoductionConfig(Config):
    DEBUG = False
    SERVER_NAME = "0.0.0.0:5555"


class DevelopmentConfig(Config):
    DEBUG = True
    SERVER_NAME = "0.0.0.0:8888"
    PORT = 3333