from config import create_db_url


def test_create_db_url():
    _type = "sqlite"
    db = "simplewiki.sqlite"
    user = None
    pw = None
    url = None

    result = create_db_url(_type, db, user, pw, url)
    assert result == "sqlite:///simplewiki.sqlite"

