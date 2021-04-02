import requests
import json
from colorama import Fore
import sys

url = sys.argv[1]
req = requests.get(url)
headers = req.headers
rem = json.load(open("remediation.json"))

check = ["Referrer-Policy","Content-Security-Policy", "X-Xss-Protection","X-Frame-Options","Strict-Transport-Security",
        "X-Content-Type-Options","Permissions-Policy"]


def check_headers():
    for i in check:
        if i not in headers:
            print()
            print("%s is not set" % i)

            if i in rem:
                output = rem[i]
                print(Fore.LIGHTCYAN_EX + "Remediation:" + Fore.RESET)
                
                for item in output:
                    print("%s" % Fore.GREEN+ item + Fore.RESET)
                

check_headers()

'''for typ,data, in headers.items():
    print("%s : %s" % (typ,data))'''