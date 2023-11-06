import requests

headers = {
    'Authorization': 'JWT eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjk5Mjk0MzkzLCJpYXQiOjE2OTkyNjQzOTMsImp0aSI6IjczNjc0MmEwYjIyNDQyOWY4YWRjOWI0ODA1YjM1NTE5IiwidXNlcl9pZCI6NX0.4LBkpiewhpsBfYdcZqQc5V2Tkk9utl26Di4LooIr3C4',
}

files = {
    'title': (None, 'string'),
    'content': (None, 'string'),
    'publisher.id': (None, '5'),
    'image': open('C:\papka\photo\images.jpg', 'rb'),
}

response = requests.post('http://127.0.0.1:8000/core/blog/v1/Publication/', headers=headers, files=files)
print(response.json())
print(response.status_code)
