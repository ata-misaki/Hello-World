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


@app.route("/")
def indexpage():
    return render_template("index.html")


# カテゴリーページ反映用

@app.route("/music_con")
def music_con():
    conn = sqlite3.connect('team3.db')
    c = conn.cursor()
    c.execute("select category.category,music.id,music.catchcopy from category join music on category.name = music.category_name")
    contents_list = []
    for row in c.fetchall():
        contents_list.append({"category":row[0],"id":row[1],"catchcopy":row[2]})
    c.execute("select name,category from category where id == 1 ")
    cate = c.fetchone()
    name = cate[0]
    img = cate[1]
    conn.close()
    return render_template("content1.html", contents_list = contents_list, name = name , img = img)


@app.route("/art_con")
def art_con():
    conn = sqlite3.connect('team3.db')
    c = conn.cursor()
    c.execute("select category.category,art.id,art.catchcopy from category join art on category.name = art.category_name")
    contents_list = []
    for row in c.fetchall():
        contents_list.append({"category":row[0],"id":row[1],"catchcopy":row[2]})
    c.execute("select name,category from category where id == 2 ")
    cate = c.fetchone()
    name = cate[0]
    img = cate[1]
    conn.close()
    return render_template("content1.html", contents_list = contents_list, name = name , img = img)


@app.route("/sport_con")
def sport_con():
    conn = sqlite3.connect('team3.db')
    c = conn.cursor()
    c.execute("select category.category,sports.id,sports.catchcopy from category join sports on category.name = sports.category_name")
    contents_list = []
    for row in c.fetchall():
        contents_list.append({"category":row[0],"id":row[1],"catchcopy":row[2]})
    c.execute("select name,category from category where id == 3 ")
    cate = c.fetchone()
    name = cate[0]
    img = cate[1]
    conn.close()
    return render_template("content1.html", contents_list = contents_list, name = name , img = img)

@app.route("/play_con")
def play_con():
    conn = sqlite3.connect('team3.db')
    c = conn.cursor()
    c.execute("select category.category,play.id,play.catchcopy from category join play on category.name = play.category_name")
    contents_list = []
    for row in c.fetchall():
        contents_list.append({"category":row[0],"id":row[1],"catchcopy":row[2]})
    c.execute("select name,category from category where id == 4 ")
    cate = c.fetchone()
    name = cate[0]
    img = cate[1]
    conn.close()
    return render_template("content1.html", contents_list = contents_list, name = name , img = img)



@app.route("/life_con")
def life_con():
    conn = sqlite3.connect('team3.db')
    c = conn.cursor()
    c.execute("select category.category,life.id,life.catchcopy from category join life on category.name = life.category_name")
    contents_list = []
    for row in c.fetchall():
        contents_list.append({"category":row[0],"id":row[1],"catchcopy":row[2]})
    c.execute("select name,category from category where id == 5 ")
    cate = c.fetchone()
    name = cate[0]
    img = cate[1]
    conn.close()
    return render_template("content1.html", contents_list = contents_list, name = name , img = img)




@app.route("/food_con")
def foods_con():
    conn = sqlite3.connect('team3.db')
    c = conn.cursor()
    c.execute("select category.category,food.id,food.catchcopy from category join food on category.name = food.category_name")
    contents_list = []
    for row in c.fetchall():
        contents_list.append({"category":row[0],"id":row[1],"catchcopy":row[2]})
    c.execute("select name,category from category where id == 6 ")
    cate = c.fetchone()
    name = cate[0]
    img = cate[1]
    conn.close()
    return render_template("content1.html", contents_list = contents_list, name = name , img = img)



@app.route("/trip_con")
def trip_con():
    conn = sqlite3.connect('team3.db')
    c = conn.cursor()
    c.execute("select category.category,trip.id,trip.catchcopy from category join trip on category.name = trip.category_name")
    contents_list = []
    for row in c.fetchall():
        contents_list.append({"category":row[0],"id":row[1],"catchcopy":row[2]})
    c.execute("select name,category from category where id == 7 ")
    cate = c.fetchone()
    name = cate[0]
    img = cate[1]
    conn.close()
    return render_template("content1.html", contents_list = contents_list, name = name , img = img)



