import os
import yaml


def load_configuration(config_file: str) -> dict:
    """
    @param: config_file path of config file
    return login account
    """
    account_login_data = list()
    login_account = dict()
    with open(file=config_file, mode='r') as config_obj:
        account_login_data = yaml.safe_load(config_obj)
    try:
        login_account["ak"] = account_login_data["alicloud"]["AccessKeyId"]
        login_account["sk"] = account_login_data["alicloud"]["AccessKeySecret"]
        login_account["reg"] = account_login_data["alicloud"]["RegionId"]

    except KeyError:
        raise KeyError('Please check your config file')

    return login_account


def load_env_variable() -> dict:
    """
    return login account
    """
    account_login_data = list()
    env_variables = ['ALIBABA_CLOUD_ACCESS_KEY_ID', 'ALIBABA_CLOUD_ACCESS_KEY_SECRET', 'REGION_NAME']
    for _, element in enumerate(env_variables):
        var_value = os.environ.get(element)
        account_login_data.append(var_value)

    login_account = dict()
    login_account['ak'] = account_login_data[0]
    login_account['sk'] = account_login_data[1]
    login_account['reg'] = account_login_data[2]
    return login_account
