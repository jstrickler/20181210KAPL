#!/usr/bin/env python

words = ["mm", "gg"]

pattern = rf"\b({'|'.join(words)})\b"

print(pattern)
