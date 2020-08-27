from flask import Blueprint, session, render_template,request,redirect
import sqlite3

app = Blueprint('func4',__name__)

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
