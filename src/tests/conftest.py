import pytest

from fastapi.testclient import TestClient

from src.main import app


@pytest.fixture(scope="session")
def client():
    """yields an api client"""
    with TestClient(app) as _client:
        yield _client
