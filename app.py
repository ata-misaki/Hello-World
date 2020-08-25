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
        
        # 自然
        c.execute("SELECT *  FROM nature") 
        nature_list = []
        for row in c.fetchall():
            nature_list.append({"id":row[0],"category_id":row[1],"catchcopy":row[2],"name":row[3],"image":row[4],"keyword1":row[5],"keyword2":row[6],"keyword3":row[7]})  
        # 音楽 
        c.execute("SELECT *  FROM music") 
        music_list = []
        for row in c.fetchall():
            music_list.append({"id":row[0],"category_id":row[1],"catchcopy":row[2],"name":row[3],"image":row[4],"keyword1":row[5],"keyword2":row[6],"keyword3":row[7]})  
 
        c.execute("SELECT *  FROM art") 
        art_list = []
        for row in c.fetchall():
            art_list.append({"id":row[0],"category_id":row[1],"catchcopy":row[2],"name":row[3],"image":row[4],"keyword1":row[5],"keyword2":row[6],"keyword3":row[7]})  
  
        c.execute("SELECT *  FROM sport") 
        sport_list = []
        for row in c.fetchall():
            sport_list.append({"id":row[0],"category_id":row[1],"catchcopy":row[2],"name":row[3],"image":row[4],"keyword1":row[5],"keyword2":row[6],"keyword3":row[7]})   

        c.execute("SELECT *  FROM trip") 
        trip_list = []
        for row in c.fetchall():
            trip_list.append({"id":row[0],"category_id":row[1],"catchcopy":row[2],"name":row[3],"image":row[4],"keyword1":row[5],"keyword2":row[6],"keyword3":row[7]})  

        c.execute("SELECT *  FROM fashion") 
        fashion_list = []
        for row in c.fetchall():
            fashion_list.append({"id":row[0],"category_id":row[1],"catchcopy":row[2],"name":row[3],"image":row[4],"keyword1":row[5],"keyword2":row[6],"keyword3":row[7]})  

        c.execute("SELECT *  FROM foods") 
        foods_list = []
        for row in c.fetchall():
            foods_list.append({"id":row[0],"category_id":row[1],"catchcopy":row[2],"name":row[3],"image":row[4],"keyword1":row[5],"keyword2":row[6],"keyword3":row[7]})  

        c.execute("SELECT *  FROM life") 
        life_list = []
        for row in c.fetchall():
            life_list.append({"id":row[0],"category_id":row[1],"catchcopy":row[2],"name":row[3],"image":row[4],"keyword1":row[5],"keyword2":row[6],"keyword3":row[7]})  
        
        c.execute("SELECT *  FROM medical") 
        medical_list = []
        for row in c.fetchall():
            medical_list.append({"id":row[0],"category_id":row[1],"catchcopy":row[2],"name":row[3],"image":row[4],"keyword1":row[5],"keyword2":row[6],"keyword3":row[7]})  

        c.execute("SELECT *  FROM history") 
        history_list = []
        for row in c.fetchall():
            history_list.append({"id":row[0],"category_id":row[1],"catchcopy":row[2],"name":row[3],"image":row[4],"keyword1":row[5],"keyword2":row[6],"keyword3":row[7]})  
            
        c.execute("SELECT *  FROM ride") 
        ride_list = []
        for row in c.fetchall():
            ride_list.append({"id":row[0],"category_id":row[1],"catchcopy":row[2],"name":row[3],"image":row[4],"keyword1":row[5],"keyword2":row[6],"keyword3":row[7]})  
        c.close()     
        return render_template("list.html", nature_list=nature_list, music_list=music_list, art_list=art_list, sport_list=sport_list, trip_list=trip_list, fashion_list=fashion_list, foods_list=foods_list, life_list=life_list, medical_list=medical_list, history_list=history_list, ride_list=ride_list)
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
        image = request.form.get("image")
        keyword1 = request.form.get("keyword1")
        keyword2 = request.form.get("keyword2")
        keyword3 = request.form.get("keyword3")
        print()
        conn = sqlite3.connect('team3.db')
        c = conn.cursor()
        c.execute("INSERT into art values(null,null,?,?,?,?,?,?)",(catchcopy,name,image,keyword1,keyword2,keyword3))
        conn.commit()
        c.close()
        return redirect("/list")
    else:
        return redirect("/login")


        
