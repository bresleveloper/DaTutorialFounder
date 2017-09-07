def add(*args):
    total=0
    for x in args:
        total+=x
    print(total)


add(1,5,8,7,5,6,9,9)

def DoPrecentzOnNumz(*precentz, **numz):
    def percentage(percent, whole):
        return (percent * whole) / 100.0

    total=0
    for x in numz:
        print('numz valz', x)
        total += numz[x]
    for p in precentz:
        total = percentage(p, total)
    print(total)

DoPrecentzOnNumz(6,6,89,8,4,5,5,1,2,2,2,6,6,9,9,8, arp=60, berp=80)


def test_var_args(f_arg, *argv):
    print("first normal arg:", f_arg)
    for arg in argv:
        print("another arg through *argv :", arg)

test_var_args('yasoob','python','eggs','test')


def greet_me(**kwargs):
    if kwargs is not None:
        for key, value in kwargs.items():
            print("%s == %s" % (key, value))

greet_me(name="yasoob", loop='for')

