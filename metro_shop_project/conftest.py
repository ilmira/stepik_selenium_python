import pytest

@pytest.fixture()
def set_up():
    print("\nStart test")
    yield
    print("\nFinish test")

@pytest.fixture(scope='module')
def set_group():
    print("\nEnter system")
    yield
    print("\nExit system")