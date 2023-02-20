from flask import Flask, render_template, request
import mysql.connector

app = Flask(__name__)


@app.route('/')
def stud():
    return render_template('test.html')


@app.route('/result', methods=['POST', 'GET'])
def user():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="marks"
    )
    mycursor = mydb.cursor()
    if request.method == 'POST':
        result = request.form
        name = result['Name']
        mycursor.execute("select name,math,phy,chem,Total from students where name='" + name + "'")
        database = mycursor.fetchone()
        print(database)
        mydb.commit()
        mycursor.close()
        return render_template("webpage1.html", database=database)


app.run(debug=True)