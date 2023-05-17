#!/usr/bin/env python3
# -*- coding: utf-8 -*

"""This script modifies dates of start and (when applied) end of calculations for input files of elements of
CALMET/CALPUFF system (CALMET, CALPUFF, PRTMET, ). More information in a readme file. Version 0.1 (first release)

"""

# Importing modules

from subprocess import Popen, PIPE
import os
from datetime import datetime
import fileinput
from os import path
import re

# Defining function that allows user to choose whether he wants to replace existing file or to create new


def y_n():
    while True:
        del_of = input("Do you want to delete old file(s)? (Y/N) default: N") or "N"
        if del_of == "y" or del_of == "yes" or del_of == "YES" or del_of == "Y":
            del_of = "Y"
            break
        elif (
                del_of == "n"
                or del_of == "no"
                or del_of == "NO"
                or del_of == "NO"
                or del_of == "N"
        ):
            del_of = "N"
            break
        elif del_of != "N" or del_of != "Y":
            print("Answer with Y or N")
            continue
    return del_of


# defining function that checks if the path exists


def ch_path():
    while True:
        patht = (
                input("path to directory with source files")
                or "/home/kamil/Desktop/calpsot_skrypt/"
        )
        ch_path = path.exists(patht)
        if ch_path:
            break
        else:
            print("Wrong path, try again")
    return patht

# Asking user for the input he wants to be changed

def sig():
 while True:
    sig = (
            input(
                "Do you want to change input of Calmet (write 'CALM'), Calpost (write 'CLO'), Calpuff (write 'CLF'), "
                "PRTMET (write 'PRT'), default 'CLO''"
            )
            or "CLO"
    )
    if (
            sig == "CALM"
            or sig == "calm"
            or sig == "CLO"
            or sig == "clo"
            or sig == "CLF"
            or sig == "clf"
            or sig == "PRT"
            or sig == "prt"
    ):
        break
    else:
        print("Answer not recognized")
 return sig
        
sig=sig()

patht = ch_path()  # path


# Dictionary that assigns values used by specific programs to date variables


calpost = {
    "YEAR": "ISYR",
    "MONTH": "ISMO",
    "DAY": "ISDY",
    "HR": "ISHR",
    "MIN": "ISMIN",
    "SEC": "ISSEC",
    "EYEAR": "IEYR",
    "EMONTH": "IEMO",
    "EDAY": "IEDY",
    "EHR": "IEHR",
    "EMIN": "IEMIN",
    "ESEC": "IESEC",
}

calmet = {
    "YEAR": "IBYR",
    "MONTH": "IBMO",
    "DAY": "IBDY",
    "HR": "IBHR",
}

calpuff = {
    "YEAR": "IBYR",
    "MONTH": "IBMO",
    "DAY": "IBDY",
    "HR": "IBHR",
}

prtmet = {
    "YEAR": "IBYR",
    "MONTH": "IBMO",
    "DAY": "IBDY",
    "HR": "IBHR",
    "EYEAR": "IEYR",
    "EMONTH": "IEMO",
    "EDAY": "IEDY",
    "EHR": "IEHR",
}

# Getting information about dates

