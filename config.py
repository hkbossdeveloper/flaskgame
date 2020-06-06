class Config(object):
    DEBUG = False
    TESTING = False
    SECRET_KEY  = 'SDHJKHFSDAJHSDKHSA'
    MONGO_URI = 'mongodb://localhost:27017/Tabib'

    UPLOADS = './Home/static/images'

    SESSSION_COOKIE_SECURE = True

class ProductionConfig(Config):
    pass

class DevelopmentConfig(Config):
    DEBUG = True
    ENV = 'development'
    SECRET_KEY  = 'SDHJKHFSDAJHSDKHSA'
    MONGO_URI = 'mongodb://localhost:27017/Tabib'


    SESSSION_COOKIE_SECURE = False


class TestingConfig(Config):
    TESTING = True
    ENV = 'tesing'
    SECRET_KEY  = 'SDHJKHFSDAJHSDKHSA'
    MONGO_URI = 'mongodb://localhost:27017/Tabib'


    SESSSION_COOKIE_SECURE = False