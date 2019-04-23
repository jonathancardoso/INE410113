#!/usr/bin/python
import re

def transform (str):
    str = re.sub(r'\?', "[\D]?", str)
    str = re.sub(r'\*', "[\D]*", str)
    return str;
    
def verify (pattern, string):
    matchObj = re.search( r'{}'.format(pattern), string)
    if matchObj:
        if matchObj.group() is string:
            return "Yes";
        else:
            return "No";
    else:
        return "No";
        
n = int(raw_input())#input number
for i in range(0,n):
    pattern = raw_input()#Put the pattern
    string = raw_input()#Put the string
    pattern = transform(pattern) 
    answear = verify (pattern, string)
    print answear
