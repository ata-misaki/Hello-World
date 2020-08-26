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

#追加
# @app.route("/add", methods = ["GET"])
# def add_get():
#     if 'manager_id' in session:
#         return render_template("add.html")
#     else:
#         return redirect("/login")

# @app.route("/add", methods = ["POST"])
# def add_post():
#     if 'manager_id' in session:
#         manager_id = session['manager_id']
#         catchcopy = request.form.get("catchcopy")
#         name = request.form.get("name")
#         image = request.form.get("image")
#         keyword1 = request.form.get("keyword1")
#         keyword2 = request.form.get("keyword2")
#         keyword3 = request.form.get("keyword3")
#         print()
#         conn = sqlite3.connect('team3.db')
#         c = conn.cursor()
#         c.execute("INSERT into art values(null,null,?,?,?,?,?,?)",(catchcopy,name,image,keyword1,keyword2,keyword3))
#         conn.commit()
#         c.close()
#         return redirect("/list")
#     else:
#         return redirect("/login")


        
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
        conn = sqlite3.connect('team3.db')
        c = conn.cursor()
        c.execute("INSERT into nature values(null,'自然',?,?,?,?,?,?,'nature')",(catchcopy,name,image,keyword1,keyword2,keyword3))
        conn.commit()
        c.close()
        return redirect("/list")
    else:
        return redirect("/login")

#play追加
@app.route("/add/play", methods = ["GET"])
def add_play_get():
    if 'manager_id' in session:
        return render_template("add_play.html")
    else:
        return redirect("/login")

@app.route("/add/play", methods = ["POST"])
def add_play_post():
    if 'manager_id' in session:
        manager_id = session['manager_id']
        catchcopy = request.form.get("catchcopy")
        name = request.form.get("name")
        image = request.form.get("image")
        keyword1 = request.form.get("keyword1")
        keyword2 = request.form.get("keyword2")
        keyword3 = request.form.get("keyword3")
        conn = sqlite3.connect('team3.db')
        c = conn.cursor()
        c.execute("INSERT into play values(null,'娯楽',?,?,?,?,?,?,'play')",(catchcopy,name,image,keyword1,keyword2,keyword3))
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
        c.execute("INSERT into art values(null,'芸術',?,?,?,?,?,?,'art')",(catchcopy,name,image,keyword1,keyword2,keyword3))
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
        conn = sqlite3.connect('team3.db')
        c = conn.cursor()
        c.execute("INSERT into music values(null,'音楽',?,?,?,?,?,?,'music')",(catchcopy,name,image,keyword1,keyword2,keyword3))
        conn.commit()
        c.close()
        return redirect("/list")
    else:
        return redirect("/login")


#sports追加
@app.route("/add/sports", methods = ["GET"])
def add_sports_get():
    if 'manager_id' in session:
        return render_template("add_sports.html")
    else:
        return redirect("/login")

@app.route("/add/sports", methods = ["POST"])
def add_sports_post():
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
        c.execute("INSERT into sports values(null,'スポーツ',?,?,?,?,?,?,'sports')",(catchcopy,name,image,keyword1,keyword2,keyword3))
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
        conn = sqlite3.connect('team3.db')
        c = conn.cursor()
        c.execute("INSERT into trip values(null,'旅',?,?,?,?,?,?,'trip')",(catchcopy,name,image,keyword1,keyword2,keyword3))
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
        c.execute("INSERT into fashion values(null,'美容・ファッション',?,?,?,?,?,?,'fashion')",(catchcopy,name,image,keyword1,keyword2,keyword3))
        conn.commit()
        c.close()
        return redirect("/list")
    else:
        return redirect("/login")


#food追加
@app.route("/add/food", methods = ["GET"])
def add_food_get():
    if 'manager_id' in session:
        return render_template("add_food.html")
    else:
        return redirect("/login")

