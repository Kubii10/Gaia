import re

lines = []
keywords = ["var", "const", "func", "return"]
operators = ["+", "-", "*", "=", "%"]
punctuators = ['"', '(', ')']

with open("plik.txt", "r", encoding="utf-8") as f:
    for linia in f:
        lines.append(linia.strip())

for line in lines:
    found_keywords = [kw for kw in keywords if re.search(rf"\b{kw}\b", line)]; found_keywords = found_keywords if found_keywords else None
    found_operators = [op for op in operators if re.search(re.escape(op), line)]; found_operators = found_operators if found_operators else None
    found_punctuators = [pun for pun in punctuators if re.search(re.escape(pun), line)]; found_punctuators = found_punctuators if found_punctuators else None

    if 'var' in found_keywords and '=' in found_operators:
        ltype = f"Variable with name {line[1]} and value {line[3]}"

    print(f"Line: {line}\n keywords: {found_keywords}, operators: {found_operators}, punctuators: {found_punctuators}\n, {ltype}")

