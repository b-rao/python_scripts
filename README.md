# python_scripts

A bunch of python programs

## about

Tested on debian linux

### checker.py

convenience tool to check if a website has changed.
```
$ ./checker.py -h
usage: checker.py [-h] website

positional arguments:
  website     Website to check

optional arguments:
  -h, --help  show this help message and exit

```

### password.py

```
$ ./password.py -h
usage: password.py [-h] [-u] [-d] [-p] num

positional arguments:
  num                Generate password of num length

optional arguments:
  -h, --help         show this help message and exit
  -u, --uppercase    Include uppercase letters
  -d, --digits       Include decimal digits
  -p, --punctuation  Include punctuation letters
```

### redblue.py

A certain urn contains 2 types of balls, red or blue.

If a red ball is draw, it is discarded.

If a blue ball is drawn, the next ball will be discarded, whichever type.

What is the chance that a red ball being the last one in the urn?

```
$./redblue.py
```