@app.route("/add/food", methods = ["POST"])
def add_food_post():
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
        c.execute("INSERT into food values(null,'食',?,?,?,?,?,?,'food')",(catchcopy,name,image,keyword1,keyword2,keyword3))
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
        c.execute("INSERT into life values(null,'暮らし',?,?,?,?,?,?,'life')",(catchcopy,name,image,keyword1,keyword2,keyword3))
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
        c.execute("INSERT into medical values(null,'医療',?,?,?,?,?,?,'medical')",(catchcopy,name,image,keyword1,keyword2,keyword3))
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
        c.execute("INSERT into history values(null,'歴史',?,?,?,?,?,?,'history')",(catchcopy,name,image,keyword1,keyword2,keyword3))
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
        c.execute("INSERT into ride values(null,'乗り物',?,?,?,?,?,?,'ride')",(catchcopy,name,image,keyword1,keyword2,keyword3))
        conn.commit()
        c.close()
        return redirect("/list")
    else:
        return redirect("/login")


# 編集コーナー
# nature edit
@app.route('/edit/nature/<int:id>')
def nature_edit(id):
    if 'manager_id' in session:
        conn = sqlite3.connect('team3.db')
        c = conn.cursor()
        c.execute("SELECT id,category_name,catchcopy,name,image,keyword1,keyword2,keyword3,category FROM nature WHERE id = ?",(id,))
        nature_item = c.fetchone()
        id= nature_item[0]
        category_name=nature_item[1]
        catchcopy = nature_item[2]
        name = nature_item[3]
        image = nature_item[4]
        keyword1 = nature_item[5]
        keyword2 = nature_item[6]
        keyword3 = nature_item[7]
        category = nature_item[8]
        conn.close()
        nature_item = {"id":id,"catchcopy":catchcopy,"name":name, "image":image, "keyword1":keyword1, "keyword2":keyword2, "keyword3":keyword3, "category":category} #辞書型をつくる
        return render_template("edit.html", id = id, category_name = category_name, catchcopy = catchcopy, name = name, image =image, keyword1 = keyword1, keyword2= keyword2, keyword3=keyword3, category=category) 
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
        category_name = "自然"
        conn = sqlite3.connect('team3.db')
        c = conn.cursor()
        c.execute("UPDATE nature set catchcopy = ? , name = ? ,image = ?, keyword1 = ?, keyword2 = ?, keyword3 = ?  where id = ?",(catchcopy,name,image,keyword1,keyword2,keyword3,id))
        conn.commit()
        c.close()
        return redirect("/list")
    else:
        return redirect("/login")

# play edit
@app.route('/edit/play/<int:id>')
def play_edit(id):
    if 'manager_id' in session:
        conn = sqlite3.connect('team3.db')
        c = conn.cursor()
        c.execute("SELECT id,category_name,catchcopy,name,image,keyword1,keyword2,keyword3,category FROM play WHERE id = ?",(id,))
        play_item = c.fetchone()
        id= play_item[0]
        category_name=play_item[1]
        catchcopy = play_item[2]
        name = play_item[3]
        image = play_item[4]
        keyword1 = play_item[5]
        keyword2 = play_item[6]
        keyword3 = play_item[7]
        category = play_item[8]
        conn.close()
        play_item = {"id":id,"catchcopy":catchcopy,"name":name, "image":image, "keyword1":keyword1, "keyword2":keyword2, "keyword3":keyword3, "category":category} #辞書型をつくる
        return render_template("edit.html", id = id, category_name = category_name, catchcopy = catchcopy, name = name, image =image, keyword1 = keyword1, keyword2= keyword2, keyword3=keyword3, category=category) 
    else:
        return redirect("/login")

@app.route("/edit/play",methods=["POST"])
def update_play():
    if 'manager_id' in session:
        id = request.form.get("id") #htmlでとったid取得 
        name = request.form.get("name")
        catchcopy = request.form.get("catchcopy")
        keyword1 = request.form.get("keyword1")
        keyword2 = request.form.get("keyword2")
        keyword3 = request.form.get("keyword3")
        image = request.form.get("image")
        category_name = "娯楽"
        conn = sqlite3.connect('team3.db')
        c = conn.cursor()
        c.execute("UPDATE nature set catchcopy = ? , name = ? ,image = ?, keyword1 = ?, keyword2 = ?, keyword3 = ?  where id = ?",(catchcopy,name,image,keyword1,keyword2,keyword3,id))
        conn.commit()
        c.close()
        return redirect("/list")
    else:
        return redirect("/login")


