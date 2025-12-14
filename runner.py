import re

from nltk.inference.mace import arguments

lines = []
keywords = ["var", "const", "func", "return"]
build_in = ["print", "input", "len", "typeof"]
operators = ["+", "-", "*", "=", "%"]
punctuators = ['"', '(', ')']
variables = {}


class initVariables:
    def __init__(self, line):
        lineIndex = lines.index(line) + 1
        if 'var' in line:
            if any(t for t in build_in):
                print("func")
            else:
                line = line.replace('var', '').strip()
                equal_index = line.find('=')
                name = line[:equal_index].strip()
                value = line[equal_index + 1:].strip()
                if not variables.get(str(name)):
                    variables.setdefault(str(name), []).append(value)  # appending value
                    variables.setdefault(str(name), []).append(self.get_type(value))  # appending type
                    variables.setdefault(str(name), []).append(len(value))  # appending length
                else:
                    print(f"Error in line {lineIndex}: Variable '{name}' is already defined.")
        else:
            pass

    @staticmethod
    def get_type(value):
        if '"' in value or "'" in value:
            return "string"
        elif re.match(r'^\d+(\.\d+)?$', value):
            return "number"
        elif value == "True" or value == "False":
            return "boolean"

    @staticmethod
    def init_with_function_value():
        pass

class BuildInFunctions:
    def __init__(self, line, type_of_function):
        self.line = line
        self.type_of_function = type_of_function
        # get arguments
        self.first_bracket = line.find('(')
        self.last_bracket = line.rfind(')')
        self.arguments = line[self.first_bracket + 1:self.last_bracket].split(',')
        if self.type_of_function == "print":
            self.print()
        elif self.type_of_function == "input":
            self.input()
        elif self.type_of_function == "len":
            self.len()
        elif self.type_of_function == "typeof":
            self.typeof()

    def print(self):
        out = ""
        for i in self.arguments:
            if '"' in i or "'" in i:  # strings
                out += (i.strip().replace('"', '').replace("'", ''))
            elif re.match(r'^\d+(\.\d+)?$', i.strip()):  # numbers
                out += i
            else:  # object
                if '(' in i: #fuction
                    self.line = self.line.replace('print', '')
                    self.line = self.line[1:len(self.line)-1]
                    id_bracket = self.line.find('(')
                    func_name = self.line[:id_bracket].strip()
                    arguments = self.line[id_bracket + 1: len(self.line) - 1].split(',')
                    if func_name in build_in:
                        if func_name == 'typeof':
                            out += getattr(self, "typeof")(arguments[0])
                else:
                    var_name = i.strip()
                    if var_name in variables:
                        out += variables[var_name][0]  # print value
                    else:
                        print(f"Error: Variable '{var_name}' is not defined.")
        print(out)
    def typeof(self, argument):
        if argument in variables:
            return variables[argument][1]
        elif argument.isdigit():
            return "number"
        elif '"' in argument:
            return "string"
    def input(self, argument):
        print(f"Succesfully called input function {argument}")
        if 'var' in self.line:
            self.line = self.line.replace('var', '').strip()
    def len(self, argument):
        print("Succesfully called input function")


with open("plik.txt", "r", encoding="utf-8") as f:
    for linia in f:
        lines.append(linia.strip())

for line in lines:
    line = line.strip()
    found_keywords = [kw for kw in keywords if re.search(rf"\b{kw}\b", line)]
    found_operators = [op for op in operators if re.search(re.escape(op), line)]
    found_punctuators = [pun for pun in punctuators if re.search(re.escape(pun), line)]

    ltype = None
    if 'var' in found_keywords and '=' in found_operators:
        variable = initVariables(line)
        ltype = ''
    elif any(t in line for t in build_in):
        found_func = [func for func in build_in if re.search(rf"\b{func}\b", line)]
        function = BuildInFunctions(line, found_func[0])
        ltype = f"Built-in function call: {', '.join(found_func)}"

    # print(f"Line: {line}\n keywords: {found_keywords} operators: {found_operators} punctuators: {found_punctuators}\n {ltype}\n\n")
