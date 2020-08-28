from flask import Blueprint, session, render_template,request,redirect
import sqlite3

app = Blueprint('func3',__name__)

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