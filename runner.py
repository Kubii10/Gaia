import re

lines = []
keywords = ["var", "const", "func", "return"]
build_in = ["print", "input", "len"]
operators = ["+", "-", "*", "=", "%"]
punctuators = ['"', '(', ')']
variables = {}

class initVariables:
    def __init__(self, line):
        lineIndex = lines.index(line) + 1
        if 'var' in line:
            line = line.replace('var', '').strip()
            equal_index = line.find('=')
            name = line[:equal_index].strip()
            value = line[equal_index + 1:].strip()
            if not variables.get(str(name)):
                variables.setdefault(str(name), []).append(value) #appending value
                variables.setdefault(str(name), []).append(self.get_type(value)) #appending type
                variables.setdefault(str(name), []).append(len(value)) #appending length
            else:
                print(f"Error in line {lineIndex}: Variable '{name}' is already defined.")
        else:
            pass

    def get_type(self, value):
        if '"' in value or "'" in value:
            return "string"
        elif re.match(r'^\d+(\.\d+)?$', value):
            return "number"
        elif value == "True" or value == "False":
            return "boolean"
            
class BuildInFunctions:
    def __init__(self, line, type_of_function):
        self.line = line
        self.type_of_function = type_of_function
        #get arguments
        first_bracket = line.find('(')
        last_bracket = line.rfind(')')
        self.arguments = line[first_bracket + 1:last_bracket].split(',')
        if self.type_of_function == "print":
            self.print_func(self.arguments)
        elif self.type_of_function == "input":
            self.input_func()
        elif self.type_of_function == "len":
            self.len_func()

    def print_func(self, arguments):
        for i in self.arguments:
            if '"' in i or "'" in i: #strings
                print(i.strip().replace('"', '').replace("'", ''))
            elif re.match(r'^\d+(\.\d+)?$', i.strip()): #numbers
                print(i)
            else: #variables
                var_name = i.strip()
                if var_name in variables:
                    print(variables[var_name][0]) #print value
                else:
                    print(f"Error: Variable '{var_name}' is not defined.")
    def input_func(self):
        print("Succesfully called input function")
    def len_func(self):
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

    #print(f"Line: {line}\n keywords: {found_keywords} operators: {found_operators} punctuators: {found_punctuators}\n {ltype}\n\n")
