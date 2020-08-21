# Flaskからインポートしてflaskを使えるようにする
from flask import Flask, render_template , request ,redirect,session
import sqlite3

# appという名前でFlaskあぷりをつくっていくよ
app = Flask(__name__)

app.secret_key = 'sunabaco_yatsusiro'

# TOPページ
@app.route("/index")
def helloWorld():
    return render_template("index.html")

# ページtop
@app.route('/top/')
def toppage():
    conn = sqlite3.connect('team3.db')
    c = conn.cursor()
    c.execute("select id,catchcopy from foods")
    foods_list = []
    for row in c.fetchall():
        foods_list.append({"id":row[0],"catchcopy":row[1]})
    c.execute("select id,catchcopy from art")
    art_list = []
    for row in c.fetchall():
        art_list.append({"id":row[0],"catchcopy":row[1]})
    c.execute("select id,catchcopy from fashion")
    fashion_list = []
    for row in c.fetchall():
        fashion_list.append({"id":row[0],"catchcopy":row[1]})
    c.execute("select id,catchcopy from history")
    history_list = []
    for row in c.fetchall():
        history_list.append({"id":row[0],"catchcopy":row[1]})
    c.execute("select id,catchcopy from life")
    life_list = []
    for row in c.fetchall():
        life_list.append({"id":row[0],"catchcopy":row[1]})
    c.execute("select id,catchcopy from medical")
    medical_list = []
    for row in c.fetchall():
        medical_list.append({"id":row[0],"catchcopy":row[1]})
    c.execute("select id,catchcopy from music")
    music_list = []
    for row in c.fetchall():
        music_list.append({"id":row[0],"catchcopy":row[1]})
    c.execute("select id,catchcopy from nature")
    nature_list = []
    for row in c.fetchall():
        nature_list.append({"id":row[0],"catchcopy":row[1]})
    c.execute("select id,catchcopy from play")
    play_list = []
    for row in c.fetchall():
        play_list.append({"id":row[0],"catchcopy":row[1]})
    c.execute("select id,catchcopy from ride")
    ride_list = []
    for row in c.fetchall():
        ride_list.append({"id":row[0],"catchcopy":row[1]})
    c.execute("select id,catchcopy from sport")
    sport_list = []
    for row in c.fetchall():
        sport_list.append({"id":row[0],"catchcopy":row[1]})
    c.execute("select id,catchcopy from trip")
    trip_list = []
    for row in c.fetchall():
        trip_list.append({"id":row[0],"catchcopy":row[1]})
    conn.close()
    return render_template("top.html",foods_list = foods_list,art_list = art_list,fashion_list = fashion_list,history_list = history_list,life_list = life_list,medical_list = medical_list,music_list = music_list,nature_list = nature_list,play_list = play_list,ride_list = ride_list,sport_list = sport_list,trip_list = trip_list)
# ページtop

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

# テーブルfoods
@app.route('/foods/<int:id>')
def foodspage(id):
    conn = sqlite3.connect('team3.db')
    c = conn.cursor()
    c.execute("select id,category_name,catchcopy,name,keyword1 from foods where id = ?", (id,) )
    contents = c.fetchone()
    category_id = contents[0]
    category_name = contents[1]
    catchcopy = contents[2]
    name = contents[3]
    keyword1 = contents[4]
    c.execute("select keyword2 from foods where id = ? and keyword2 is not null", (id,) )
    keyword2 = c.fetchone()
    if keyword2 is not None:
        keyword2 = keyword2[0]
    else:
        keyword2 = ""
    c.execute("select keyword3 from foods where id = ? and keyword3 is not null", (id,) )
    keyword3 = c.fetchone()
    if keyword3 is not None:
        keyword3 = keyword3[0]
    else:
        keyword3 = ""
    c.execute("select image from foods where id = ?", (id,) )
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
@app.route('/sport/<int:id>')
def sportpage(id):
    conn = sqlite3.connect('team3.db')
    c = conn.cursor()
    c.execute("select id,category_name,catchcopy,name,keyword1 from sport where id = ?", (id,) )
    contents = c.fetchone()
    category_id = contents[0]
    category_name = contents[1]
    catchcopy = contents[2]
    name = contents[3]
    keyword1 = contents[4]
    c.execute("select keyword2 from sport where id = ? and keyword2 is not null", (id,) )
    keyword2 = c.fetchone()
    if keyword2 is not None:
        keyword2 = keyword2[0]
    else:
        keyword2 = ""
    c.execute("select keyword3 from sport where id = ? and keyword3 is not null", (id,) )
    keyword3 = c.fetchone()
    if keyword3 is not None:
        keyword3 = keyword3[0]
    else:
        keyword3 = ""
    c.execute("select image from sport where id = ?", (id,) )
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






if __name__ == "__main__":
    # Flaskが持っている開発用サーバーを実行します
    app.run(debug=True)