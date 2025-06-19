from flask import Flask, request, jsonify
from app.reservas import verificar_disponibilidad

app = Flask(__name__)
reservas = []

@app.route('/reservar', methods=['POST'])
def reservar():
    data = request.get_json()
    disponible = verificar_disponibilidad(reservas, data)
    
    if disponible:
        reservas.append(data)
        return jsonify({"mensaje": "Reserva con éxito"}), 201
    else:
        return jsonify({"mensaje": "Sala no disponible"}), 409