# music edit
@app.route('/edit/music/<int:id>')
def music_edit(id):
    if 'manager_id' in session:
        conn = sqlite3.connect('team3.db')
        c = conn.cursor()
        c.execute("SELECT id,category_name,catchcopy,name,image,keyword1,keyword2,keyword3,category from music WHERE id = ?",(id,))
        music_item = c.fetchone()
        id= music_item[0]
        category_name=music_item[1]
        catchcopy = music_item[2]
        name = music_item[3]
        image = music_item[4]
        keyword1 = music_item[5]
        keyword2 = music_item[6]
        keyword3 = music_item[7]
        category = music_item[8]
        conn.close()
        music_item = {"id":id,"catchcopy":catchcopy,"name":name, "image":image, "keyword1":keyword1, "keyword2":keyword2, "keyword3":keyword3, "category":category} #辞書型をつくる
        return render_template("edit.html", id = id, category_name = category_name, catchcopy = catchcopy, name = name, image =image, keyword1 = keyword1, keyword2= keyword2, keyword3=keyword3, category=category) 
    else:
        return redirect("/login")

@app.route("/edit/music",methods=["POST"])
def update_music():
    if 'manager_id' in session:
        id = request.form.get("id") #htmlでとったid取得 
        name = request.form.get("name")
        catchcopy = request.form.get("catchcopy")
        keyword1 = request.form.get("keyword1")
        keyword2 = request.form.get("keyword2")
        keyword3 = request.form.get("keyword3")
        image = request.form.get("image")
        category_name = "音楽"
        conn = sqlite3.connect('team3.db')
        c = conn.cursor()
        c.execute("UPDATE music set name = ? ,image = ?, catchcopy = ? , keyword1 = ?, keyword2 = ?, keyword3 = ?  where id = ?",(name,image,catchcopy,keyword1,keyword2,keyword3,id))
        conn.commit()
        c.close()
        return redirect("/list")
    else:
        return redirect("/login")

# art edit
@app.route('/edit/art/<int:id>')
def art_edit(id):
    if 'manager_id' in session:
        conn = sqlite3.connect('team3.db')
        c = conn.cursor()
        c.execute("SELECT id,category_name,catchcopy,name,image,keyword1,keyword2,keyword3,category FROM art WHERE id = ?",(id,))
        art_item = c.fetchone()
        id= art_item[0]
        category_name=art_item[1]
        catchcopy = art_item[2]
        name = art_item[3]
        image = art_item[4]
        keyword1 = art_item[5]
        keyword2 = art_item[6]
        keyword3 = art_item[7]
        category = art_item[8]
        conn.close()
        art_item = {"id":id,"catchcopy":catchcopy,"name":name, "image":image, "keyword1":keyword1, "keyword2":keyword2, "keyword3":keyword3, "category":category} #辞書型をつくる
        return render_template("edit.html", id = id, category_name = category_name, catchcopy = catchcopy, name = name, image =image, keyword1 = keyword1, keyword2= keyword2, keyword3=keyword3, category=category) 
    else:
        return redirect("/login")

@app.route("/edit/art",methods=["POST"])
def update_art():
    if 'manager_id' in session:
        id = request.form.get("id") #htmlでとったid取得 
        name = request.form.get("name")
        catchcopy = request.form.get("catchcopy")
        keyword1 = request.form.get("keyword1")
        keyword2 = request.form.get("keyword2")
        keyword3 = request.form.get("keyword3")
        image = request.form.get("image")
        category_name = "芸術"
        conn = sqlite3.connect('team3.db')
        c = conn.cursor()
        c.execute("UPDATE art set name = ? ,image = ?, catchcopy = ? , keyword1 = ?, keyword2 = ?, keyword3 = ?  where id = ?",(name,image,catchcopy,keyword1,keyword2,keyword3,id))
        conn.commit()
        c.close()
        return redirect("/list")
    else:
        return redirect("/login")


