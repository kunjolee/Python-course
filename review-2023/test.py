def test1(**kwargs):
    print(kwargs)

    print(kwargs['name1']) 

test1(name1="only name arguments", name2="i seeee")


def test2(**kwargs):
    print(kwargs)

test2(**{'a':'a', 'b':1})


def test3(hola,names):
    print(hola,names)

test3(**{"namess":""})


