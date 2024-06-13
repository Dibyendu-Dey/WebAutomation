"""
Conftest.py is a centralized fixture available to all Pytest test file.
"""
import pytest


@pytest.fixture(scope="class")
# the scope of this fixture is set to class that means this will get executed before the instantiation of the class
def setup(request):  # request is a object of the fixture
    pass