#sports edit
@app.route('/edit/sports/<int:id>')
def sports_edit(id):
    if 'manager_id' in session:
        conn = sqlite3.connect('team3.db')
        c = conn.cursor()
        c.execute("SELECT id,category_name,catchcopy,name,image,keyword1,keyword2,keyword3,category FROM sports WHERE id = ?",(id,))
        sports_item = c.fetchone()
        id= sports_item[0]
        category_name=sports_item[1]
        catchcopy = sports_item[2]
        name = sports_item[3]
        image = sports_item[4]
        keyword1 = sports_item[5]
        keyword2 = sports_item[6]
        keyword3 = sports_item[7]
        category = sports_item[8]
        conn.close()
        sports_item = {"id":id,"catchcopy":catchcopy,"name":name, "image":image, "keyword1":keyword1, "keyword2":keyword2, "keyword3":keyword3, "category":category} #辞書型をつくる
        return render_template("edit.html", id = id, category_name = category_name, catchcopy = catchcopy, name = name, image =image, keyword1 = keyword1, keyword2= keyword2, keyword3=keyword3, category=category) 
    else:
        return redirect("/login")

@app.route("/edit/sports",methods=["POST"])
def update_sports():
    if 'manager_id' in session:
        id = request.form.get("id") #htmlでとったid取得 
        name = request.form.get("name")
        catchcopy = request.form.get("catchcopy")
        keyword1 = request.form.get("keyword1")
        keyword2 = request.form.get("keyword2")
        keyword3 = request.form.get("keyword3")
        image = request.form.get("image")
        category_name = "スポーツ"
        conn = sqlite3.connect('team3.db')
        c = conn.cursor()
        c.execute("UPDATE sports set name = ? ,image = ?, catchcopy = ? , keyword1 = ?, keyword2 = ?, keyword3 = ?  where id = ?",(name,image,catchcopy,keyword1,keyword2,keyword3,id))
        conn.commit()
        c.close()
        return redirect("/list")
    else:
        return redirect("/login")

#trip edit
@app.route('/edit/trip/<int:id>')
def trip_edit(id):
    if 'manager_id' in session:
        conn = sqlite3.connect('team3.db')
        c = conn.cursor()
        c.execute("SELECT id,category_name,catchcopy,name,image,keyword1,keyword2,keyword3,category FROM trip WHERE id = ?",(id,))
        trip_item = c.fetchone()
        id= trip_item[0]
        category_name=trip_item[1]
        catchcopy = trip_item[2]
        name = trip_item[3]
        image = trip_item[4]
        keyword1 = trip_item[5]
        keyword2 = trip_item[6]
        keyword3 = trip_item[7]
        category = trip_item[8]
        conn.close()
        trip_item = {"id":id,"catchcopy":catchcopy,"name":name, "image":image, "keyword1":keyword1, "keyword2":keyword2, "keyword3":keyword3, "category":category} #辞書型をつくる
        return render_template("edit.html", id = id, category_name = category_name, catchcopy = catchcopy, name = name, image =image, keyword1 = keyword1, keyword2= keyword2, keyword3=keyword3, category=category) 
    else:
        return redirect("/login")

@app.route("/edit/trip",methods=["POST"])
def update_trip():
    if 'manager_id' in session:
        id = request.form.get("id") #htmlでとったid取得 
        name = request.form.get("name")
        catchcopy = request.form.get("catchcopy")
        keyword1 = request.form.get("keyword1")
        keyword2 = request.form.get("keyword2")
        keyword3 = request.form.get("keyword3")
        image = request.form.get("image")
        category_name = "trip"
        conn = sqlite3.connect('team3.db')
        c = conn.cursor()
        c.execute("UPDATE trip set name = ? ,image = ?, catchcopy = ? , keyword1 = ?, keyword2 = ?, keyword3 = ?  where id = ?",(name,image,catchcopy,keyword1,keyword2,keyword3,id))
        conn.commit()
        c.close()
        return redirect("/list")
    else:
        return redirect("/login")

