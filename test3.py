import jwt

print(jwt.decode(
    'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjk5MzIwNzQ3LCJpYXQiOjE2OTkyOTA3NDcsImp0aSI6IjI4YzRlZjkwZjI5MzQzMzY5YzNkZmZhMDgxMDk4YWM1IiwidXNlcl9pZCI6NX0.orw9nUUtXZRMwzONy9qkI1hnuOojPvGhQoIlDRC-1lQ',
    algorithms=['HS256'],
    key='django-insecure-v%u1^i@^%0x(r&3e5o06&elul68jtihaverkw2$ucuoa7_dh-n'))