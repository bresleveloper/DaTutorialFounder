a = 7829

def corn():
    b = 15
    print(a)


def fudge():
    #print(b) # error
    print(a)


corn()
fudge()
corn()

def dummy(name='ari', action='num num', item='meat'):
    print(name, action, item)

dummy()
dummy('sara', 'play', 'buba')
dummy('ayala', 'play')
dummy('nanach')

dummy(item='breakfast')
dummy(item='breakfast', name='naomi', action='prepared')

