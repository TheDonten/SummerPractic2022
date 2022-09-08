
REGX_CHECK_NAME = r'^[0-9A-Za-z_/:.=\-;]+'
REGX_CHECK_NEW_STR = r'^[\n]+'

array = [{"Name" : REGX_CHECK_NAME},{"New_str" : REGX_CHECK_NEW_STR}]

import  re





class Option_tools:

    options = {
        "whatweb" : "",
        "wappalyzer" : "",
        "open_file" : "",
        "PATH_TOOLS_ONE" : "",
        "PATH_TOOLS_TWO" : "",
        "PATH_TOOLS_ONE_TO_JSON" : ""
    }
    def __init__(self):
       self.init_options()


    def get_value(self,key):
        return self.options[key]

    def init_options(self):
        with open("options.txt",'r') as opt:
            str = opt.read()
            while str != '':
                cond = str.find("[")
                if cond != -1:
                    name = re.search(REGX_CHECK_NAME,str[cond + 1:]).group(0)
                    if self.options[name] != None:
                        str = str[len(name) + 1:]
                        if str[0] != "]":
                            raise ("An exception occured error 002, the details of the in error_help.txt")
                        str = str[1:]
                        while str != "" and str[0] != "[":
                            for i in array:
                                for key,value in i.items():
                                    result = re.search(value, str)
                                    if result is None:
                                        continue
                                    if key == "Name":
                                        self.options[name] += " " + result.group(0)
                                        str = str[len(result.group(0)):]
                                    if key == "New_str":
                                        str = str[len(result.group(0)):]
                        continue


                raise ("An exception occured error 002, the details of the in error_help.txt")
                pass
        return



if __name__ == '__main__':
    A = Option_tools()
    A.init_options()
    pass