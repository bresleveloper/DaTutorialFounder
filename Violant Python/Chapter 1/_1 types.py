

def hr(m):
    print('\n---------------' + ('-' * (len(m) - 3)))
    print('---  ', m, '  ---')
    print(('-' * (len(m) - 3)) + '---------------\n')

def p(x):
    print(type(x))


hr('types')

s = 'a'
p(s)

i = 1
p(i)

b = True
p(b)

l = [1,4,'t']
p(l)

hr('string funcs')

print(s.upper())
s = 'AiKjI'
print(s.lower())
s = 'let me let me'
print(s.replace('let', 'its'))
print(s.find('me'))
print(len(s))


hr('list funcs')

l = [90,80,4,666,66]
print(l)
l.sort()
print(l)
l = [90,80,'o9',4,666,66, 'sds']
print(l)
# l.sort() # will cause an error    TypeError: '<' not supported between instances of 'str' and 'int'

print(l.index('o9'))
l.remove(80)
print(l.index('o9'))
print(len(l))



hr('dictionary funcs')

services = {'ftp':21, 'ssh':22, 'smpt':25, 'http':80}
p(services)

print(services)
print(services.keys())
print(services.items())
print(services.__contains__(21))
print(services.__contains__('ftp'))
print(services['ftp'])
print(services.values())