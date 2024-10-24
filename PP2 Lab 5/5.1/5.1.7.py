def snake_to_camel_case(snake_str):
    components = snake_str.split('_')
    return components[0] + ''.join(x.capitalize() for x in components[1:])

print(snake_to_camel_case("this_is_snake_case")) 
