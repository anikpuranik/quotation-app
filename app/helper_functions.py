#!/usr/bin/env python3

# Importing modules
import json

def read_quotations_from_file(path):
    with open(path, "r") as file:
        quotations = json.load(file)
    return quotations
