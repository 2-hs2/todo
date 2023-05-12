from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

from pymongo import MongoClient
import certifi

client = MongoClient('mongodb+srv://sparta:test@cluster0.wfmkath.mongodb.net/?retryWrites=true&w=majority', tlsCAFile=certifi.where())
db = client.dbsparta

@app.route('/')
def home():
    return render_template('index.html')

@app.route("/icon", methods=["POST"])
def icon_post():
    src_receive = request.form['src_give']
    day_receive = request.form['day_give']
    month_receive = request.form['month_give']
    year_receive = request.form['year_give']
    doc = {
        'src': src_receive,
        'day': day_receive,
        'month': month_receive,
        'year': year_receive
    }
    db.icon.insert_one(doc)
    return jsonify({'msg': '저장 완료!'})
    
@app.route("/icon", methods=["GET"])
def icon_get():
    all_icons = list(db.icon.find({},{'_id':False}))
    return jsonify({'result': all_icons})

@app.route("/todo", methods=["POST"])
def todo_post():
  todolist_receive = request.form['todolist_give']
  day_receive = request.form['day_give']
  month_receive = request.form['month_give']
  year_receive = request.form['year_give']
  doc = {
      'todo':todolist_receive,
      'day': day_receive,
      'month': month_receive,
      'year': year_receive
      }
  db.todo.insert_one(doc)
  return jsonify({'msg': '저장 연결 완료!'})

@app.route("/todo", methods=["GET"])
def todo_get():
  all_todo = list(db.todo.find({},{'_id':False}))
  return jsonify({'result': all_todo})

@app.route("/todo-delete", methods=["POST"])
def todo_delete():
  todolist_receive = request.form['todolist_give']
  day_receive = request.form['day_give']
  month_receive = request.form['month_give']
  year_receive = request.form['year_give']
  print(todolist_receive, day_receive, month_receive, year_receive)
  doc = {
    'todo':todolist_receive,
    'day': day_receive,
    'month': month_receive,
    'year': year_receive
  }
  db.todo.delete_one(doc)
  return jsonify({'msg': '삭제 완료!'})

if __name__ == '__main__':
    app.run('0.0.0.0', port=5001, debug=True)