#nature追加
@app.route("/add/nature", methods = ["GET"])
def add_nature_get():
    if 'manager_id' in session:
        return render_template("add_nature.html")
    else:
        return redirect("/login")

@app.route("/add/nature", methods = ["POST"])
def add_nature_post():
    if 'manager_id' in session:
        manager_id = session['manager_id']
        catchcopy = request.form.get("catchcopy")
        name = request.form.get("name")
        image = request.form.get("image")
        keyword1 = request.form.get("keyword1")
        keyword2 = request.form.get("keyword2")
        keyword3 = request.form.get("keyword3")
        print()
        conn = sqlite3.connect('team3.db')
        c = conn.cursor()
        c.execute("INSERT into nature values(null,null,?,?,?,?,?,?)",(catchcopy,name,image,keyword1,keyword2,keyword3))
        conn.commit()
        c.close()
        return redirect("/list")
    else:
        return redirect("/login")


# art_追加
@app.route("/add/art", methods = ["GET"])
def add_art_get():
    if 'manager_id' in session:
        return render_template("add_art.html")
    else:
        return redirect("/login")
@app.route("/add/art", methods = ["POST"])
def add_art_post():
    if 'manager_id' in session:
        manager_id = session['manager_id']
        catchcopy = request.form.get("catchcopy")
        name = request.form.get("name")
        image = request.form.get("image")
        keyword1 = request.form.get("keyword1")
        keyword2 = request.form.get("keyword2")
        keyword3 = request.form.get("keyword3")
        print()
        conn = sqlite3.connect('team3.db')
        c = conn.cursor()
        c.execute("INSERT into art values(null,null,?,?,?,?,?,?)",(catchcopy,name,image,keyword1,keyword2,keyword3))
        conn.commit()
        c.close()
        return redirect("/list")
    else:
        return redirect("/login")




#music追加
@app.route("/add/music", methods = ["GET"])
def add_music_get():
    if 'manager_id' in session:
        return render_template("add_music.html")
    else:
        return redirect("/login")

@app.route("/add/music", methods = ["POST"])
def add_music_post():
    if 'manager_id' in session:
        manager_id = session['manager_id']
        catchcopy = request.form.get("catchcopy")
        name = request.form.get("name")
        image = request.form.get("image")
        keyword1 = request.form.get("keyword1")
        keyword2 = request.form.get("keyword2")
        keyword3 = request.form.get("keyword3")
        print()
        conn = sqlite3.connect('team3.db')
        c = conn.cursor()
        c.execute("INSERT into music values(null,null,?,?,?,?,?,?)",(catchcopy,name,image,keyword1,keyword2,keyword3))
        conn.commit()
        c.close()
        return redirect("/list")
    else:
        return redirect("/login")


#sport追加
@app.route("/add/sport", methods = ["GET"])
def add_sport_get():
    if 'manager_id' in session:
        return render_template("add_sport.html")
    else:
        return redirect("/login")

@app.route("/add/sport", methods = ["POST"])
def add_sport_post():
    if 'manager_id' in session:
        manager_id = session['manager_id']
        catchcopy = request.form.get("catchcopy")
        name = request.form.get("name")
        image = request.form.get("image")
        keyword1 = request.form.get("keyword1")
        keyword2 = request.form.get("keyword2")
        keyword3 = request.form.get("keyword3")
        print()
        conn = sqlite3.connect('team3.db')
        c = conn.cursor()
        c.execute("INSERT into sport values(null,null,?,?,?,?,?,?)",(catchcopy,name,image,keyword1,keyword2,keyword3))
        conn.commit()
        c.close()
        return redirect("/list")
    else:
        return redirect("/login")

#trip追加
@app.route("/add/trip", methods = ["GET"])
def add_trip_get():
    if 'manager_id' in session:
        return render_template("add_trip.html")
    else:
        return redirect("/login")

@app.route("/add/trip", methods = ["POST"])
def add_trip_post():
    if 'manager_id' in session:
        manager_id = session['manager_id']
        catchcopy = request.form.get("catchcopy")
        name = request.form.get("name")
        image = request.form.get("image")
        keyword1 = request.form.get("keyword1")
        keyword2 = request.form.get("keyword2")
        keyword3 = request.form.get("keyword3")
        print()
        conn = sqlite3.connect('team3.db')
        c = conn.cursor()
        c.execute("INSERT into trip values(null,null,?,?,?,?,?,?)",(catchcopy,name,image,keyword1,keyword2,keyword3))
        conn.commit()
        c.close()
        return redirect("/list")
    else:
        return redirect("/login")


