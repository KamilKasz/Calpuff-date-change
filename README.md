# Calpuff-date-change
Current version: 0.1.0

Python script that allows to modify dates of input files of modules of CALMET/CALPUFF model, by using date provided by user. Just run this program using the Python interpreter. At the moment you can only use it to calcluate.

Right now it is not possible to change files from the whole package (CALMET, CALPUFF, PRTMET etc.) at one time, but it could be done by example with the use of shell script. Script example.sh shows how to do it. Im general: you
have to look at the main script what question are asked for a given program and then in every line gave answers to them. Thisc is just a temporary solution, hopefully soon it won't be necessary. 

Explanation how co create shell script:

https://github.com/KamilKasz/Calpuff-date-change/blob/be618364711f1bbc92c6b5b7e975dc8ecd10bd94/example.sh#LL2C1-L21C6

Future plans:
- Improving structure of the code (creating more functions for example)
- Adding the posibility to change multiple files at once
- Create a GUI
