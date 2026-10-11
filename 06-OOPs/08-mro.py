class A:
    label = "I am class A"

class B:
    label = "I am class B"

class C:
    label = "I am class C"

class D(C,B): pass

d = D()
print(d.label)
print(D.__mro__)              