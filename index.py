#Importar
from flask import Flask, render_template,request,redirect,url_for,flash
from flask_mysqldb import MySQL


#configuracion
app=Flask(__name__)
app.config['MYSQL_HOST']= 'localhost'
app.config['MYSQL_USER']='root'  
app.config['MYSQL_PASSWORD']=''
app.config['MYSQL_DB']='schema'
mysql = MySQL(app)

#Routeo
@app.route('/')
def home ():
    return render_template("home.html")

@app.route('/add',methods=['POST'])
def add():
    if request.method == 'POST':
       name = request.form['user']
       password = request.form['pass']
       correo = request.form['correo']
       cur= mysql.connection.cursor() # realiza la conexion 
    cur.execute('INSERT INTO usuarios(usuario,contraseña,correo)VALUES(%s,%s,%s)',(name,password,correo)) #se indica los datos que se insertaran
    mysql.connection.commit() #se realiza la coneccion y se inserta los datos
    flash('Añadido satisfactoriamente')
    return redirect(url_for('home'))

#validacion
if __name__ == "__main__":
          app.run(debug=True)