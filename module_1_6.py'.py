my_dict = {'Ivan' : 1988, 'Maria' : 1999}
print(my_dict)
print(my_dict['Ivan'])
my_dict.update({'Maksim' : 2002,
                'Julia' : 2001})
print(my_dict)
del my_dict['Maria']
print(my_dict)
print(my_dict.get('Maria'))
print(my_dict)

my_set = {1, 1, 2, 2, 3, 3, "Cola", True, (2, 4, 6)}
print(my_set)
my_set.update({5, 7,})
print(my_set)
my_set.discard('Cola')
print(my_set)