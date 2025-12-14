linie = []
varNames = []
varValues = []
operators = ["+", "-", "*", "/"]


def basic_operations_to_var(line):
    line = line.replace(" ", "")
    isoperator = False
    found_operator = None
    for char in line:
        if char in operators:
            found_operator = char
            found_operator_id = line.index(found_operator)
            isoperator = True
            break

    if line[0] == 'var':
        varNames.append(line[1])
        line.strip(" ")
        equity_sign_id = line.index('=')
        operator = next((op for op in operators if op in linia), None)
        operator_id = line.index(operator)

    elif line[0] != 'var':
        index_equal = line.find('=')
        if index_equal != 0 and index_equal < line.find(found_operator):
            if isoperator:
                el2 = line[found_operator_id + 1]
                el1 = line[index_equal + 1]
                if str(el1) in varNames:
                    el1_val = varValues[varNames.index(str(el1))]
                else:
                    el1_val = int(el1)
                if str(el2) in varNames:
                    el2_val = varValues[varNames.index(str(el2))]
                else:
                    el2_val = int(el2)
                if found_operator == '+':
                    varValues[varNames.index(line[0])] = el1_val + el2_val
                elif found_operator == '-':
                    varValues[varNames.index(line[0])] = el1_val - el2_val
                elif found_operator == '*':
                    varValues[varNames.index(line[0])] = el1_val * el2_val
                elif found_operator == '/':
                    varValues[varNames.index(line[0])] = el1_val / el2_val
        else:
            print("Variable not valid")


def printfunc(line):
    output_list = []
    bracket_id = line.index('(')
    end_bracked_id = line.index(')')
    # printing strings
    if '"' in line:
        apostrophe_id = line.index('"')
        copy_list = [i for i in line]
        copy_list.pop(apostrophe_id)
        if '"' in copy_list:
            end_apostrophe_id = copy_list.index('"')
            output_list.extend(line[apostrophe_id + 1:end_apostrophe_id + 1])
        else:
            print("Syntax error")
            pass
    # printing variables
    else:
        var_id = line[bracket_id + 1]
        if var_id in varNames:
            var_id = varNames.index(var_id)
            out = varValues[var_id]
            print(str(out).strip('"'))
        else:
            print("Variable not found")
            pass

    output = "".join(output_list)
    print(output)


def var_init(line):
    tokens = line.split()
    if '"' in tokens[3] or "'" in tokens[3]:
        varNames.append(tokens[1])
        varValues.append(str(tokens[3]))
    else:
        varNames.append(tokens[1])
        varValues.append(int(tokens[3]))


def var_getvalue(var_name):
    var_id = varNames.index(var_name)
    out = varValues[var_id]
    return out


with open("plik.txt", "r", encoding="utf-8") as f:
    for linia in f:
        linie.append(linia.strip())

for linia in linie:
    if "print" in linia:
        printfunc(linia)

    elif any(op in linia for op in operators):
        basic_operations_to_var(linia)

    elif "var" in linia:
        var_init(linia)
