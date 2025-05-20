import pytest
from tests.utils.reset_json_data import reset_servicios_json

@pytest.fixture(autouse=True)
def reset_json_before_each_test():
    reset_servicios_json()
