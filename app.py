import sys

try:
  f = open("/mnt/data/myfile.txt", "w")
  f.write("writing" + sys.argv[1])
except FileNotFoundError:
    print('File not found')
