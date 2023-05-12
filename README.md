# Calpuff-date-change
Current version: 0.2.0

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
calpost.inp
calpost.inp1
INPUT  #changing date in calpost.inp

```

So in this case we want to change input of CALPUFF file (so the answer to question: "Do you want to change input of Calmet (write 'CALM'), Calpost (write 'CLO'), Calpuff (write 'CLF'), "                 "PRTMET (write 'PRT'), default 'CLO''" is CLO, although it could be left empty), next is the question about path to base file, we are keeping current path so we skip it, then we are giving answers about starting date. Next three skips are about hours, minutes and seconds, because we are keeping them at default value 00. The same procedure works for ending date and as we don't want to delete old files, we are answering "no". "calpost.inp" is the name of the file we are modyfing, "calpost.inp1" is the name of the file we are creating. 

Current script works well with the version of CALMET/CALPUFF approved for US-EPA, there could be some inosistences with newer versions (for example input of CALMET were changed a little), but it generally should work

Future plans:
- Improving the structure of the code 
- Adding the posibility to change multiple files at once
- Making the script working correctly for all versions of Calmet/Calpuff 
- Create a GUI
