import json
import re

REGX_CHECK_NAME = r'^[0-9A-Za-z_/:.=\-;]+'

BAN_WORD_NAME_TECH = ["Country", "IP", "RedirectLocation",
                      "Title"]  # Список технологий, которые не нужны. Будет загружаться из настроек

NEED_WEB_WORD = ['name', 'string', 'certainty', 'search', 'version', "confidence", "categories",
                 "module"]  # Поля технологий к которым имеется интерес

SWAP_WORD = {"confidence": 'certainty', "search" : "string"}  # Слова которые имеют одинаковый смысл в данном контексте


class parse_tools_two:
    JSON_PATH_TXT = ""
    JSON_PROM = ""
    URL = ""
    plugins = []

    def __init__(self, path, url):
        self.JSON_PATH_TXT = path
        self.URL = url
        self.JSON_PROM = {
            "site": self.URL,
            "plugins": self.plugins
        }

    def _parse_list(self, data):
        result = []

        for el in data:
            if isinstance(el, list):
                result.append(self._parse_list(el))
            elif isinstance(el, dict):
                if len(data) == 1:
                    result = self._parse_dict(el)
                else:
                    result.append(self._parse_dict(el))
            else:
                return el

        return result

    def _parse_dict(self, data):
        new_dict = {}

        if isinstance(data, dict):
            for key, value in data.items():
                if key in NEED_WEB_WORD:
                    if SWAP_WORD.get(key) is not None:
                        key = SWAP_WORD.get(key)
                    if isinstance(value, list):
                        value = self._parse_list(value)
                    elif isinstance(value, dict):
                        value = self._parse_dict(value)
                    new_dict = new_dict | {key: value}
        return new_dict

    def _parse_json(self, json_in):
        if isinstance(json_in, list):
            key = ""
            result = {}
            for el in json_in[2]:
                key = el[0]
                if not key in BAN_WORD_NAME_TECH:
                    result = self._parse_list(el[1])
                    if isinstance(result, list):
                        result = {"string": result}
                        result['name'] = key
                    else:
                        result['name'] = key
                    if result in self.JSON_PROM["plugins"]:
                        continue
                    self.JSON_PROM["plugins"].append(result)

        if isinstance(json_in, dict):
            result = self._parse_list(json_in["technologies"])
            for el in result:
                if el not in self.JSON_PROM["plugins"]:
                    self.JSON_PROM["plugins"].append(el)

        return

    def add_json_object(self, data):

        str_check = data
        str_check = data.readline()
        while str_check != "":
            json_in = json.loads(str_check)
            self._parse_json(json_in)
            str_check = data.readline()

        with open('dataCheck.json', 'a') as f:
            json.dump(self.JSON_PROM, f)
        return 0
