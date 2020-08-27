# Flaskからインポートしてflaskを使えるようにする
from flask import Flask, render_template , request ,redirect,session
import sqlite3
from func1 import add
from func2 import edit
from func3 import delete
from func4 import all_list
from func5 import regist


# appという名前でFlaskあぷりをつくっていくよ
app = Flask(__name__)
# 分割したblueprintを登録する
app.register_blueprint(add.app)
app.register_blueprint(edit.app)
app.register_blueprint(delete.app)
app.register_blueprint(all_list.app)
app.register_blueprint(regist.app)




app.secret_key = 'sunabaco_yatsusiro'


# インデックスページ


@app.route("/index")
def indexpage():
    return render_template("index.html")



# login
@app.route("/login")
def login_get():
    if 'manager_id' in session:
        return redirect("/list")
    else:
        return render_template("login.html")
    return render_template("login.html")

@app.route("/login",methods=["POST"])
def login_list():
    manager_id = request.form.get("manager_id")
    password = request.form.get("password")
    conn = sqlite3.connect('team3.db')
    c = conn.cursor()
    c.execute("SELECT * FROM manager WHERE manager_id = ? AND password = ?",(manager_id,password))
    manager_id = c.fetchone()
    print(manager_id)
    c.close()
    if manager_id is None:
        return render_template("login.html")
    else:
        session['manager_id'] = manager_id[0]
    return redirect("/list")

@app.route("/logout")
def logout():
    session.pop('manager_id',None)
    return redirect("login")

@app.errorhandler(404)
def not_found(code):
    return "ページがないですよ"


if __name__ == "__main__":
    # Flaskが持っている開発用サーバーを実行します
    app.run(debug=True)