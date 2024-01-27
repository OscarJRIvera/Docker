from flask import Flask, request, jsonify
import mysql.connector

app = Flask(__name__)

db_config = {
    'host': 'localhost', 
    'user': 'root',
    'password': '1234567',
    'database': 'Virtual',
    'port':3304
}

# Conexión a la base de datos
db = mysql.connector.connect(**db_config)
cursor = db.cursor()

# Rutas Crud utilizados despues en postman
@app.route('/api/get', methods=['GET'])
def get_data():
    cursor.execute('SELECT * FROM nombres;')
    data = cursor.fetchall()
    return jsonify(data)
@app.route('/api/post', methods=['POST'])
def create_data():
    nombres=request.form.get('nombres')
    print(f'data re: {nombres}')
    cursor.execute('INSERT INTO nombres (nombres) VALUES (%s);', (nombres,))
    db.commit()
    return 'Insertado!', 201

@app.route('/api/put/<int:id>', methods=['PUT'])
def update_data(id):
    nombre_nuevo = request.form.get('nombres')
    cursor.execute('UPDATE nombres SET nombres = %s WHERE idnombres = %s;', (nombre_nuevo, id))
    db.commit()
    return 'Actualizado'

@app.route('/api/delete/<int:id>', methods=['DELETE'])
def delete_data(id):
    cursor.execute('DELETE FROM nombres WHERE idnombres = %s;', (id,))
    db.commit()
    return 'Eliminado!'


if __name__ == '__main__':
    app.run(debug=True, port=3034)