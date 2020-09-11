import ast
import json
import shutil


def dict_to_json(data: dict, path: str) -> dict:
    with open(path, 'w') as f:
        json.dump(data, f)

    return data


def json_to_dict(path: str) -> dict:
    with open(path, 'r') as f:
        res = json.load(f)
        return res


def json_to_code(path: str, variable_name: str, filename: str) -> dict:
    """

    :param path:
    :type path:
    :param variable_name:
    :type variable_name:
    :param filename:
    :type filename:
    :return: json dict
    :rtype:
    """
    data = json_to_dict(path)

    shutil.copy2(path, filename)
    with open(filename, 'r') as f:
        res = f.read()

    with open(filename, 'w') as f:
        f.write(f'{variable_name} = ' + res)

    return data


def code_to_json(code: str, path: str) -> str:
    data = ast.literal_eval(code)
    with open(path, 'w') as f:
        json.dump(data, f)
    return data
