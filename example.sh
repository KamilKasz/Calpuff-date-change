#!/bin/bash

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


python3 calpost_r16.py<<INPUT
CALM

2020
01
02

N
calmet_l2
calmet.inp


INPUT  #changing date in calmet.inp

