#!/usr/bin/env python
import os
import requests

nnl_url = "https://navalnuclearlab.energy.gov/about-us/"

response = requests.get(nnl_url)

print(response.content) # .decode())

# print(response.json())

pdf_url = "https://navalnuclearlab.energy.gov/ckfinder/userfiles/files/October%202018%20Update%20to%20the%20Kesselring%20Site%20Refueling%20and%20Overhaul%20of%20the%20S8G%20Prototype.pdf"


response = requests.get(pdf_url)

response.content

with open('nnl.pdf', 'wb') as nnl_out:
    nnl_out.write(response.content)


# os.system("nnl.pdf")  # windows
os.system("open nnl.pdf")  # mac
# os.system("adobereader nnl.pdf")  # linux




