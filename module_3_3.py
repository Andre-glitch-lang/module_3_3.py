def print_params(a=1, b='string', c=True):
    print(a, b, c)


print_params()
print_params(b=25)
print_params(c=[1, 2, 3])

value_list = [4, 'man', 'herb']
value_dict = {'a': "dragon", 'b': "Fox", 'c': 1}
print_params(value_list, value_dict)

print_params(*value_list)
print_params(**value_dict)

value_list2 = [54.32, "Строка"]
print_params(*value_list2, 42)
