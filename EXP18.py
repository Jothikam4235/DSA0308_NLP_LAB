import re
def fopc_parser(expression):
    pattern = r'([A-Za-z]+)\(([^()]+)\)'
    match = re.fullmatch(pattern, expression.strip())
    if match:
        predicate = match.group(1)
        arguments = match.group(2).split(',')
        print("Valid FOPC Expression")
        print("Predicate:", predicate)
        print("Arguments:", [arg.strip() for arg in arguments])
    else:
        print("Invalid FOPC Expression")
print("Jothika M 192324235")
expression = "Student(John)"
print("Input Expression:", expression)
fopc_parser(expression)