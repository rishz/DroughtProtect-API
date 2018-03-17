# Drought Protect API

API written in Django Framework.

# Setup

 In Terminal, enter the following commands
  - `virtualenv venv`
  - `mkvirtualenv -p /usr/bin/python2.7 --no-site-packages venv`
  - `pip install -r requirements.txt `
  - `python2.7 manage.py makemigrations`
  - `python2.7 manage.py migrate`
  - `python 2.7 manage.py runserver`

# API Endpoints

## Register
`POST http://localhost:8000/register/`
### Body: 
```
{
    'email': "<email>"
    'password': "<password>"
}
```
### Response:
```
200
{
    'Status': "Ok"
}
```
```
400
{
    'Error':'User already exists'
}
```
```
400
{
    'Error':'Please provide email/password'
}
```

## Login
`POST http://localhost:8000/login/`
### Body: 
```
{
    'email': "<email>"
    'password': "<password>"
}
```
### Response:
```
200
{
    'token': "..."
}
```
```
400
{
    'Error':'Please provide email/password'
}
```
```
400
{
    'Error':'Invalid credentials'
}
```

## Verify_Token
`GET http://localhost:8000/verify_token/`
### Header: 
```
{
    'Authorization': "token <auth token>"
}
```
### Response:
```
200
{
    'Status': "ok"
}
```
```
401
{
    'detail':'Authentication credentials were not provided.'
}
```

License
----

MIT

