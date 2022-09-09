import os
import time
import argparse

from src.Mode import Mode
from src.Enumerator import Enumerator

parser = argparse.ArgumentParser()
parser.add_argument("--mode", "-m", type=str, required=True, choices=[Mode.DIR, Mode.SUB], help="The operating mode")
parser.add_argument("--address", "-a", type=str, required=True, help="IP Address or URL")
parser.add_argument("--list", "-l", required = True, type=str, help="Path to List of Directories/Subdomains")
parser.add_argument("--port", "-p", type=int, default=80, help="Target Port Number")
parser.add_argument("--timeout", "-t", type=int, default=0.01, help="Request timeout in sec")

args = parser.parse_args()

if(os.path.isfile(args.list)):
    list = open(args.list, 'r', encoding="utf8")
else:
    print("--> There is no file with the name " + args.list + " available")
    exit()

if(args.mode == Mode.DIR):
        mode = "Directory Enumeration"
elif(args.mode == Mode.SUB):
        mode = "Subdomain Enumeration"

print("################################################################################")
print("")
print("Enumerus by 5f0")
print("Directory and Subdomain Enumeration")
print("")
print("Selected Mode: " + mode)
print("")
print("################################################################################")

print("")
print("Starting enumeration...")
print("")


e = Enumerator()
start = time.time()

while True:
    entry = list.readline().rstrip('\n')
    if not entry:
        break
    
    url = ""
    if(args.mode == Mode.DIR):
        url = args.address + ":" + str(args.port) + "/" + entry    
    elif(args.mode == Mode.SUB):
        parts = args.address.split("://")
        url = parts[0] + "://" + entry + "." + parts[1] + ":" + str(args.port) 

    result = e.enumerate(url, args.timeout)
    
print("")
print("################################################################################") 

list.close()

end = time.time()

print("Execution Time: " + str(end-start)[0:8] + " sec")
print("")