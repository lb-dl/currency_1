from account.models import User

from faker import Faker

import pytest


@pytest.fixture(autouse=True, scope="function")
def enable_db_access_for_All_tests(db):
    '''
    enable db for all tests
    '''


@pytest.fixture(scope="function", autouse=True)
def user_fix():
    user = User.objects.create()
    yield user


@pytest.fixture(scope="function", autouse=True)
def fake():
    yield Faker()
