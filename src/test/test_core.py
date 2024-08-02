from test_exception import TestPrivateIndexError,TestPrivateKeyError



test_lis = [1, 3, 5, 7, 9]

test_dic = {
    "prod1": "apple",
    "prod2": "banana",
    "prod3": "pineapple"
}

try:
    print(test_lis[5])
except TestPrivateIndexError as e:
    raise e

try:
    assert test_dic["prod4"] == "grape"
except TestPrivateKeyError as err:
    raise err

