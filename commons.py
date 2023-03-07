import json
import pickle


def find_deep_field(obj, fields, default):
    try:
        result = obj
        for f in fields:
            result = result[f]
        return result if result != '' else default
    except:
        return default


def load_json_file(filename):
    try:
        with open(f"{filename}", encoding='utf_8-sig') as json_file:
            return json.load(json_file)
    except Exception as ex:
        print(f'ERROR {filename}: {ex}')
        return {}


def compare_files(att_one, att_two):
    if att_one == att_two:
        return True
    else:
        return False


def find_in_list(obj_list, param):
    att_list = [find_deep_field(policy, param, '') for policy in obj_list if find_deep_field(policy, param, '')]
    return att_list if len(att_list) > 0 else ''


def find_attribute(obj, param):
    return find_deep_field(obj, param, None)


def get_data_from_pickle(pickle_path):
    pickle_file = open(pickle_path, "rb")
    pickle_data = pickle.load(pickle_file)
    pickle_file.close()

    return pickle_data