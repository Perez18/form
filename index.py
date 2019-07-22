#Importar
from flask import Flask, render_template,request,redirect,url_for,flash
from flask_mysqldb import MySQL


#configuracion mysql
app=Flask(__name__)
app.config['MYSQL_HOST']= 'localhost'
app.config['MYSQL_USER']='root'  
app.config['MYSQL_PASSWORD']=''
app.config['MYSQL_DB']='schema'
mysql = MySQL(app)

#setting
app.secret_key ='mysecretkey'

#Routeo
@app.route('/')
def home ():
   cur=mysql.connection.cursor()
   cur.execute('SELECT * FROM usuarios')
   data=cur.fetchall()
   return render_template('home.html',usuarios=data)



@app.route('/add',methods=['POST'])
def add():
    if request.method == 'POST':
       name = request.form['user']
       password = request.form['pass']
       correo = request.form['correo']
       cur= mysql.connection.cursor() # realiza la conexion 
    cur.execute('INSERT INTO usuarios(usuario,contraseña,correo)VALUES(%s,% s,%s)',(name,password,correo)) #se indica los datos que se insertaran
    mysql.connection.commit() #se realiza la coneccion y se inserta los datos
    flash('Contacto añadido a la base de datos')
    return redirect(url_for('home'))

@app.route('/update/<id>', methods=['POST'])
def update(id):
    if request.method=='POST':
        name = request.form['user']
        password=request.form['pass']
        correo = request.form['correo']
        cur=mysql.connection.cursor()
        cur.execute("""
        UPDATE usuarios
        SET usuario = %s,
            contraseña = %s,
            correo = %s
        WHERE id= %s
        """,(name,password,correo,id))
        mysql.connection.commit()
        flash('guardado correctamente')
        return redirect(url_for('home'))
@app.route('/edit/<id>')
def get_edit(id):
    cur=mysql.connection.cursor()
    cur.execute('SELECT * FROM  usuarios WHERE id= %s',(id))
    mysql.connection.commit()
    data=cur.fetchall()
    print(data[0])
    return render_template('editar.html', usuario=data[0])

@app.route('/delete/<string:id>')
def delete(id):
    cur=mysql.connection.cursor()
    cur.execute('DELETE FROM usuarios WHERE id= {0}'.format(id))
    mysql.connection.commit()
    flash('contacto eliminado')
    return redirect(url_for('home'))


#validacion
if __name__ == "__main__":
          app.run(debug=True)