import random
import string

from src.bufferingcloud.runner import is_ak, is_sk

def generate_acesskey_string(length: int) -> str:
    if length <= 24 or length > 24:
        raise ValueError("Access Key id data uncorrect")
    
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))

def generate_secretkey_string(length: int) -> str:
    if length <= 30 or length > 30:
        raise ValueError("Secret key data uncorrect")
    
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))

def test_is_ak():
    random_ak = generate_acesskey_string(24)
    ak_var = is_ak(random_ak)
    assert type(ak_var) == str
    try: 
        assert type(ak_var) == bool
    except AssertionError:
        print('断言成功')

def test_is_sk():
    random_sk = generate_secretkey_string(30)
    sk_var = is_sk(random_sk)
    assert type(sk_var) == str
    try: 
        assert type(sk_var) == bool
    except AssertionError:
        print('断言成功')