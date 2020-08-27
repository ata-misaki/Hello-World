# Flaskからインポートしてflaskを使えるようにする
from flask import Flask, render_template , request ,redirect,session
import sqlite3
from func1 import add
from func2 import edit
from func3 import delete


# appという名前でFlaskあぷりをつくっていくよ
app = Flask(__name__)
# 分割したblueprintを登録する
app.register_blueprint(add.app)
app.register_blueprint(edit.app)
app.register_blueprint(delete.app)



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
        
        # 音楽 
        c.execute("SELECT *  FROM music") 
        music_list = []
        for row in c.fetchall():
            music_list.append({"id":row[0],"category_id":row[1],"catchcopy":row[2],"name":row[3],"image":row[4],"keyword1":row[5],"keyword2":row[6],"keyword3":row[7]})  
 
        c.execute("SELECT *  FROM art") 
        art_list = []
        for row in c.fetchall():
            art_list.append({"id":row[0],"category_id":row[1],"catchcopy":row[2],"name":row[3],"image":row[4],"keyword1":row[5],"keyword2":row[6],"keyword3":row[7]})  

        c.execute("SELECT *  FROM sports") 
        sports_list = []
        for row in c.fetchall():
            sports_list.append({"id":row[0],"category_id":row[1],"catchcopy":row[2],"name":row[3],"image":row[4],"keyword1":row[5],"keyword2":row[6],"keyword3":row[7]})   

        c.execute("SELECT *  FROM play") 
        play_list = []
        for row in c.fetchall():
            play_list.append({"id":row[0],"category_id":row[1],"catchcopy":row[2],"name":row[3],"image":row[4],"keyword1":row[5],"keyword2":row[6],"keyword3":row[7]})  
   
        c.execute("SELECT *  FROM life") 
        life_list = []
        for row in c.fetchall():
            life_list.append({"id":row[0],"category_id":row[1],"catchcopy":row[2],"name":row[3],"image":row[4],"keyword1":row[5],"keyword2":row[6],"keyword3":row[7]})  

        c.execute("SELECT *  FROM food") 
        food_list = []
        for row in c.fetchall():
            food_list.append({"id":row[0],"category_id":row[1],"catchcopy":row[2],"name":row[3],"image":row[4],"keyword1":row[5],"keyword2":row[6],"keyword3":row[7]})  

        c.execute("SELECT *  FROM trip") 
        trip_list = []
        for row in c.fetchall():
            trip_list.append({"id":row[0],"category_id":row[1],"catchcopy":row[2],"name":row[3],"image":row[4],"keyword1":row[5],"keyword2":row[6],"keyword3":row[7]})  

        c.execute("SELECT *  FROM nature") 
        nature_list = []
        for row in c.fetchall():
            nature_list.append({"id":row[0],"category_id":row[1],"catchcopy":row[2],"name":row[3],"image":row[4],"keyword1":row[5],"keyword2":row[6],"keyword3":row[7]})  
    
        c.execute("SELECT *  FROM fashion") 
        fashion_list = []
        for row in c.fetchall():
            fashion_list.append({"id":row[0],"category_id":row[1],"catchcopy":row[2],"name":row[3],"image":row[4],"keyword1":row[5],"keyword2":row[6],"keyword3":row[7]})  
        
        c.execute("SELECT *  FROM ride") 
        ride_list = []
        for row in c.fetchall():
            ride_list.append({"id":row[0],"category_id":row[1],"catchcopy":row[2],"name":row[3],"image":row[4],"keyword1":row[5],"keyword2":row[6],"keyword3":row[7]})  
        

        c.execute("SELECT *  FROM history") 
        history_list = []
        for row in c.fetchall():
            history_list.append({"id":row[0],"category_id":row[1],"catchcopy":row[2],"name":row[3],"image":row[4],"keyword1":row[5],"keyword2":row[6],"keyword3":row[7]})  
            
        c.execute("SELECT *  FROM medical") 
        medical_list = []
        for row in c.fetchall():
            medical_list.append({"id":row[0],"category_id":row[1],"catchcopy":row[2],"name":row[3],"image":row[4],"keyword1":row[5],"keyword2":row[6],"keyword3":row[7]})  
  
        c.close()     
        return render_template("list.html", nature_list=nature_list, music_list=music_list, art_list=art_list, sports_list=sports_list, trip_list=trip_list, fashion_list=fashion_list, food_list=food_list, life_list=life_list, medical_list=medical_list, history_list=history_list, ride_list=ride_list,play_list=play_list)
    else:
        return redirect("/login")




#管理者登録（あとで）
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