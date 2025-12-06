import re

lines = []
keywords = ["var", "const", "func", "return"]
operators = ["+", "-", "*", "=", "%"]
punctuators = ['"', '(', ')']

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
        parts = line.split()
        if len(parts) >= 4:
            ltype = f"Variable with name {parts[1]} and value {parts[3]}"
        else:
            ltype = "Variable assignment (format unclear)"

    print(f"Line: {line}\n keywords: {found_keywords} operators: {found_operators} punctuators: {found_punctuators}\n {ltype}")

