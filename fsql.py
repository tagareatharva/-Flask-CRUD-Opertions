from flask import Flask, render_template ,request
import mysql.connector
app =Flask(__name__)
@app.route('/')
def student():
    return render_template('index1.html')

@app.route('/results',methods=['POST','GET'])
def result():
    mydb=mysql.connector.connect(
        host = "localhost",
        user="root",
        password="",
        database = "marks"
    )
    mycursor=mydb.cursor()
    if request.method =='POST':
        result = request.form.to_dict()
        name=result['Name']
        mat =int(request.form['Mathematics'])
        phy =int(request.form['physics'])
        che =int(request.form['chemistry'])
        s=str(mat+phy+che)
        result['Total']=s
        mycursor.execute("insert into students (name,math,phy,chem,Total)values(%s,%s,%s,%s,%s)",(name,mat,phy,che,s))
        mydb.commit()
        mycursor.close()
        return 'success'


    return render_template("index1.html")

app.run(debug =True)