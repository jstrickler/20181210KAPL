#!/usr/bin/env python

x = "100"

i1 = 100
i2 = 0b100
i3 = 0x100
i4 = 0o100
i5 = 23958023985209385209385209385209385209385029385029385029385029385029385029835029835029385029385029385029835029385029385029835029835092830598

print(i1, i2, i3, i4)

f1 = 123.456
f2 = 123.
f3 = .456
f4 = 1.456e22

c1 = 25j
print(c1)
print(c1.conjugate(), c1.real)

print(help(c1.conjugate))



x = 23
y = 7

print(x + y)
print(x - y)
print(x * y)
print(x / y)
print(x // y)  # floored division
print(x ** y)  # power
print(x % y)   # modulus (remainder)

x += 1     # x = x + 1
x *= 100
x /= 12
x -= 25   # x = x - 25
print(x)

#  x++ ++x  x-- --x

#  P E M D A S

result = (x + y) * (x - y)
result = x + (y * x - y)

#  == !=

a = "1234"

print(a * 10)

print(int(a) * 10)

a = "    1234     "
i = int(a)
print(i * 1000)

a = "1.23e55"
print(float(a) * 10)

# print(int(a))

a = "1234"
print(float(a))


d = "DeadBeef"

print(int(d, 16))

flags = "10111110"
print(int(flags, 2))


# int() float() complex()

# bool()   str()   repr()



x = "wombat"

print(str(x), repr(x))




















