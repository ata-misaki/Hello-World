# Flaskからインポートしてflaskを使えるようにする
from flask import Flask, render_template , request ,redirect,session
import sqlite3

# appという名前でFlaskあぷりをつくっていくよ
app = Flask(__name__)

app.secret_key = 'sunabaco_yatsusiro'

@app.route("/")
def helloWorld():
    return "Hello World."


@app.route("/list")
def tasklist():
    if 'user_id' in session:
        user_id = session['user_id']
        conn = sqlite3.connect('task_list.db')
        c = conn.cursor()
        c.execute("SELECT name FROM user WHERE id = ?",(user_id,))
        user_name = c.fetchone()[0]
        c.execute("SELECT *  FROM task WHERE user_id = ?",(user_id,))
        task_list = []
        for row in c.fetchall():
            task_list.append({"id":row[0],"task":row[1],"limit_task":row[2]})
            print(task_list)
        c.close()
        return render_template("task_list.html", task_list = task_list,user_name = user_name)
    else:
        return redirect("/login")

@app.route("/add", methods = ["GET"])
def add_get():
    if 'user_id' in session:
        return render_template("add.html")
    else:
        return redirect("/login")

@app.route("/add", methods = ["POST"])
def add_post():
    if 'user_id' in session:
        user_id = session['user_id']
        task = request.form.get("task")
        limit_task = request.form.get("limit_task")
        print(task)
        conn = sqlite3.connect('task_list.db')
        c = conn.cursor()
        c.execute("INSERT into task values(null,?,?,?)",(task,limit_task,user_id))
        conn.commit()
        c.close()
        return redirect("/list")
    else:
        return redirect("/login")

@app.route('/edit/<int:id>')
def edit(id):
    if 'user_id' in session:
        conn = sqlite3.connect('task_list.db')
        c = conn.cursor()
        c.execute("SELECT task ,limit_task FROM task WHERE id = ?",(id,))
        task = c.fetchone()
        conn.close()
        if task is not None:
            task_name = task[0]
            limit_task = task[1]
        else:
            return "アイテムがありません"
        
        item = {"id":id,"task":task_name,"limit_task":limit_task}
        return render_template("edit.html",task = item)
    else:
        return redirect("/login")

@app.route("/edit",methods=["POST"])
def update_task():
    if 'user_id' in session:
        limit_task = request.form.get("limit_task")
        task = request.form.get("task")
        task_id = request.form.get("task_id")
        print(task)
        conn = sqlite3.connect('task_list.db')
        c = conn.cursor()
        c.execute("UPDATE task set task = ? ,limit_task = ? where id = ?",(task,limit_task,task_id))
        conn.commit()
        c.close()
        return redirect("/list")
    else:
        return redirect("/login")

@app.route('/del/<int:id>')
def del_task(id):
    if 'user_id' in session:
        conn = sqlite3.connect('task_list.db')
        c = conn.cursor()
        c.execute("DELETE  FROM task WHERE id = ?",(id,))
        conn.commit()
        conn.close()
        return redirect("/list")
    else:
        return redirect("/login")

    # fetchone:sqlを描いた時点では操作は完了していない.fetchoneで情報を1つだけ取る.全部ならfetchall
    # commit:変更を確定.DBへの操作を確定する

@app.route('/regist')
def regist_get():
    return render_template("regist.html")


@app.route("/regist", methods = ["POST"])
def regist_post():
    name = request.form.get("name")
    password = request.form.get("password")
    conn = sqlite3.connect('task_list.db')
    c = conn.cursor()
    c.execute("INSERT into user values(null,?,?)",(name,password))
    conn.commit()
    c.close()
    return redirect("/login")

@app.route("/login")
def login_get():
    if 'user_id' in session:
        return redirect("/list")
    else:
        return render_template("login.html")
    return render_template("login.html")

@app.route("/login",methods=["POST"])
def login_post():
    name = request.form.get("name")
    password = request.form.get("password")
    conn = sqlite3.connect('task_list.db')
    c = conn.cursor()
    c.execute("SELECT id FROM user WHERE name = ? AND password = ?",(name,password))
    user_id = c.fetchone()
    print(user_id)
    c.close()
    if user_id is None:
        return render_template("login.html")
    else:
        session['user_id'] = user_id[0]
    return redirect("/list")

@app.route("/logout")
def logout():
    session.pop('user_id',None)
    return redirect("login")

@app.errorhandler(404)
def not_found(code):
    return "ページないですよ"


if __name__ == "__main__":
    app.run(debug = True)








if __name__ == "__main__":
    # Flaskが持っている開発用サーバーを実行します
    app.run(debug=True)