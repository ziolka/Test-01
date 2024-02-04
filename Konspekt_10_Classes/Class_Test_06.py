class A:
    x = "I am A class"

class B:
    x = "I am B class"
    y = "I exist only in B class"

class C(A, B):
    z = "This exists only in C class"

c = C()
print(c.z)
print(c.y)
print(c.x)