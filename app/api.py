from flask import Flask, request, jsonify
from app.bookings import check_availability

app = Flask(__name__)
bookings = []

@app.route('/reservar', methods=['POST'])
def book():
    data = request.get_json()
    is_available = check_availability(bookings, data)
    
    if is_available:
        bookings.append(data)
        return jsonify({"mensaje": "Reserva con éxito"}), 201
    else:
        return jsonify({"mensaje": "Sala no disponible"}), 409