#fashion追加
@app.route("/add/fashion", methods = ["GET"])
def add_fashion_get():
    if 'manager_id' in session:
        return render_template("add_fashion.html")
    else:
        return redirect("/login")

@app.route("/add/fashion", methods = ["POST"])
def add_fashion_post():
    if 'manager_id' in session:
        manager_id = session['manager_id']
        catchcopy = request.form.get("catchcopy")
        name = request.form.get("name")
        image = request.form.get("image")
        keyword1 = request.form.get("keyword1")
        keyword2 = request.form.get("keyword2")
        keyword3 = request.form.get("keyword3")
        print()
        conn = sqlite3.connect('team3.db')
        c = conn.cursor()
        c.execute("INSERT into fashion values(null,null,?,?,?,?,?,?)",(catchcopy,name,image,keyword1,keyword2,keyword3))
        conn.commit()
        c.close()
        return redirect("/list")
    else:
        return redirect("/login")


#foods追加
@app.route("/add/foods", methods = ["GET"])
def add_foods_get():
    if 'manager_id' in session:
        return render_template("add_foods.html")
    else:
        return redirect("/login")

@app.route("/add/foods", methods = ["POST"])
def add_foods_post():
    if 'manager_id' in session:
        manager_id = session['manager_id']
        catchcopy = request.form.get("catchcopy")
        name = request.form.get("name")
        image = request.form.get("image")
        keyword1 = request.form.get("keyword1")
        keyword2 = request.form.get("keyword2")
        keyword3 = request.form.get("keyword3")
        print()
        conn = sqlite3.connect('team3.db')
        c = conn.cursor()
        c.execute("INSERT into foods values(null,null,?,?,?,?,?,?)",(catchcopy,name,image,keyword1,keyword2,keyword3))
        conn.commit()
        c.close()
        return redirect("/list")
    else:
        return redirect("/login")


#life追加
@app.route("/add/life", methods = ["GET"])
def add_life_get():
    if 'manager_id' in session:
        return render_template("add_life.html")
    else:
        return redirect("/login")

@app.route("/add/life", methods = ["POST"])
def add_life_post():
    if 'manager_id' in session:
        manager_id = session['manager_id']
        catchcopy = request.form.get("catchcopy")
        name = request.form.get("name")
        image = request.form.get("image")
        keyword1 = request.form.get("keyword1")
        keyword2 = request.form.get("keyword2")
        keyword3 = request.form.get("keyword3")
        print()
        conn = sqlite3.connect('team3.db')
        c = conn.cursor()
        c.execute("INSERT into life values(null,null,?,?,?,?,?,?)",(catchcopy,name,image,keyword1,keyword2,keyword3))
        conn.commit()
        c.close()
        return redirect("/list")
    else:
        return redirect("/login")


#medical追加
@app.route("/add/medical", methods = ["GET"])
def add_medical_get():
    if 'manager_id' in session:
        return render_template("add_madical.html")
    else:
        return redirect("/login")

@app.route("/add/medical", methods = ["POST"])
def add_medical_post():
    if 'manager_id' in session:
        manager_id = session['manager_id']
        catchcopy = request.form.get("catchcopy")
        name = request.form.get("name")
        image = request.form.get("image")
        keyword1 = request.form.get("keyword1")
        keyword2 = request.form.get("keyword2")
        keyword3 = request.form.get("keyword3")
        print()
        conn = sqlite3.connect('team3.db')
        c = conn.cursor()
        c.execute("INSERT into medical values(null,null,?,?,?,?,?,?)",(catchcopy,name,image,keyword1,keyword2,keyword3))
        conn.commit()
        c.close()
        return redirect("/list")
    else:
        return redirect("/login")


#history追加
@app.route("/add/history", methods = ["GET"])
def add_history_get():
    if 'manager_id' in session:
        return render_template("add_history.html")
    else:
        return redirect("/login")

