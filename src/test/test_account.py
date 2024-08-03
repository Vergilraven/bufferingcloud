import os


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


res = load_env_variable()
print(res)
print(type(res))