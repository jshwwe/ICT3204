import re
import sys

# filepath = sys.argv[1]
# regexp = sys.argv[2]
# output = sys.argv[3]

filepath = "syslogv5"
regexp = "^(.+? .+? .+?) (.*?) (.*?): (.*?)$"
outpath = "output.csv"

out_file = open(outpath, "w")

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

