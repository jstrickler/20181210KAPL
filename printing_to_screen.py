#!/usr/bin/env python

actor = 'Brad Pitt'
city = "Hollywood"
salary = 15.23903

print(actor, city, salary)
print("What a guy!")

print(actor, end=' ')
print(city, end=' ' )
print(salary)

print(actor, city, salary, sep='; ')

print("{} lives in {} and makes {:.2f} per picture".format(actor, city, salary))

print(actor, city, salary, sep="/", end="....\n")

print(f"{actor} lives in {city} and makes {salary:.2f} per picture")

print(actor, "lives in", city, "and makes", round(salary, 2), "per picture")

print("%s lives in %s and makes %.2f per picture" % (actor, city, salary))
