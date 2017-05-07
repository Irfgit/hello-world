#!/bin/python3

rivers={
    'Nile':'Egypt',
    'redsea':'saudi',
    'erie':'usa',
    }

for k,v in sorted(rivers.items()):
    print("The ",k.title(),"runs through ",v.title())