# fashion edit
@app.route('/edit/fashion/<int:id>')
def fashion_edit(id):
    if 'manager_id' in session:
        conn = sqlite3.connect('team3.db')
        c = conn.cursor()
        c.execute("SELECT id,category_name,catchcopy,name,image,keyword1,keyword2,keyword3,category FROM fashion WHERE id = ?",(id,))
        fashion_item = c.fetchone()
        id= fashion_item[0]
        category_name=fashion_item[1]
        catchcopy = fashion_item[2]
        name = fashion_item[3]
        image = fashion_item[4]
        keyword1 = fashion_item[5]
        keyword2 = fashion_item[6]
        keyword3 = fashion_item[7]
        category = fashion_item[8]
        conn.close()
        fashion_item = {"id":id,"catchcopy":catchcopy,"name":name, "image":image, "keyword1":keyword1, "keyword2":keyword2, "keyword3":keyword3, "category":category} #辞書型をつくる
        return render_template("edit.html", id = id, category_name = category_name, catchcopy = catchcopy, name = name, image =image, keyword1 = keyword1, keyword2= keyword2, keyword3=keyword3, category=category) 
    else:
        return redirect("/login")

@app.route("/edit/fashion",methods=["POST"])
def update_fashion():
    if 'manager_id' in session:
        id = request.form.get("id") #htmlでとったid取得 
        name = request.form.get("name")
        catchcopy = request.form.get("catchcopy")
        keyword1 = request.form.get("keyword1")
        keyword2 = request.form.get("keyword2")
        keyword3 = request.form.get("keyword3")
        image = request.form.get("image")
        category_name = "美容・ファッション"
        conn = sqlite3.connect('team3.db')
        c = conn.cursor()
        c.execute("UPDATE fashion set name = ? ,image = ?, catchcopy = ? , keyword1 = ?, keyword2 = ?, keyword3 = ?  where id = ?",(name,image,catchcopy,keyword1,keyword2,keyword3,id))
        conn.commit()
        c.close()
        return redirect("/list")
    else:
        return redirect("/login")


# food編集
@app.route('/edit/food/<int:id>')
def food_edit(id):
    if 'manager_id' in session:
        conn = sqlite3.connect('team3.db')
        c = conn.cursor()
        c.execute("SELECT id,category_name,catchcopy,name,image,keyword1,keyword2,keyword3,category FROM food WHERE id = ?",(id,))
        food_item = c.fetchone()
        id= food_item[0]
        category_name=food_item[1]
        catchcopy = food_item[2]
        name = food_item[3]
        image = food_item[4]
        keyword1 = food_item[5]
        keyword2 = food_item[6]
        keyword3 = food_item[7]
        category = food_item[8]
        conn.close()
        food_item = {"id":id,"catchcopy":catchcopy,"name":name, "image":image, "keyword1":keyword1, "keyword2":keyword2, "keyword3":keyword3, "category":category} #辞書型をつくる
        return render_template("edit.html", id = id, category_name = category_name, catchcopy = catchcopy, name = name, image =image, keyword1 = keyword1, keyword2= keyword2, keyword3=keyword3, category=category) 
    else:
        return redirect("/login")

@app.route("/edit/food",methods=["POST"])
def update_food():
    if 'manager_id' in session:
        id = request.form.get("id") #htmlでとったid取得 
        name = request.form.get("name")
        catchcopy = request.form.get("catchcopy")
        keyword1 = request.form.get("keyword1")
        keyword2 = request.form.get("keyword2")
        keyword3 = request.form.get("keyword3")
        image = request.form.get("image")
        category_name = "food"
        conn = sqlite3.connect('team3.db')
        c = conn.cursor()
        c.execute("UPDATE food set name = ? ,image = ?, catchcopy = ? , keyword1 = ?, keyword2 = ?, keyword3 = ?  where id = ?",(name,image,catchcopy,keyword1,keyword2,keyword3,id))
        conn.commit()
        c.close()
        return redirect("/list")
    else:
        return redirect("/login")