@app.route("/nature_con")
def nature_con():
    conn = sqlite3.connect('team3.db')
    c = conn.cursor()
    c.execute("select category.category,nature.id,nature.catchcopy from category join nature on category.name = nature.category_name")
    contents_list = []
    for row in c.fetchall():
        contents_list.append({"category":row[0],"id":row[1],"catchcopy":row[2]})
    c.execute("select name,category from category where id == 8 ")
    cate = c.fetchone()
    name = cate[0]
    img = cate[1]
    conn.close()
    return render_template("content1.html", contents_list = contents_list, name = name , img = img)



@app.route("/fashion_con")
def fashion_con():
    conn = sqlite3.connect('team3.db')
    c = conn.cursor()
    c.execute("select category.category,fashion.id,fashion.catchcopy from category join fashion on category.name = fashion.category_name")
    contents_list = []
    for row in c.fetchall():
        contents_list.append({"category":row[0],"id":row[1],"catchcopy":row[2]})
    c.execute("select name,category from category where id == 9 ")
    cate = c.fetchone()
    name = cate[0]
    img = cate[1]
    conn.close()
    return render_template("content1.html", contents_list = contents_list, name = name , img = img)



@app.route("/ride_con")
def ride_con():
    conn = sqlite3.connect('team3.db')
    c = conn.cursor()
    c.execute("select category.category,ride.id,ride.catchcopy from category join ride on category.name = ride.category_name")
    contents_list = []
    for row in c.fetchall():
        contents_list.append({"category":row[0],"id":row[1],"catchcopy":row[2]})
    c.execute("select name,category from category where id == 10 ")
    cate = c.fetchone()
    name = cate[0]
    img = cate[1]
    conn.close()
    return render_template("content1.html", contents_list = contents_list, name = name , img = img)



@app.route("/history_con")
def history_con():
    conn = sqlite3.connect('team3.db')
    c = conn.cursor()
    c.execute("select category.category,history.id,history.catchcopy from category join history on category.name = history.category_name")
    contents_list = []
    for row in c.fetchall():
        contents_list.append({"category":row[0],"id":row[1],"catchcopy":row[2]})
    c.execute("select name,category from category where id == 11 ")
    cate = c.fetchone()
    name = cate[0]
    img = cate[1]
    conn.close()
    return render_template("content1.html", contents_list = contents_list, name = name , img = img)



@app.route("/medical_con")
def medical_con():
    conn = sqlite3.connect('team3.db')
    c = conn.cursor()
    c.execute("select category.category,medical.id,medical.catchcopy from category join medical on category.name = medical.category_name")
    contents_list = []
    for row in c.fetchall():
        contents_list.append({"category":row[0],"id":row[1],"catchcopy":row[2]})
    c.execute("select name,category from category where id == 12 ")
    cate = c.fetchone()
    name = cate[0]
    img = cate[1]
    conn.close()
    return render_template("content1.html", contents_list = contents_list, name = name , img = img)





# コンテンツページ反映用
# テーブルfashion
@app.route('/fashion/<int:id>')
def fashionpage(id):
    conn = sqlite3.connect('team3.db')
    c = conn.cursor()
    c.execute("select id,category_name,catchcopy,name,keyword1 from fashion where id = ?", (id,) )
    contents = c.fetchone()
    category_id = contents[0]
    category_name = contents[1]
    catchcopy = contents[2]
    name = contents[3]
    keyword1 = contents[4]
    c.execute("select keyword2 from fashion where id = ? and keyword2 is not null", (id,) )
    keyword2 = c.fetchone()
    if keyword2 is not None:
        keyword2 = keyword2[0]
    else:
        keyword2 = ""
    c.execute("select keyword3 from fashion where id = ? and keyword3 is not null", (id,) )
    keyword3 = c.fetchone()
    if keyword3 is not None:
        keyword3 = keyword3[0]
    else:
        keyword3 = ""
    c.execute("select image from fashion where id = ?", (id,) )
    image = c.fetchone()
    image = image[0]
    conn.close()
    return render_template("contents.html",category_id = category_id,category_name = category_name,catchcopy = catchcopy,name = name,keyword1 = keyword1,keyword2 = keyword2,keyword3 = keyword3,image = image )
# テーブルfashion

