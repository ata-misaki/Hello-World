# Flaskからインポートしてflaskを使えるようにする
from flask import Flask, render_template , request ,redirect,session
import sqlite3

# appという名前でFlaskあぷりをつくっていくよ
app = Flask(__name__)

app.secret_key = 'sunabaco_yatsusiro'

@app.route("/")
def helloWorld():
    return "こんにちは."

#編集リスト
@app.route("/list")
def testlist():
    if 'manager_id' in session:
        manager_id = session['manager_id']
        conn = sqlite3.connect('team3.db') #team3dbにコネクト
        c = conn.cursor()
        c.execute("SELECT *  FROM nature") 
        nature_list = []
        for row in c.fetchall():
            nature_list.append({"id":row[0],"category_id":row[1],"nature_catchcopy":row[2],"nature_name":row[3],"nature_image":row[4],"nature_keyword1":row[5],"nature_keyword2":row[6],"nature_keyword3":row[7]})  
        c.close()

        # conn = sqlite3.connect('team3.db')
        # c = conn.cursor()
        # c.execute("SELECT *  FROM music") 
        # music_list = []  
        # for row in c.fetchall():      
        #     music_list.append({"id":row[0],"category_id":row[1],"music_catchcopy":row[2],"music_name":row[3],"music_image":row[4],"music_keyword1":row[5],"music_keyword2":row[6],"music_keyword3":row[7]}) 
        return render_template("list.html", nature_list=nature_list) #music_list=music_list

        # c.execute("SELECT *  FROM sport") 
        # sport_list = []  
        # for row in c.fetchall():      
        #     sport_list.append({"id":row[0],"category_id":row[1],"sport_catchcopy":row[2],"sport_name":row[3],"sport_image":row[4],"sport_keyword1":row[5],"sport_keyword2":row[6],"sport_keyword3":row[7]}) 
        # c.close()
    else:
        return redirect("/login")

#追加
@app.route("/add", methods = ["GET"])
def add_get():
    if 'manager_id' in session:
        return render_template("add.html")
    else:
        return redirect("/login")

@app.route("/add", methods = ["POST"])
def add_post():
    if 'manager_id' in session:
        manager_id = session['manager_id']
        catchcopy = request.form.get("catchcopy")
        name = request.form.get("name")
        keyword1 = request.form.get("keyword1")
        keyword2 = request.form.get("keyword2")
        keyword3 = request.form.get("keyword3")
        print()
        conn = sqlite3.connect('team3.db')
        c = conn.cursor()
        c.execute("INSERT into art values(null,?,?,?,?,?,?)",(catchcopy,name,image,keyword1,keyword2,keyword3))
        conn.commit()
        c.close()
        return redirect("/list")
    else:
        return redirect("/login")

#課題の回答からとってきたもの 画像アップどうしたらええんや・・・・
@app.route('/upload', methods=["POST"])
def do_upload():
    # bbs.tplのinputタグ name="upload" をgetしてくる
    upload = request.files['upload']
    # uploadで取得したファイル名をlower()で全部小文字にして、ファイルの最後尾の拡張子が'.png', '.jpg', '.jpeg'ではない場合、returnさせる。
    if not upload.filename.lower().endswith(('.png', '.jpg', '.jpeg')):
        return 'png,jpg,jpeg形式のファイルを選択してください'
    
    # 下の def get_save_path()関数を使用して "./static/img/" パスを戻り値として取得する。
    save_path = get_save_path()
    # パスが取得できているか確認
    print(save_path)
    # ファイルネームをfilename変数に代入
    filename = upload.filename
    # 画像ファイルを./static/imgフォルダに保存。 os.path.join()は、パスとファイル名をつないで返してくれます。
    upload.save(os.path.join(save_path,filename))
    # ファイル名が取れることを確認、あとで使うよ
    print(filename)
    
    # アップロードしたユーザのIDを取得
    # user_id = session['user_id']
    # conn = sqlite3.connect('team3.db')
    c = conn.cursor()
    # update文
    # 上記の filename 変数ここで使うよ
    c.execute("update user set prof_img = ? where id=?", (filename,user_id))
    conn.commit()
    conn.close()

    return redirect ('/add')


@app.route('/edit/<int:id>')
def edit(id):
    if 'manager_id' in session:
        conn = sqlite3.connect('team3.db')
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
    if 'manager_id' in session:
        name = request.form.get("name")
        catchcopy = request.form.get("catchcopy")
        keyword1 = request.form.get("keyword1")
        keyword2 = request.form.get("keyword2")
        keyword3 = request.form.get("keyword3")
  
        conn = sqlite3.connect('team3.db')
        c = conn.cursor()
        c.execute("UPDATE art set name = ? ,category = ? , keyword1 = ?, keyword2 = ?, keyword3 = ?, where id = ?",(name,category,keyword1,keyword2,keyword3))
        conn.commit()
        c.close()
        return redirect("/list")
    else:
        return redirect("/login")

@app.route('/del/<int:id>')
def del_task(id):
    if 'manager_id' in session:
        conn = sqlite3.connect('team3.db')
        c = conn.cursor()
        c.execute("DELETE FROM art WHERE id = ?",(id,))
        c.execute("DELETE FROM music WHERE id = ?",(id,))
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
    maneger = request.form.get("name")
    password = request.form.get("password")
    conn = sqlite3.connect('team3.db')
    c = conn.cursor()
    c.execute("INSERT into user values(null,?,?)",(name,password))
    conn.commit()
    c.close()
    return redirect("/login")

@app.route("/login")
def login_get():
    if 'manager_id' in session:
        return redirect("/list")
    else:
        return render_template("login.html")
    return render_template("login.html")

@app.route("/login",methods=["POST"])
def login_post():
    manager_id = request.form.get("manager_id")
    password = request.form.get("password")
    conn = sqlite3.connect('team3.db')
    c = conn.cursor()
    c.execute("SELECT id FROM manager WHERE manager_id = ? AND password = ?",(manager_id,password))
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
    return "ページないですよ"


if __name__ == "__main__":
    app.run(debug = True)








if __name__ == "__main__":
    # Flaskが持っている開発用サーバーを実行します
    app.run(debug=True)