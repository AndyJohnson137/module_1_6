my_dict = {'Владимир': 1981, 'Игорь': 1970, 'Алина': 2002, 'Виктория': 1995}
print("Dict:",my_dict)
print("Existing value:",my_dict['Алина'])
print("Not existing value:",my_dict.get('Сергей'))
my_dict.update({'Денис': 2000,'Валерия': 2003})
del_t=my_dict.pop('Игорь')
print("Deleted value:",del_t)
print("Modified dictionary:",my_dict)
my_set = {6, 1, 3, 4, "Телега", 8, 4, 6.5321, 1, (6, 8, 25.4), 4, 6, "Телега", 3}
print("Set:",my_set)
my_set.update({14, "Чайник"})
my_set.discard(6.5321)
print(f"Modified set:" ,my_set)