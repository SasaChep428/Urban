my_dict = {'Sasha': 2005, 'Max': 2007}
print('Dict:', my_dict)
print('Existing value: ', my_dict.get('Max'))
print('Not existing value: ', my_dict.get('Maxim'))
my_dict.update({'Anton': 2003,
                'Denis': 2004})
a = my_dict.pop('Max')
print('Deleted value: ', a)
print('Modified dictionary: ', my_dict)

my_set = {1, 2, 2.3, (1, 2, 3), (1, 2, 3), 1, 'a', 'a', 'p'}
print('Set: ', set(my_set))
my_set.add(5.5)
my_set.add(5)
my_set.discard(1)
print('Modified set: ', my_set)