def ch_date(sig):
 result = {
        "year_beg": None, "mon_beg": None, "day_beg": None, "hr_beg": None, 
        "min_beg": None, "sec_beg": None, "year_end": None, "mon_end": None, 
        "day_end": None, "hr_end": None, "min_end": None, "sec_end": None, 
        "YEAR": None, "MONTH": None, "DAY": None, "HR": None, "MIN": None, 
        "SEC": None, "EYEAR": None, "EMONTH": None, "EDAY": None, 
        "EHR": None, "EMIN": None, "ESEC": None
    }











 while True:
    try:
        if sig == "CLO":
            print("Please name date of beginning of calculations")
            # DATE=input("patht to directory with source files")
            YEAR = input("Specify year (four numbers)")
            MONTH = input("Specify month (two numbers)")
            DAY = input("Specify day (two numbers)")
            HR = input("Specify hour (default: 00)") or "00"
            MIN = input("Specify minutes (default: 00)") or "00"
            SEC = input("Specify seconds (default: 00") or "00"

            date_time_str = (
                    YEAR + " " + MONTH + " " + DAY + " " + HR + " " + MIN + " " + SEC
            )
            date_time_obj = datetime.strptime(date_time_str, '%Y %m %d %H %M %S')  # created to check if given date
            # is acceptable
            year_beg = calpost.get("YEAR")
            mon_beg = calpost.get("MONTH")
            day_beg = calpost.get("DAY")
            hr_beg = calpost.get("HR")
            min_beg = calpost.get("MIN")
            sec_beg = calpost.get("SEC")
            
            print("Please name date of the end of calculations")
            EYEAR = input("Specify year (four numbers)")
            EMONTH = input("Specify month (two numbers)")
            EDAY = input("Specify day (two numbers)")
            EHR = input("Specify hour (default: 00)") or "00"
            EMIN = input("Specify minutes (default: 00)") or "00"
            ESEC = input("Specify seconds (default: 00") or "00"

            date_time_str = (
                    EYEAR + " " + EMONTH + " " + EDAY + " " + EHR + " " + EMIN + " " + ESEC
            )
            date_time_obj = datetime.strptime(date_time_str, "%Y %m %d %H %M %S")
            year_end = calpost.get("EYEAR")
            mon_end = calpost.get("EMONTH")
            day_end = calpost.get("EDAY")
            hr_end = calpost.get("EHR")
            min_end = calpost.get("EMIN")
            sec_end = calpost.get("ESEC")
            result["year_beg"] = year_beg
            result["mon_beg"] = mon_beg
            result["day_beg"] = day_beg
            result["hr_beg"] = hr_beg
            result["min_beg"] = min_beg
            result["sec_beg"] = sec_beg
            result["year_end"] = year_end
            result["mon_end"] = mon_end
            result["day_end"] = day_end
            result["hr_end"] = hr_end
            result["min_end"] = min_end
            result["sec_end"] = sec_end
            result["YEAR"] = YEAR
            result["MONTH"] = MONTH
            result["DAY"] = DAY
            result["HR"] = HR
            result["MIN"] = MIN
            result["SEC"] = SEC
            result["EYEAR"] = EYEAR
            result["EMONTH"] = EMONTH
            result["EDAY"] = EDAY
            result["EHR"] = EHR
            result["EMIN"] = EMIN
            result["ESEC"] = ESEC


            return result
            
            #continue
        if sig == "CALM":
            print("Please name date of beginning of calculations")
            YEAR = input("Specify year (four numbers)")
            MONTH = input("Specify month (two numbers)")
            DAY = input("Specify day (two numbers)")
            HR = input("Hour (default: 00)") or "00"
            date_time_str = YEAR + " " + MONTH + " " + DAY + " " + HR
            date_time_obj = datetime.strptime(date_time_str, "%Y %m %d %H")
            year_beg = calmet.get("YEAR")
            mon_beg = calmet.get("MONTH")
            day_beg = calmet.get("DAY")
            hr_beg = calmet.get("HR")
            result["year_beg"] = year_beg
            result["mon_beg"] = mon_beg
            result["day_beg"] = day_beg
            result["hr_beg"] = hr_beg
 
            result["YEAR"] = YEAR
            result["MONTH"] = MONTH
            result["DAY"] = DAY
            result["HR"] = HR

            return result
        if sig == "CLF":
            print("Please name date of beginning of calculations")
            YEAR = input("Specify year (four numbers)")
            MONTH = input("Specify month (two numbers)")
            DAY = input("Specify day (two numbers)")
            HR = input("Hour (default: 00)") or "00"
            date_time_str = YEAR + " " + MONTH + " " + DAY + " " + HR
            date_time_obj = datetime.strptime(date_time_str, "%Y %m %d %H")
            year_beg = calpuff.get("YEAR")
            mon_beg = calpuff.get("MONTH")
            day_beg = calpuff.get("DAY")
            hr_beg = calpuff.get("HR")
            result["year_beg"] = year_beg
            result["mon_beg"] = mon_beg
            result["day_beg"] = day_beg
            result["hr_beg"] = hr_beg
            result["min_beg"] = min_beg
            result["sec_beg"] = sec_beg
            result["year_end"] = year_end
            result["mon_end"] = mon_end
            result["day_end"] = day_end
            result["hr_end"] = hr_end
            result["min_end"] = min_end
            result["sec_end"] = sec_end
            result["YEAR"] = YEAR
            result["MONTH"] = MONTH
            result["DAY"] = DAY
            result["HR"] = HR
            result["MIN"] = MIN
            result["SEC"] = SEC
            result["EYEAR"] = EYEAR
            result["EMONTH"] = EMONTH
            result["EDAY"] = EDAY
            result["EHR"] = EHR
            result["EMIN"] = EMIN
            result["ESEC"] = ESEC

        if sig == "PRT":
            print("Please name date of beginning of calculations")
            YEAR = input("Specify year (four numbers)")
            MONTH = input("Specify month (two numbers)")
            DAY = input("Specify day (two numbers)")
            HR = input("Hour (default: 00)") or "00"
            date_time_str = YEAR + " " + MONTH + " " + DAY + " " + HR
            date_time_obj = datetime.strptime(date_time_str, "%Y %m %d %H")
            year_beg = prtmet.get("YEAR")
            mon_beg = prtmet.get("MONTH")
            day_beg = prtmet.get("DAY")
            hr_beg = prtmet.get("HR")
            print("Please name date of the end of calculations")
            EYEAR = input("Specify year (four numbers)")
            EMONTH = input("Specify month (two numbers)")
            EDAY = input("Specify day (two numbers)")
            EHR = input("Specify hour (default: 00)") or "00"

            date_time_str = EYEAR + " " + EMONTH + " " + EDAY + " " + EHR
            date_time_obj = datetime.strptime(date_time_str, "%Y %m %d %H")
            year_end = calpost.get("EYEAR")
            mon_end = calpost.get("EMONTH")
            day_end = calpost.get("EDAY")
            hr_end = calpost.get("EHR")
            result["year_beg"] = year_beg
            result["mon_beg"] = mon_beg
            result["day_beg"] = day_beg
            result["hr_beg"] = hr_beg
            result["min_beg"] = min_beg
            result["sec_beg"] = sec_beg
            result["year_end"] = year_end
            result["mon_end"] = mon_end
            result["day_end"] = day_end
            result["hr_end"] = hr_end
            result["min_end"] = min_end
            result["sec_end"] = sec_end
            result["YEAR"] = YEAR
            result["MONTH"] = MONTH
            result["DAY"] = DAY
            result["HR"] = HR
            result["MIN"] = MIN
            result["SEC"] = SEC
            result["EYEAR"] = EYEAR
            result["EMONTH"] = EMONTH
            result["EDAY"] = EDAY
            result["EHR"] = EHR
            result["EMIN"] = EMIN
            result["ESEC"] = ESEC

    except ValueError:
        print("Wrong date, try again")
        continue
 return result