# テーブルfood
@app.route('/food/<int:id>')
def foodspage(id):
    conn = sqlite3.connect('team3.db')
    c = conn.cursor()
    c.execute("select id,category_name,catchcopy,name,keyword1 from food where id = ?", (id,) )
    contents = c.fetchone()
    category_id = contents[0]
    category_name = contents[1]
    catchcopy = contents[2]
    name = contents[3]
    keyword1 = contents[4]
    c.execute("select keyword2 from food where id = ? and keyword2 is not null", (id,) )
    keyword2 = c.fetchone()
    if keyword2 is not None:
        keyword2 = keyword2[0]
    else:
        keyword2 = ""
    c.execute("select keyword3 from food where id = ? and keyword3 is not null", (id,) )
    keyword3 = c.fetchone()
    if keyword3 is not None:
        keyword3 = keyword3[0]
    else:
        keyword3 = ""
    c.execute("select image from food where id = ?", (id,) )
    image = c.fetchone()
    image = image[0]
    conn.close()
    return render_template("contents.html",category_id = category_id,category_name = category_name,catchcopy = catchcopy,name = name,keyword1 = keyword1,keyword2 = keyword2,keyword3 = keyword3,image = image )
# テーブルfoods

# テーブルart
@app.route('/art/<int:id>')
def artpage(id):
    conn = sqlite3.connect('team3.db')
    c = conn.cursor()
    c.execute("select id,category_name,catchcopy,name,keyword1 from art where id = ?", (id,) )
    contents = c.fetchone()
    category_id = contents[0]
    category_name = contents[1]
    catchcopy = contents[2]
    name = contents[3]
    keyword1 = contents[4]
    c.execute("select keyword2 from art where id = ? and keyword2 is not null", (id,) )
    keyword2 = c.fetchone()
    if keyword2 is not None:
        keyword2 = keyword2[0]
    else:
        keyword2 = ""
    c.execute("select keyword3 from art where id = ? and keyword3 is not null", (id,) )
    keyword3 = c.fetchone()
    if keyword3 is not None:
        keyword3 = keyword3[0]
    else:
        keyword3 = ""
    c.execute("select image from art where id = ?", (id,) )
    image = c.fetchone()
    image = image[0]
    conn.close()
    return render_template("contents.html",category_id = category_id,category_name = category_name,catchcopy = catchcopy,name = name,keyword1 = keyword1,keyword2 = keyword2,keyword3 = keyword3,image = image )
# テーブルart

# テーブルhistory
@app.route('/history/<int:id>')
def historypage(id):
    conn = sqlite3.connect('team3.db')
    c = conn.cursor()
    c.execute("select id,category_name,catchcopy,name,keyword1 from history where id = ?", (id,) )
    contents = c.fetchone()
    category_id = contents[0]
    category_name = contents[1]
    catchcopy = contents[2]
    name = contents[3]
    keyword1 = contents[4]
    c.execute("select keyword2 from history where id = ? and keyword2 is not null", (id,) )
    keyword2 = c.fetchone()
    if keyword2 is not None:
        keyword2 = keyword2[0]
    else:
        keyword2 = ""
    c.execute("select keyword3 from history where id = ? and keyword3 is not null", (id,) )
    keyword3 = c.fetchone()
    if keyword3 is not None:
        keyword3 = keyword3[0]
    else:
        keyword3 = ""
    c.execute("select image from history where id = ?", (id,) )
    image = c.fetchone()
    image = image[0]
    conn.close()
    return render_template("contents.html",category_id = category_id,category_name = category_name,catchcopy = catchcopy,name = name,keyword1 = keyword1,keyword2 = keyword2,keyword3 = keyword3,image = image )
# テーブルhistory


# テーブルlife
@app.route('/life/<int:id>')
def lifepage(id):
    conn = sqlite3.connect('team3.db')
    c = conn.cursor()
    c.execute("select id,category_name,catchcopy,name,keyword1 from life where id = ?", (id,) )
    contents = c.fetchone()
    category_id = contents[0]
    category_name = contents[1]
    catchcopy = contents[2]
    name = contents[3]
    keyword1 = contents[4]
    c.execute("select keyword2 from life where id = ? and keyword2 is not null", (id,) )
    keyword2 = c.fetchone()
    if keyword2 is not None:
        keyword2 = keyword2[0]
    else:
        keyword2 = ""
    c.execute("select keyword3 from life where id = ? and keyword3 is not null", (id,) )
    keyword3 = c.fetchone()
    if keyword3 is not None:
        keyword3 = keyword3[0]
    else:
        keyword3 = ""
    c.execute("select image from life where id = ?", (id,) )
    image = c.fetchone()
    image = image[0]
    conn.close()
    return render_template("contents.html",category_id = category_id,category_name = category_name,catchcopy = catchcopy,name = name,keyword1 = keyword1,keyword2 = keyword2,keyword3 = keyword3,image = image )
