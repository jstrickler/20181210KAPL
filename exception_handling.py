#!/usr/bin/env python
import math

x = 23.9

values = [5.3, 9.1, 4.8, 0.0, 3.7, "ABC", 2.2, 8.5]

results = []

for v in values:
    try:
        result = x / v
    except ZeroDivisionError as err:
        print(err)
    except (TypeError, ValueError) as err:
        print(err)
    else:
        results.append(result)
        print("DING!")
    finally:
        print("*")

print(results)
