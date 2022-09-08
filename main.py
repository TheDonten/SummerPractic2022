# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import os
import subprocess
import ctypes
import sys
import argparse
import string
import json

from Parse_tools_two import parse_tools_two
from Options import Option_tools


class Script:
    options = ""

    def __init__(self):
        self.options = Option_tools()

    def call_cmd(self, arg):
        encoding = os.device_encoding(1) or str(
            ctypes.windll.kernel32.GetOEMCP())
        return subprocess.check_output(arg[0], encoding=encoding, cwd=arg[1])

    def open_txt_file(self, args):
        str = args[0]

        with open(str, 'r') as array_url:
            data = array_url.read().split('\n')
            for url in data:
                if url == "":
                    break
                if url.find("https://") == -1:
                    url = "https://" + url
                    prom = parse_tools_two('1', url)
                    try:
                        self.call_cmd([
                            "ruby whatweb " + url + " --log-json-verbose what_web_file" + " --no-errors" + self.options.get_value(
                                "whatweb"), self.options.get_value("PATH_TOOLS_ONE")[1:]])
                        output2 = self.call_cmd(
                            ["node src/drivers/npm/cli.js " + url + self.options.get_value("wappalyzer"),
                             self.options.get_value("PATH_TOOLS_TWO")[1:]])
                    except:
                        raise ("An exception occured error 001, the details of the in Readme.txt")

                    with open(self.options.get_value("PATH_TOOLS_ONE")[1:] + "/what_web_file", 'a') as json_array:
                        json_in = json.loads(output2)
                        json.dump(json_in, json_array)
                        json_array.close()

                    with open(self.options.get_value("PATH_TOOLS_ONE")[1:] + "/what_web_file", 'r') as json_array:
                        prom.add_json_object(json_array)

                    with open(self.options.get_value("PATH_TOOLS_ONE")[1:] + "/what_web_file", 'w') as json_array:
                        json_array.close()

        return

    def open_url(self, args):
        # Тут получается будут вызовы тулзов и передача им ссылки. Можно тут и распаллелить все.
        # Пока что заглушка, чтобы чисто проверить работоспособность парсера.
        arg = args[0]
        if arg.find("https://") == -1:
            arg = "https://" + args[0]
        prom = parse_tools_two('1', 'acs2.abr.ru')
        # call_cmd(["ruby whatweb " + arg, PATH_TOOLS_ONE + "--verbose"])
        with open('123.txt', 'r') as array_url:
            prom.add_json_object(array_url)
        return

    def help_output(self, args):
        return


if __name__ == '__main__':

    launch = Script()

    commands = {
        'open_with': launch.open_txt_file,
        'url': launch.open_url,
        'help': launch.help_output

    }
    tools_list_string = "\t  - %s\n" * len(commands) % tuple(k for k in commands)

    tool_parser = argparse.ArgumentParser(
        usage='Run the desired program with the -h option to get help for that program.')
    tool_parser.add_argument('cmd', choices=commands.keys())
    tool_parser.add_argument('args', nargs=argparse.REMAINDER)
    tool_opts = tool_parser.parse_args()

    if tool_opts.cmd in commands:
        commands[tool_opts.cmd](tool_opts.args)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