# テーブルlife


# テーブルmedical
@app.route('/medical/<int:id>')
def medicalpage(id):
    conn = sqlite3.connect('team3.db')
    c = conn.cursor()
    c.execute("select id,category_name,catchcopy,name,keyword1 from medical where id = ?", (id,) )
    contents = c.fetchone()
    category_id = contents[0]
    category_name = contents[1]
    catchcopy = contents[2]
    name = contents[3]
    keyword1 = contents[4]
    c.execute("select keyword2 from medical where id = ? and keyword2 is not null", (id,) )
    keyword2 = c.fetchone()
    if keyword2 is not None:
        keyword2 = keyword2[0]
    else:
        keyword2 = ""
    c.execute("select keyword3 from medical where id = ? and keyword3 is not null", (id,) )
    keyword3 = c.fetchone()
    if keyword3 is not None:
        keyword3 = keyword3[0]
    else:
        keyword3 = ""
    c.execute("select image from medical where id = ?", (id,) )
    image = c.fetchone()
    image = image[0]
    conn.close()
    return render_template("contents.html",category_id = category_id,category_name = category_name,catchcopy = catchcopy,name = name,keyword1 = keyword1,keyword2 = keyword2,keyword3 = keyword3,image = image )
# テーブルmaedical



# テーブルmusic
@app.route('/music/<int:id>')
def musicpage(id):
    conn = sqlite3.connect('team3.db')
    c = conn.cursor()
    c.execute("select id,category_name,catchcopy,name,keyword1 from music where id = ?", (id,) )
    contents = c.fetchone()
    category_id = contents[0]
    category_name = contents[1]
    catchcopy = contents[2]
    name = contents[3]
    keyword1 = contents[4]
    c.execute("select keyword2 from music where id = ? and keyword2 is not null", (id,) )
    keyword2 = c.fetchone()
    if keyword2 is not None:
        keyword2 = keyword2[0]
    else:
        keyword2 = ""
    c.execute("select keyword3 from music where id = ? and keyword3 is not null", (id,) )
    keyword3 = c.fetchone()
    if keyword3 is not None:
        keyword3 = keyword3[0]
    else:
        keyword3 = ""
    c.execute("select image from music where id = ?", (id,) )
    image = c.fetchone()
    image = image[0]
    conn.close()
    return render_template("contents.html",category_id = category_id,category_name = category_name,catchcopy = catchcopy,name = name,keyword1 = keyword1,keyword2 = keyword2,keyword3 = keyword3,image = image )
# テーブルmusic



# テーブルnature
@app.route('/nature/<int:id>')
def naturepage(id):
    conn = sqlite3.connect('team3.db')
    c = conn.cursor()
    c.execute("select id,category_name,catchcopy,name,keyword1 from nature where id = ?", (id,) )
    contents = c.fetchone()
    category_id = contents[0]
    category_name = contents[1]
    catchcopy = contents[2]
    name = contents[3]
    keyword1 = contents[4]
    c.execute("select keyword2 from nature where id = ? and keyword2 is not null", (id,) )
    keyword2 = c.fetchone()
    if keyword2 is not None:
        keyword2 = keyword2[0]
    else:
        keyword2 = ""
    c.execute("select keyword3 from nature where id = ? and keyword3 is not null", (id,) )
    keyword3 = c.fetchone()
    if keyword3 is not None:
        keyword3 = keyword3[0]
    else:
        keyword3 = ""
    c.execute("select image from nature where id = ?", (id,) )
    image = c.fetchone()
    image = image[0]
    conn.close()
    return render_template("contents.html",category_id = category_id,category_name = category_name,catchcopy = catchcopy,name = name,keyword1 = keyword1,keyword2 = keyword2,keyword3 = keyword3,image = image )
# テーブルnature



# テーブルplay
@app.route('/play/<int:id>')
def playpage(id):
    conn = sqlite3.connect('team3.db')
    c = conn.cursor()
    c.execute("select id,category_name,catchcopy,name,keyword1 from play where id = ?", (id,) )
    contents = c.fetchone()
    category_id = contents[0]
    category_name = contents[1]
    catchcopy = contents[2]
    name = contents[3]
    keyword1 = contents[4]
    c.execute("select keyword2 from play where id = ? and keyword2 is not null", (id,) )
    keyword2 = c.fetchone()
    if keyword2 is not None:
        keyword2 = keyword2[0]
    else:
        keyword2 = ""
    c.execute("select keyword3 from play where id = ? and keyword3 is not null", (id,) )
    keyword3 = c.fetchone()
    if keyword3 is not None:
        keyword3 = keyword3[0]
    else:
        keyword3 = ""
    c.execute("select image from play where id = ?", (id,) )
    image = c.fetchone()
    image = image[0]
    conn.close()
    return render_template("contents.html",category_id = category_id,category_name = category_name,catchcopy = catchcopy,name = name,keyword1 = keyword1,keyword2 = keyword2,keyword3 = keyword3,image = image )
