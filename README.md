# Calpuff-date-change
Current version: 0.1.0

Python script that allows to modify dates of input files of modules of CALMET/CALPUFF model, by using date provided by user. Just run this program using the Python interpreter. At the moment you can only use it to calcluate.

Right now it is not possible to change files from the whole package (CALMET, CALPUFF, PRTMET etc.) at one time, but it could be done by example with the use of shell script. Script example.sh shows how to do it. Im general: you
have to look at the main script what question are asked for a given program and then in every line gave answers to them. Thisc is just a temporary solution, hopefully soon it won't be necessary. 

Explanation how to create shell script:

``` shell
python3 calpost_r16.py<<INPUT
CLO

2006
10
13



2009
11
13



N


INPUT  #changing date in calpost.inp

```

So in this case we want to change input of CALMET file

Future plans:
- Improving structure of the code (creating more functions for example)
- Adding the posibility to change multiple files at once
- Create a GUI
