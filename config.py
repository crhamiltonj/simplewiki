import os


def get_env_variable(name):
    try:
        return os.environ.get(name)
    except KeyError:
        message = f"Expected environment variable {name} not set."
        raise Exception(message)


def create_db_url(_type, db, user=None, pw=None, url=None):
    if type == "postgresql":
        return f"{_type}://{user}:{pw}@{url}/{db}"
    elif type == "mysql":
        return f"{_type}://{user}:{pw}@{url}/{db}"
    elif type == "sqlite":
        return f"{_type}:///{db}"
    else:
        return "Invalid DB specified"


# TODO: Switch to using dotenv
def get_env_db_url(env_setting):
    if env_setting == "development":
        _TYPE = get_env_variable("DEV_DBTYPE")
        USER = get_env_variable("DEV_USER")
        PW = get_env_variable("DEV_PW")
        URL = get_env_variable("DEV_URL")
        DB = get_env_variable("DEV_DB")
    elif env_setting == "testing":
        _TYPE = get_env_variable("TEST_DBTYPE")
        USER = get_env_variable("TEST_USER")
        PW = get_env_variable("TEST_PW")
        URL = get_env_variable("TEST_URL")
        DB = get_env_variable("TEST_DB")
    elif env_setting == "production":
        _TYPE = get_env_variable("PROD_DBTYPE")
        USER = get_env_variable("PROD_USER")
        PW = get_env_variable("PROD_PW")
        URL = get_env_variable("PROD_URL")
        DB = get_env_variable("PROD_DB")

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

