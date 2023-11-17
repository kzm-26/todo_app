# curlコマンド例
```sh
POST:   curl http://127.0.0.1:5000/todo -XPOST -H "Content-Type: application/json" -d '{"task":"work","dead_line":"9/12","done":"False"}'
GET:    curl http://127.0.0.1:5000/todo -XGET
PUT:    curl http://127.0.0.1:5000/todo -XPUT -H "Content-Type: application/json" -d ' {"task":"work","done":"True"}'
DELETE: curl http://127.0.0.1:5000/todo -XDELETE -H "Content-Type: application/json" -d ' {"task":"work"}'
```

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

# 参考URL
●api　　　  
  https://hogetech.info/network/restapi  
●.dbの中身確認 　　  
  https://qiita.com/baraobara/items/027a4bcbad1c4c68798d  
●python環境  
  https://qiita.com/t-fuku/items/83c721ed7107ffe5d8ff  
●DB作成  
  https://qiita.com/sasao-genmaicha/items/57e2c6758e1aa8df7ae0  
●sqlalchemy CRUD処理  
  https://zenn.dev/shimakaze_soft/articles/6e5e47851459f5  
●queryの使い方  
  https://zenn.dev/suyaa/articles/30d23448d4d472  


# 参考サイト todo
https://su-gi-rx.com/archives/6333

# フォーム取得
https://note.com/studynote/n/n4d962bb013eb

# todo flask app github
https://github.com/patrickloeber/flask-todo

# 2window
command + shift + n