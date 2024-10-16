from flask import Flask
from flask import render_template, request, redirect

app = Flask(__name__)

@app.route('/')
def inicio():
    return render_template('website/index.html')

@app.route('/integrantes')
def libros():
    return render_template('website/integrantes.html')

@app.route('/nosotros')
def nosotros():
    return render_template('website/nosotros.html')

@app.route('/admin/')
def admin_index():
    return render_template('admin/index.html')

@app.route('/admin/login')
def admin_login():
    return render_template('admin/login.html')

@app.route('/admin/integrantes')
def admin_integrantes():
    from db.sql import ee97per091_sql
    sql = "SELECT * FROM ee97per091"
    integrantes = ee97per091_sql(sql, None, 'Q')
    return render_template('admin/integrantes.html', integrantes=integrantes)

@app.route('/admin/integrantes/guardar', methods=['POST'])
def admin_integrantes_guardar():
    sql = 'INSERT INTO ee97per001 (DNI, NOMBRE1, NOMBRE2, APELLIDO1, APELLIDO2, TELEFONO, IMAGEN) VALUES (?, ?, ?, ?, ?, ?, ?);'
    _DNI       = request.form['txtDNI']
    _nombre1   = request.form['txtNombre1']
    _nombre2   = request.form['txtNombre2']
    _apellido1 = request.form['txtApellido1']
    _apellido2 = request.form['txtApellido2']
    _telefono  = request.form['txtTelefono']
    _Archivo   = request.files['txtImg']
    parm = (_DNI.strip(),_nombre1.strip(), _nombre2.strip(), _apellido1.strip(), _apellido2.strip(), _telefono.strip(), _Archivo.filename.strip())
    from db.sql import ee97per001_sql
    ee97per001_sql(sql,parm,'I')
    return redirect('/admin/integrantes')

@app.route('/admin/integrantes/borrar', methods=['POST'])
def admin_integrantes_borrar():
    sql = "DELETE FROM ee97per091 WHERE COD = ?"
    _COD = request.form['txtID']
    parm =  (_COD,)
    from db.sql import ee97per091_sql
    ee97per091_sql(sql,parm,'D')
    return redirect('/admin/integrantes')





if __name__ == "__main__":
    app.run(debug=False)