date_values = ch_date(sig)

year_beg = date_values["year_beg"]
mon_beg = date_values["mon_beg"]
day_beg = date_values["day_beg"]
hr_beg = date_values["hr_beg"]
min_beg = date_values["min_beg"]
sec_beg = date_values["sec_beg"]
year_end = date_values["year_end"]
mon_end = date_values["mon_end"]
day_end = date_values["day_end"]
hr_end = date_values["hr_end"]
min_end = date_values["min_end"]
sec_end = date_values["sec_end"]
YEAR = date_values["YEAR"]
MONTH = date_values["MONTH"]
DAY = date_values["DAY"]
HR = date_values["HR"]
MIN = date_values["MIN"]
SEC = date_values["SEC"]
EYEAR = date_values["EYEAR"]
EMONTH = date_values["EMONTH"]
EDAY = date_values["EDAY"]
EHR = date_values["EHR"]
EMIN = date_values["EMIN"]
ESEC = date_values["ESEC"]





# Function that allows user to decide whether they want to create new input file (while keeping the old) or to replace
# the existing one


def dir_path(sig, del_of):
    if del_of == "N":
        # continue
        if sig == "CLO":
            name_of = (
                    input("Name of the file to modify (default name: calpost.inp)")
                    or "calpost.inp"
            )
            name_nf = (
                    input("Name of the new file (default name: calpost.inp1)")
                    or "calpost.inp1"
            )
        if sig == "CALM":
            name_of = (
                    input("Name of the file to modify (default name: calmet.inp)")
                    or "calmet.inp"
            )
            name_nf = (
                    input("Name of the new file (default name: calmet.inp1)")
                    or "calmet.inp1"
            )
        if sig == "CLF":
            name_of = (
                    input("Name of the file to modify (default name: calpuff.inp)")
                    or "calpuff.inp"
            )
            name_nf = (
                    input("Name of the new file(default name: calpuff.inp1)")
                    or "calpuff.inp1"
            )
        if sig == "PRT":
            name_of = (
                    input("Name of the file to modify (default name: prtmet.inp)")
                    or "prtmet.inp"
            )
            name_nf = (
                    input("Name of the new file(default name: prtmet.inp1)")
                    or "prtmet.inp1"
            )
    else:

        if sig == "CLO":
            name_of = (
                    input("Name of the file to modify (default name: calpost.inp)")
                    or "calpost.inp"
            )

        if sig == "CALM":
            name_of = (
                    input("Name of the file to modify (default name: calmet.inp)")
                    or "calmet.inp"
            )

        if sig == "CLF":
            name_of = (
                    input("Name of the file to modify (default name: calpuff.inp)")
                    or "calpuff.inp"
            )

        if sig == "PRT":
            name_of = (
                    input("Name of the file to modify (default name: prtmet.inp)")
                    or "prtmet.inp"
            )

        name_nf = name_of
    return name_of, name_nf


