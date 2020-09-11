import os
import json
from dictcode import transfer
from pathlib import Path

PROJECT_ROOT = Path(os.path.dirname(os.path.abspath(__file__)))


def test_dict_to_json():
    data = {
        'a': 1,
        'b': 1
    }

    path = PROJECT_ROOT / 'data/test.json'
    data = transfer.dict_to_json(data=data, path=path)
    with open(path, 'r') as f:
        res = json.load(f)

    assert data == res


def test_json_to_dict():
    got = transfer.json_to_dict(path=PROJECT_ROOT / 'data/test.json')
    data = {
        'a': 1,
        'b': 1
    }
    assert got == data


def test_json_to_code():
    got = transfer.json_to_code(path=PROJECT_ROOT / 'data/test.json', variable_name='want',
                                filename=PROJECT_ROOT / 'data/want.py')
    from .data.want import want
    assert got == want


def test_code_to_json():
    code = """{"a": 1, "b": 1}"""
    path = PROJECT_ROOT / 'data/test.json'
    data = transfer.code_to_json(code, path)
    assert data == transfer.json_to_dict(path)
