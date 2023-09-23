from flask import Flask, jsonify, request #Del paquete flask importo una clase yel paquete que permite convertir obj de py a json
from markupsafe import escape

app = Flask(__name__)   #Creamos constructor clase

@app.route('/')
def index():
    return 'Index'

@app.route('/ping')
def ping():
    return jsonify({"message": "pong"})

@app.route('/usuarios/<string:nombre>')
def usuario_by_name(nombre):
    return jsonify({"name": nombre})

@app.route('/usuarios/<int:id>')
def usuario_by_id(id):
    return jsonify({"id": id})

@app.route('/<path:nombre>')
def no_hacer(nombre):
    return escape(nombre)

# GET de todos los "recursos" (clientes/facturas/lo que sea)
@app.route('/recurso', methods = ['GET'])
def get_recursos():
    return jsonify({"data": "lista de todos los items de este recurso"})

# POST nuevo "recurso"
@app.route('/recurso', methods = ['POST'])
def post_recurso():
    print(request.get_json())
    body = request.get_json()  #Guardo el request en una variable
    name = body["name"]
    modelo = body["modelo"]
    # Insertar en la base de datos
    return jsonify({"recurso": {
        "name": name,
        "modelo": modelo    
        }})

# GET un "recurso" a través de su ID
@app.route('/recurso/<int:id>', methods = ['GET'])
def get_recurso_by_id(id):
    # buscar en la base de datos un registro con ese id
    return jsonify({"recurso": {
        "name": "nombre correspondiente a ese id",
        "modelo": "modelo correspondiente a ese id"  
        }})


if __name__ == '__main__':
    app.run(debug= True, port=5000) #Utilizamos un método