@app.route("/add/history", methods = ["POST"])
def add_history_post():
    if 'manager_id' in session:
        manager_id = session['manager_id']
        catchcopy = request.form.get("catchcopy")
        name = request.form.get("name")
        image = request.form.get("image")
        keyword1 = request.form.get("keyword1")
        keyword2 = request.form.get("keyword2")
        keyword3 = request.form.get("keyword3")
        print()
        conn = sqlite3.connect('team3.db')
        c = conn.cursor()
        c.execute("INSERT into history values(null,null,?,?,?,?,?,?)",(catchcopy,name,image,keyword1,keyword2,keyword3))
        conn.commit()
        c.close()
        return redirect("/list")
    else:
        return redirect("/login")


#ride追加
@app.route("/add/ride", methods = ["GET"])
def add_ride_get():
    if 'manager_id' in session:
        return render_template("add_ride.html")
    else:
        return redirect("/login")

@app.route("/add/ride", methods = ["POST"])
def add_ride_post():
    if 'manager_id' in session:
        manager_id = session['manager_id']
        catchcopy = request.form.get("catchcopy")
        name = request.form.get("name")
        image = request.form.get("image")
        keyword1 = request.form.get("keyword1")
        keyword2 = request.form.get("keyword2")
        keyword3 = request.form.get("keyword3")
        print()
        conn = sqlite3.connect('team3.db')
        c = conn.cursor()
        c.execute("INSERT into ride values(null,null,?,?,?,?,?,?)",(catchcopy,name,image,keyword1,keyword2,keyword3))
        conn.commit()
        c.close()
        return redirect("/list")
    else:
        return redirect("/login")


# 編集コーナー
@app.route('/edit/nature/<int:id>')
def nature_edit(id):
    if 'manager_id' in session:
        conn = sqlite3.connect('team3.db')
        c = conn.cursor()
        c.execute("SELECT id,category_name,catchcopy,name,image,keyword1,keyword2,keyword3 FROM nature WHERE id = ?",(id,))
        nature_item = c.fetchone()
        id= nature_item[0]
        category_name=nature_item[1]
        catchcopy = nature_item[2]
        name = nature_item[3]
        image = nature_item[4]
        keyword1 = nature_item[5]
        keyword2 = nature_item[6]
        keyword3 = nature_item[7]
        print(nature_item)
        conn.close()
        nature_item = {"id":id,"catchcopy":catchcopy,"name":name, "image":image, "keyword1":keyword1, "keyword2":keyword2, "keyword3":keyword3} #辞書型をつくる

        return render_template("edit.html", id = id, category_name = category_name, catchcopy = catchcopy, name = name, image =image, keyword1 = keyword1, keyword2= keyword2, keyword3=keyword3) 
    else:
        return redirect("/login")

@app.route("/edit/nature",methods=["POST"])
def update_nature():
    if 'manager_id' in session:
        id = request.form.get("id") #htmlでとったid取得 
        name = request.form.get("name")
        catchcopy = request.form.get("catchcopy")
        keyword1 = request.form.get("keyword1")
        keyword2 = request.form.get("keyword2")
        keyword3 = request.form.get("keyword3")
        image = request.form.get("image")
        category_name = "nature"
        conn = sqlite3.connect('team3.db')
        c = conn.cursor()
        c.execute("UPDATE nature set name = ? ,image = ?, catchcopy = ? , keyword1 = ?, keyword2 = ?, keyword3 = ?  where id = ?",(name,image,catchcopy,keyword1,keyword2,keyword3,id))
        conn.commit()
        c.close()
        return redirect("/list")
    else:
        return redirect("/login")


# nature削除
@app.route('/del/nature/<int:id>')
def del_nature(id):
    if 'manager_id' in session:
        conn = sqlite3.connect('team3.db')
        c = conn.cursor()
        c.execute("DELETE FROM nature WHERE id = ?",(id,))
        conn.commit()
        conn.close()
        return redirect("/list")
    else:
        return redirect("/login")



# music削除
@app.route('/del/music/<int:id>')
def del_music(id):
    if 'manager_id' in session:
        conn = sqlite3.connect('team3.db')
        c = conn.cursor()
        c.execute("DELETE FROM music WHERE id = ?",(id,))
        conn.commit()
        conn.close()
        return redirect("/list")
    else:
        return redirect("/login")
      
      
        # c.execute("DELETE FROM music WHERE id = ?",(id,))
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
    return "ページないですよ"


if __name__ == "__main__":
    app.run(debug = True)








if __name__ == "__main__":
    # Flaskが持っている開発用サーバーを実行します
    app.run(debug=True)