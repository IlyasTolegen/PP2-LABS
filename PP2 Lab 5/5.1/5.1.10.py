import re

def camel_to_snake_case(camel_str):
    return re.sub(r'(?<!^)(?=[A-Z])', '_', camel_str).lower()

print(camel_to_snake_case("thisIsCamelCase")) 
