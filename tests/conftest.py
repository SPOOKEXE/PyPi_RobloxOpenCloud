
import pytest

def pytest_addoption(parser : pytest.Parser):
	parser.addoption("--id1", action="store", default=None)
	parser.addoption("--id2", action="store", default=None)
	parser.addoption("--id3", action="store", default=None)
	parser.addoption("--id4", action="store", default=None)

# COMMAND LINE ARGUMENT INSERTION
@pytest.fixture
def id1(request : pytest.FixtureRequest):
	return request.config.getoption("--id1")

@pytest.fixture
def id2(request : pytest.FixtureRequest):
	return request.config.getoption("--id2")

@pytest.fixture
def id3(request : pytest.FixtureRequest):
	return request.config.getoption("--id3")

@pytest.fixture
def id4(request : pytest.FixtureRequest):
	return request.config.getoption("--id4")
