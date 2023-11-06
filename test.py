import requests

headers = {
    'Authorization':
    'JWT eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjk5MjA5MDE3LCJpYXQiOjE2OTkxNzkwMTcsImp0aSI6ImRiZTdmYWEyODIyNTQyODQ5N2I3NTFkZjRhZjY0ZjcxIiwidXNlcl9pZCI6NX0.aSxPfBE9J-n0QaXM7Raf6qmdh7WYhrjP5xtpJYBICGM',
}

files = {
    'photo': open(r'C:\Users\vladg\PycharmProjects\django_social_media\social\media\blog\5I3IXcA6C2E.jpg', 'rb'),
    'email': (None, 'zxc@zxc.com'),
    'first_name': (None, 'string11'),
    'last_name': (None, 'string12'),
    'password': (None, 'Qseawdzxc1'),
}

response = requests.put('http://127.0.0.1:8000/users/me/', headers=headers, files=files)

print(response.json())
print(response.status_code)