# テーブルplay



# テーブルride
@app.route('/ride/<int:id>')
def ridepage(id):
    conn = sqlite3.connect('team3.db')
    c = conn.cursor()
    c.execute("select id,category_name,catchcopy,name,keyword1 from ride where id = ?", (id,) )
    contents = c.fetchone()
    category_id = contents[0]
    category_name = contents[1]
    catchcopy = contents[2]
    name = contents[3]
    keyword1 = contents[4]
    c.execute("select keyword2 from ride where id = ? and keyword2 is not null", (id,) )
    keyword2 = c.fetchone()
    if keyword2 is not None:
        keyword2 = keyword2[0]
    else:
        keyword2 = ""
    c.execute("select keyword3 from ride where id = ? and keyword3 is not null", (id,) )
    keyword3 = c.fetchone()
    if keyword3 is not None:
        keyword3 = keyword3[0]
    else:
        keyword3 = ""
    c.execute("select image from ride where id = ?", (id,) )
    image = c.fetchone()
    image = image[0]
    conn.close()
    return render_template("contents.html",category_id = category_id,category_name = category_name,catchcopy = catchcopy,name = name,keyword1 = keyword1,keyword2 = keyword2,keyword3 = keyword3,image = image )
# テーブルride



# テーブルsport
@app.route('/sports/<int:id>')
def sportpage(id):
    conn = sqlite3.connect('team3.db')
    c = conn.cursor()
    c.execute("select id,category_name,catchcopy,name,keyword1 from sports where id = ?", (id,) )
    contents = c.fetchone()
    category_id = contents[0]
    category_name = contents[1]
    catchcopy = contents[2]
    name = contents[3]
    keyword1 = contents[4]
    c.execute("select keyword2 from sports where id = ? and keyword2 is not null", (id,) )
    keyword2 = c.fetchone()
    if keyword2 is not None:
        keyword2 = keyword2[0]
    else:
        keyword2 = ""
    c.execute("select keyword3 from sports where id = ? and keyword3 is not null", (id,) )
    keyword3 = c.fetchone()
    if keyword3 is not None:
        keyword3 = keyword3[0]
    else:
        keyword3 = ""
    c.execute("select image from sports where id = ?", (id,) )
    image = c.fetchone()
    image = image[0]
    conn.close()
    return render_template("contents.html",category_id = category_id,category_name = category_name,catchcopy = catchcopy,name = name,keyword1 = keyword1,keyword2 = keyword2,keyword3 = keyword3,image = image )
# テーブルsport



# テーブルtrip
@app.route('/trip/<int:id>')
def trippage(id):
    conn = sqlite3.connect('team3.db')
    c = conn.cursor()
    c.execute("select id,category_name,catchcopy,name,keyword1 from trip where id = ?", (id,) )
    contents = c.fetchone()
    category_id = contents[0]
    category_name = contents[1]
    catchcopy = contents[2]
    name = contents[3]
    keyword1 = contents[4]
    c.execute("select keyword2 from trip where id = ? and keyword2 is not null", (id,) )
    keyword2 = c.fetchone()
    if keyword2 is not None:
        keyword2 = keyword2[0]
    else:
        keyword2 = ""
    c.execute("select keyword3 from trip where id = ? and keyword3 is not null", (id,) )
    keyword3 = c.fetchone()
    if keyword3 is not None:
        keyword3 = keyword3[0]
    else:
        keyword3 = ""
    c.execute("select image from trip where id = ?", (id,) )
    image = c.fetchone()
    image = image[0]
    conn.close()
    return render_template("contents.html",category_id = category_id,category_name = category_name,catchcopy = catchcopy,name = name,keyword1 = keyword1,keyword2 = keyword2,keyword3 = keyword3,image = image )
# テーブルtrip


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
    return "ページがないです....ごめんね・・・・"


if __name__ == "__main__":
    # Flaskが持っている開発用サーバーを実行します
    app.run(debug=True)