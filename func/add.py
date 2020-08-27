from flask import Blueprint, session, render_template,request,redirect
import sqlite3

app = Blueprint('func',__name__)

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