# life
@app.route('/edit/life/<int:id>')
def life_edit(id):
    if 'manager_id' in session:
        conn = sqlite3.connect('team3.db')
        c = conn.cursor()
        c.execute("SELECT id,category_name,catchcopy,name,image,keyword1,keyword2,keyword3,category FROM life WHERE id = ?",(id,))
        life_item = c.fetchone()
        id= life_item[0]
        category_name=life_item[1]
        catchcopy = life_item[2]
        name = life_item[3]
        image = life_item[4]
        keyword1 = life_item[5]
        keyword2 = life_item[6]
        keyword3 = life_item[7]
        category = life_item[8]
        conn.close()
        life_item = {"id":id,"catchcopy":catchcopy,"name":name, "image":image, "keyword1":keyword1, "keyword2":keyword2, "keyword3":keyword3, "category":category} #辞書型をつくる
        return render_template("edit.html", id = id, category_name = category_name, catchcopy = catchcopy, name = name, image =image, keyword1 = keyword1, keyword2= keyword2, keyword3=keyword3, category=category) 
    else:
        return redirect("/login")

@app.route("/edit/life",methods=["POST"])
def update_life():
    if 'manager_id' in session:
        id = request.form.get("id") #htmlでとったid取得 
        name = request.form.get("name")
        catchcopy = request.form.get("catchcopy")
        keyword1 = request.form.get("keyword1")
        keyword2 = request.form.get("keyword2")
        keyword3 = request.form.get("keyword3")
        image = request.form.get("image")
        category_name = "暮らし"
        conn = sqlite3.connect('team3.db')
        c = conn.cursor()
        c.execute("UPDATE life set name = ? ,image = ?, catchcopy = ? , keyword1 = ?, keyword2 = ?, keyword3 = ?  where id = ?",(name,image,catchcopy,keyword1,keyword2,keyword3,id))
        conn.commit()
        c.close()
        return redirect("/list")
    else:
        return redirect("/login")

# medical編集 
@app.route('/edit/medical/<int:id>')
def medical_edit(id):
    if 'manager_id' in session:
        conn = sqlite3.connect('team3.db')
        c = conn.cursor()
        c.execute("SELECT id,category_name,catchcopy,name,image,keyword1,keyword2,keyword3,category FROM medical WHERE id = ?",(id,))
        medical_item = c.fetchone()
        id= medical_item[0]
        category_name=medical_item[1]
        catchcopy = medical_item[2]
        name = medical_item[3]
        image = medical_item[4]
        keyword1 = medical_item[5]
        keyword2 = medical_item[6]
        keyword3 = medical_item[7]
        category = medical_item[8]
        conn.close()
        medical_item = {"id":id,"catchcopy":catchcopy,"name":name, "image":image, "keyword1":keyword1, "keyword2":keyword2, "keyword3":keyword3,"category":category} #辞書型をつくる
        return render_template("edit.html", id = id, category_name = category_name, catchcopy = catchcopy, name = name, image =image, keyword1 = keyword1, keyword2= keyword2, keyword3=keyword3, category=category) 
    else:
        return redirect("/login")

@app.route("/edit/medical",methods=["POST"])
def update_medical():
    if 'manager_id' in session:
        id = request.form.get("id") #htmlでとったid取得 
        name = request.form.get("name")
        catchcopy = request.form.get("catchcopy")
        keyword1 = request.form.get("keyword1")
        keyword2 = request.form.get("keyword2")
        keyword3 = request.form.get("keyword3")
        image = request.form.get("image")
        category_name = "medical"
        conn = sqlite3.connect('team3.db')
        c = conn.cursor()
        c.execute("UPDATE medical set name = ? ,image = ?, catchcopy = ? , keyword1 = ?, keyword2 = ?, keyword3 = ?  where id = ?",(name,image,catchcopy,keyword1,keyword2,keyword3,id))
        conn.commit()
        c.close()
        return redirect("/list")
    else:
        return redirect("/login")

