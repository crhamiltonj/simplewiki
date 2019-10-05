import os


def get_env_variable(name):
    try:
        return os.environ.get(name)
    except KeyError:
        message = f"Expected environment variable {name} not set."
        raise Exception(message)


def create_db_url(_type, db, user=None, pw=None, url=None):
    if _type == "postgresql":
        print(f"URL String: {_type}://{user}:{pw}@{url}/{db}")
        return f"{_type}://{user}:{pw}@{url}/{db}"
    elif _type == "mysql":
        print(f"URL String: {_type}://{user}:{pw}@{url}/{db}")
        return f"{_type}://{user}:{pw}@{url}/{db}"
    elif _type == "sqlite":
        print(f"URL String: {_type}:///{db}")
        return f"{_type}:///{db}"
    else:
        return "Invalid DB specified"


# TODO: Switch to using dotenv
def get_env_db_url(env_setting):
    if env_setting == "development":
        _TYPE = "sqlite"
        USER = ""
        PW = ""
        URL = ""
        DB = "simplewiki_dev.sqlite"
    elif env_setting == "testing":
        _TYPE = "sqlite"
        USER = ""
        PW = ""
        URL = ""
        DB = ""
    elif env_setting == "production":
        _TYPE = "sqlite"
        USER = ""
        PW = ""
        URL = ""
        DB = "simplewiki_prod.sqlite"

    print(f"DB Environment: {_TYPE} {USER} {PW} {URL} {DB} ")

    return create_db_url(_TYPE, USER, PW, URL, DB)


DEV_DB_URL = get_env_db_url("development")
TEST_DB_URL = get_env_db_url("testing")
PROD_DB_URL = get_env_db_url("production")


class Config(object):
    # SQLAlchemy Settings
    SQLALCHEMY_DATABASE_URI = DEV_DB_URL
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Flask Settings
    DEBUG = False
    TESTING = False


class DevelopementConfig(Config):
    DEBUG = True


class TestingConfig(Config):
    SQLALCHEMY_DATABASE_URI = TEST_DB_URL
    DEBUG = True
    TESTING = True


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = PROD_DB_URL
    DEBUG = False
    TESTING = False

