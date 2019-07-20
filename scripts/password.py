#! /usr/bin/env python3
import string as st
import random
import argparse

def passwordGen(n= 10):
    letters = st.ascii_lowercase

    letters += st.ascii_uppercase if up else ""
    letters += st.digits if di else ""
    letters += st.punctuation if pu else ""
    
    password = ""
    for i in range(n):
        password += random.choice(letters)
    return password

up = False
di = False
pu = False

parse = argparse.ArgumentParser()
parse.add_argument("num", help="Generate password of num length", type=int)
parse.add_argument("-u","--uppercase", help="Include uppercase letters",action="store_true")
parse.add_argument("-d","--digits", help="Include decimal digits",action="store_true")
parse.add_argument("-p","--punctuation", help="Include punctuation letters",action="store_true")
args = parse.parse_args()

if args.uppercase:
    up = True
if args.digits:
    di = True
if args.punctuation:
    pu = True

print(passwordGen(args.num))