# history
@app.route('/edit/history/<int:id>')
def history_edit(id):
    if 'manager_id' in session:
        conn = sqlite3.connect('team3.db')
        c = conn.cursor()
        c.execute("SELECT id,category_name,catchcopy,name,image,keyword1,keyword2,keyword3 FROM history WHERE id = ?",(id,))
        history_item = c.fetchone()
        id= history_item[0]
        category_name=history_item[1]
        catchcopy = history_item[2]
        name = history_item[3]
        image = history_item[4]
        keyword1 = history_item[5]
        keyword2 = history_item[6]
        keyword3 = history_item[7]
        category = history_item[8]
        conn.close()
        history_item = {"id":id,"catchcopy":catchcopy,"name":name, "image":image, "keyword1":keyword1, "keyword2":keyword2, "keyword3":keyword3, "category":category} #辞書型をつくる
        return render_template("edit.html", id = id, category_name = category_name, catchcopy = catchcopy, name = name, image =image, keyword1 = keyword1, keyword2= keyword2, keyword3=keyword3, category=category) 
    else:
        return redirect("/login")

@app.route("/edit/history",methods=["POST"])
def update_history():
    if 'manager_id' in session:
        id = request.form.get("id") #htmlでとったid取得 
        name = request.form.get("name")
        catchcopy = request.form.get("catchcopy")
        keyword1 = request.form.get("keyword1")
        keyword2 = request.form.get("keyword2")
        keyword3 = request.form.get("keyword3")
        image = request.form.get("image")
        category_name = "歴史"
        conn = sqlite3.connect('team3.db')
        c = conn.cursor()
        c.execute("UPDATE history set name = ? ,image = ?, catchcopy = ? , keyword1 = ?, keyword2 = ?, keyword3 = ?  where id = ?",(name,image,catchcopy,keyword1,keyword2,keyword3,id))
        conn.commit()
        c.close()
        return redirect("/list")
    else:
        return redirect("/login")

# ride edit
@app.route('/edit/ride/<int:id>')
def ride_edit(id):
    if 'manager_id' in session:
        conn = sqlite3.connect('team3.db')
        c = conn.cursor()
        c.execute("SELECT id,category_name,catchcopy,name,image,keyword1,keyword2,keyword3,category FROM ride WHERE id = ?",(id,))
        ride_item = c.fetchone()
        id= ride_item[0]
        category_name=ride_item[1]
        catchcopy = ride_item[2]
        name = ride_item[3]
        image = ride_item[4]
        keyword1 = ride_item[5]
        keyword2 = ride_item[6]
        keyword3 = ride_item[7]
        category = ride_item[8]
        conn.close()
        ride_item = {"id":id,"catchcopy":catchcopy,"name":name, "image":image, "keyword1":keyword1, "keyword2":keyword2, "keyword3":keyword3,"category":category} #辞書型をつくる
        return render_template("edit.html", id = id, category_name = category_name, catchcopy = catchcopy, name = name, image =image, keyword1 = keyword1, keyword2= keyword2, keyword3=keyword3, category=category) 
    else:
        return redirect("/login")

@app.route("/edit/ride",methods=["POST"])
def update_ride():
    if 'manager_id' in session:
        id = request.form.get("id") #htmlでとったid取得 
        name = request.form.get("name")
        catchcopy = request.form.get("catchcopy")
        keyword1 = request.form.get("keyword1")
        keyword2 = request.form.get("keyword2")
        keyword3 = request.form.get("keyword3")
        image = request.form.get("image")
        category_name = "乗り物"
        conn = sqlite3.connect('team3.db')
        c = conn.cursor()
        c.execute("UPDATE ride set name = ? ,image = ?, catchcopy = ? , keyword1 = ?, keyword2 = ?, keyword3 = ?  where id = ?",(name,image,catchcopy,keyword1,keyword2,keyword3,id))
        conn.commit()
        c.close()
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

