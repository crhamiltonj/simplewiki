import pytest

from tests.support.configure_test import app
from api import db

import api.models.wikientry as wikientry
from config import TestingConfig


def test_db_create(app):
    app = app(TestingConfig)

    test_model_to_insert = wikientry.WikiEntry("# This is a test entry")
    test_model_to_insert.save()
    db.session.commit()

    assert db.session.query(wikientry.WikiEntry).one()

