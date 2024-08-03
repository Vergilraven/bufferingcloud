import os
import pytest
import random 
import string
from bufferingcloud.utils.account_loader import load_configuration
from bufferingcloud.utils.account_loader import load_env_variable


# Mock data file
config_file_path = 'tests/test_account_loader.yaml'

# Mock data
valid_config_content = """
alicloud:
  AccessKeyId: 'test_ak'
  AccessKeySecret: 'test_sk'
  RegionId: 'test_region'
"""

invalid_config_content = """
alicloud:
  AccessKeyId: 'test_ak'
  AccessKeySecret: 'test_sk'
  RegionId:
"""

missing_config_content = """
alicloud:
  AccessKeyId: 'test_ak'
  AccessKeySecret:
"""

def generate_account_strings(pass_length: int) -> str:
    """
    @param: pass_length integer
    """
    if pass_length < 24 or pass_length > 30:
        raise ValueError("Length must be between 24 and 30.")
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(pass_length))

def generate_account_configuration(how_many: int) -> list:
    cloud_account = list()
    for _ in range(how_many):
        pass_length = random.randint(24, 30)
        account_config = generate_account_strings(pass_length)
        cloud_account.append(account_config)
    return cloud_account

@pytest.fixture
def create_test_file(tmp_path):
    test_file = tmp_path / "test_account_loader.yaml"
    test_file.write_text(valid_config_content)
    return str(test_file)

def test_load_configuration_success(create_test_file):
    test_ak = generate_account_configuration(2)[0]
    test_sk = generate_account_configuration(2)[1]
    expected_output = {
        "ak": f"{test_ak}",
        "sk": f"{test_sk}",
        "reg": "cn-shenzhen"
    }
    output = load_configuration(create_test_file)
    assert output == expected_output

def test_load_configuration_invalid(create_test_file):
    test_file = create_test_file
    with open(test_file, "w") as f:
        f.write(invalid_config_content)
    with pytest.raises(KeyError):
        load_configuration(test_file)

def test_load_configuration_missing(create_test_file):
    test_file = create_test_file
    with open(test_file, "w") as f:
        f.write(missing_config_content)
    with pytest.raises(KeyError):
        load_configuration(test_file)

# Set up environment variables for the tests.
@pytest.fixture(autouse=True)
def setup_environment_variables():
    os.environ['ALIBABA_CLOUD_ACCESS_KEY_ID'] = generate_account_configuration(2)[0]
    os.environ['ALIBABA_CLOUD_ACCESS_KEY_SECRET'] = generate_account_configuration(2)[1]
    os.environ['REGION_NAME'] = 'cn-shenzhen'
    yield
    # Tear down environment variables after tests.
    del os.environ['ALIBABA_CLOUD_ACCESS_KEY_ID']
    del os.environ['ALIBABA_CLOUD_ACCESS_KEY_SECRET']
    del os.environ['REGION_NAME']

def test_load_env_variable():
    """Test the load_env_variable function."""
    expected_result = {
        'ak': f'{generate_account_configuration(2)[0]}',
        'sk': f'{generate_account_configuration(2)[1]}',
        'reg': 'ch-shenzhen'
    }
    # Call the function to be tested
    actual_result = load_env_variable()
    # Assert that the actual result matches the expected result
    assert actual_result == expected_result
