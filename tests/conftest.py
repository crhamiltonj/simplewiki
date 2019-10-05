import pytest

from api import create_app, db
from config import get_env_db_url
from config import TestingConfig


@pytest.yield_fixture
def app():
    def _app(config_class):
        app = create_app(config_class)
        app.test_request_context().push()

        if config_class is TestingConfig:
            # always start with an empty dn
            db.drop_all()
            from api.models.wikientry import WikiEntry
        return app

    yield _app
    db.session.remove()
    if str(db.engine.url) == TestingConfig.SQLALCHEMY_DATABASE_URI:
        db.drop_all()

