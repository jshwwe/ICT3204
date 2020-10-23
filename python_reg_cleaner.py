import re
import sys

filepath = "--File path here--"
regexp = "^(.+? .+? .+?) (.*?) (.*?): (.*?)$"
outpath = "output.csv"
headers = "x,y,z\n"

out_file = open(outpath, "w")
out_file.write(headers)

with open(filepath) as f:
    while True:
        try:
            txt = f.readline()
            if txt == "":
                break
            else:
                out = re.findall(regexp, txt)
                output = ""
                for field in out[0]:
                    output += (field + ",")
                output = output[:-1] + "\n"
                out_file.write(output)
                print(output)
        except:
            continue

