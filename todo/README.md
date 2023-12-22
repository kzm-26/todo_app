# requests
```sh
# GET  
response=requests.get(url, params=None)  
print(response.status_code)  
print(response.text)  

# POST    
response = requests.post(url, json=post_data)  
print(response.status_code)  
print(response.json())  

# PUT
response = requests.put(url, json=put_data)
print(response.status_code)
print(response.json())

# DELETE
response = requests.delete(url, json=delete_data)
print(response.status_code)
print(response.json())
```


# flask実行方法
```
export FLASK_APP=<Pythonファイル>
export FLASK_ENV=development
flask run
```

# DB作成
```
python
>>> from app import app
>>> from app import db
>>> with app.app_context():
>>>     db.create_all()
>>> exit()
```
