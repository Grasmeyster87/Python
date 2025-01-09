db_is_available = False

print(db_is_available)
print(type(db_is_available))

db_is_available = True
print(db_is_available)

print('bool(10): ', bool(10))
print('bool(\'abc\'): ', bool('abc'))
print('bool([]): ', bool([]))
print('bool([1, 2]: ', bool([1, 2]))
print('bool(None): ', bool(None))

print('100 > 10: ', 100 > 10)
print('\'Long string\' > \'Short\': ', 'Long string' > 'Short')
print('[] == [1]:', [] == [1])
print('{\'a\': 3} == {\'a\': 3}: ', {'a': 3} == {'a': 3})