@app.route('/del/art/<int:id>')
def del_art(id):
    if 'manager_id' in session:
        conn = sqlite3.connect('team3.db')
        c = conn.cursor()
        c.execute("DELETE FROM art WHERE id = ?",(id,))
        conn.commit()
        conn.close()
        return redirect("/list")
    else:
        return redirect("/login")

@app.route('/del/sports/<int:id>')
def del_sports(id):
    if 'manager_id' in session:
        conn = sqlite3.connect('team3.db')
        c = conn.cursor()
        c.execute("DELETE FROM sports WHERE id = ?",(id,))
        conn.commit()
        conn.close()
        return redirect("/list")
    else:
        return redirect("/login")

@app.route('/del/play/<int:id>')
def del_play(id):
    if 'manager_id' in session:
        conn = sqlite3.connect('team3.db')
        c = conn.cursor()
        c.execute("DELETE FROM play WHERE id = ?",(id,))
        conn.commit()
        conn.close()
        return redirect("/list")
    else:
        return redirect("/login")

@app.route('/del/life/<int:id>')
def del_life(id):
    if 'manager_id' in session:
        conn = sqlite3.connect('team3.db')
        c = conn.cursor()
        c.execute("DELETE FROM life WHERE id = ?",(id,))
        conn.commit()
        conn.close()
        return redirect("/list")
    else:
        return redirect("/login")

@app.route('/del/food/<int:id>')
def del_food(id):
    if 'manager_id' in session:
        conn = sqlite3.connect('team3.db')
        c = conn.cursor()
        c.execute("DELETE FROM food WHERE id = ?",(id,))
        conn.commit()
        conn.close()
        return redirect("/list")
    else:
        return redirect("/login")

@app.route('/del/trip/<int:id>')
def del_trip(id):
    if 'manager_id' in session:
        conn = sqlite3.connect('team3.db')
        c = conn.cursor()
        c.execute("DELETE FROM trip WHERE id = ?",(id,))
        conn.commit()
        conn.close()
        return redirect("/list")
    else:
        return redirect("/login")

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

@app.route('/del/fashion/<int:id>')
def del_fashion(id):
    if 'manager_id' in session:
        conn = sqlite3.connect('team3.db')
        c = conn.cursor()
        c.execute("DELETE FROM fashion WHERE id = ?",(id,))
        conn.commit()
        conn.close()
        return redirect("/list")
    else:
        return redirect("/login")

@app.route('/del/ride/<int:id>')
def del_ride(id):
    if 'manager_id' in session:
        conn = sqlite3.connect('team3.db')
        c = conn.cursor()
        c.execute("DELETE FROM ride WHERE id = ?",(id,))
        conn.commit()
        conn.close()
        return redirect("/list")
    else:
        return redirect("/login")

@app.route('/del/history/<int:id>')
def del_history(id):
    if 'manager_id' in session:
        conn = sqlite3.connect('team3.db')
        c = conn.cursor()
        c.execute("DELETE FROM history WHERE id = ?",(id,))
        conn.commit()
        conn.close()
        return redirect("/list")
    else:
        return redirect("/login")

@app.route('/del/medical/<int:id>')
def del_medical(id):
    if 'manager_id' in session:
        conn = sqlite3.connect('team3.db')
        c = conn.cursor()
        c.execute("DELETE FROM medical WHERE id = ?",(id,))
        conn.commit()
        conn.close()
        return redirect("/list")
    else:
        return redirect("/login")
     
#管理者登録
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
    return "ページはないですよ"


if __name__ == "__main__":
    app.run(debug = True)








if __name__ == "__main__":
    # Flaskが持っている開発用サーバーを実行します
    app.run(debug=True)