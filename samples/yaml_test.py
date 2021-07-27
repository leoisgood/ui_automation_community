import os
import yaml

cur_path = os.path.dirname(__file__)
yaml_path = os.path.join(cur_path, '..\\elements_info_datas\\main_page.yaml')


def read_yaml():
    with open(yaml_path, encoding='utf-8') as f:
        data = yaml.load(f.read(), Loader=yaml.FullLoader)
        print(data)
        # print(data["logger"]["name"])


read_yaml()
