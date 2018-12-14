#!/usr/bin/env python

import re

rx_longword = re.compile(r"\b[a-z]{8,}\b", re.I)


def mark_word(m):
    return '**' + m.group() + '**'


with open('../DATA/parrot.txt') as parrot_in:
    with open('bigwords.txt', 'w') as bigwords_out:
        for line in parrot_in:
            new_line = rx_longword.sub(r"**\g<0>**", line)
            bigwords_out.write(new_line)
