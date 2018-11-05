from pprint import pprint
import re
file = "log.txt" 


important = []
keep_phrases = ["ThreadCount"]

with open(file ,'r') as f:
    f = f.readlines()

for line in f:
    for phrase in keep_phrases:
        if phrase in line:
            important.append(line)
            break


pprint(important)
text = important[len(important)-1]
print(text.split(' ')) 