del_of = y_n()  # deleting files

dir_path = dir_path(sig, del_of)
name_of = dir_path[0]
name_nf = dir_path[1]

# Opening base input file

with open(patht + name_of, "r") as file:
    contents = file.read()

# Finding dates and replacing them


year_match = re.search(year_beg + r"\s*=\s*(\d+)", contents)
if year_match:
    old_year = int(year_match.group(1))
    contents = re.sub(year_beg + r"\s*=\s*\d+", f"{year_beg} = {YEAR}", contents)

month_match = re.search(mon_beg + r"\s*=\s*(\d+)", contents)
if month_match:
    old_month = int(month_match.group(1))
    contents = re.sub(mon_beg + r"\s*=\s*\d+", f"{mon_beg} = {MONTH}", contents)

day_match = re.search(day_beg + r"\s*=\s*(\d+)", contents)
if day_match:
    old_day = int(month_match.group(1))
    contents = re.sub(day_beg + r"\s*=\s*\d+", f"{day_beg} = {DAY}", contents)

hr_match = re.search(hr_beg + r"\s*=\s*(\d+)", contents)
if hr_match:
    old_hr = int(month_match.group(1))
    contents = re.sub(hr_beg + r"\s*=\s*\d+", f"{hr_beg} = {HR}", contents)
    
if MIN is not None:
    try:
        min_match = re.search(min_beg + r"\s*=\s*(\d+)", contents)

        if min_match:
           # old_sec = int(sec_match.group(1))
            old_min = int(min_match.group(1))
            contents = re.sub(min_beg + r"\s*=\s*\d+", f"{min_beg} = {MIN}", contents)
    except NameError:
     pass

if SEC is not None:
    try:
        sec_match = re.search(sec_beg + r"\s*=\s*(\d+)", contents)

        if sec_match:
            old_sec = int(sec_match.group(1))
            contents = re.sub(sec_beg + r"\s*=\s*\d+", f"{sec_beg} = {SEC}", contents)
    except NameError:
     pass
print(year_beg)



if EYEAR is not None:
    try:
        yeare_match = re.search(year_end + r"\s*=\s*(\d+)", contents)

        if yeare_match:
            old_year = int(yeare_match.group(1))
            contents = re.sub(year_end + r"\s*=\s*\d+", f"{year_end} = {EYEAR}", contents)
    except NameError:
     pass


if EMONTH is not None:
    try:
        monthe_match = re.search(mon_end + r"\s*=\s*(\d+)", contents)

        if monthe_match:
            old_month = int(monthe_match.group(1))
            contents = re.sub(mon_end + r"\s*=\s*\d+", f"{mon_end} = {EMONTH}", contents)
    except NameError:
     pass


if EDAY is not None:
    try:
        daye_match = re.search(day_end + r"\s*=\s*(\d+)", contents)

        if daye_match:
            old_day = int(daye_match.group(1))
            contents = re.sub(day_end + r"\s*=\s*\d+", f"{day_end} = {EDAY}", contents)
    except NameError:
     pass



if EHR is not None:
    try:
        hre_match = re.search(hr_end + r"\s*=\s*(\d+)", contents)

        if hre_match:
            old_hour = int(hre_match.group(1))
            contents = re.sub(hr_end + r"\s*=\s*\d+", f"{hr_end} = {EHR}", contents)
    except NameError:
     pass




if EMIN is not None:
    try:
        mine_match = re.search(min_end + r"\s*=\s*(\d+)", contents)

        if mine_match:
            old_min = int(mine_match.group(1))
            contents = re.sub(min_end + r"\s*=\s*\d+", f"{min_end} = {EMIN}", contents)
    except NameError:
     pass



if ESEC is not None:
    try:
        sece_match = re.search(sec_end + r"\s*=\s*(\d+)", contents)

        if sece_match:
            old_sec = int(sece_match.group(1))
            contents = re.sub(sec_end + r"\s*=\s*\d+", f"{sec_end} = {ESEC}", contents)
    except NameError:
     pass




#Saving file with changed date


with open(patht + name_nf, "w") as file:
    file.write(contents)
