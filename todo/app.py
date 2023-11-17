
from flask import Flask,request,jsonify,g,render_template,redirect,url_for
import json
import sqlite3
import json   


app = Flask(__name__)
app.json.ensure_ascii = False   # 文字化けを防ぐ

dbpath = 'todo.db' #テーブルを保存するファイル

def get_db():#データベースのコネクションを取得
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(dbpath)
        db.execute('CREATE TABLE IF NOT EXISTS todo_tbl(id integer primary key, task VARCHAR(100), dead_line VARCHAR(140),done VARCHAR(10))')
    return db 




# GETに対する処理
@app.route('/', methods=['GET'])
def get_todo():
    con = get_db() 
    con.row_factory = sqlite3.Row 
    cur = con.cursor()
              
    cur.execute('SELECT * FROM todo_tbl')
    lists = []
    for row in cur.fetchall(): 
        lists.append(dict(row))
            
    return render_template("index.html",todo_lists=lists)



# POSTに対する処理
@app.route('/register', methods=['POST'])
def register():
    con = get_db() 
    cur = con.cursor() 
              
    task = request.form["todo"]
    dead_line = request.form["deadline"]
    done = request.form["priority"]
    cur.execute(f"INSERT INTO todo_tbl(task,dead_line,done) values('{task}','{dead_line}','{done}')") #ツイート文をテーブルにINSERT
    con.commit()
    return redirect(url_for('get_todo'))





# # PUTに対する処理
# @app.route('/todo', methods=['PUT'])
# def put_todo():
#     con = get_db() 
#     cur = con.cursor()
              
#     task = request.json["task"]
#     done = request.json["done"]
    
#     cur.execute(f"UPDATE todo_tbl SET done = '{done}' WHERE task = '{task}'")
#     con.commit()

#     return 'updated !\n'



# # DELETEに対する処理            
@app.route('/delete/<int:todo_id>')
def delete(todo_id):
    con = get_db() 
    cur = con.cursor() 

    # task = request.json["task"]
    cur.execute(f"DELETE FROM todo_tbl WHERE id = '{todo_id}'")
    con.commit()
              
    return redirect(url_for('get_todo'))


if __name__ == "__main__":
    app.run()

# , methods=['DELETE']