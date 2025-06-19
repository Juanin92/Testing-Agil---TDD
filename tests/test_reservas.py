from app.reservas import verificar_disponibilidad

def test_sala_disponible():
    reservas = [
        {"sala": "A", "hora": "10:00"},
        {"sala": "A", "hora": "11:00"}
    ]
    
    nueva = {"sala": "A", "hora": "12:00"}
    assert verificar_disponibilidad(reservas, nueva) == True
    
def test_sala_no_disponible():
    reservas = [
        {"sala": "A", "hora": "10:00"},
        {"sala": "A", "hora": "11:00"}
    ]
    
    nueva = {"sala": "A", "hora": "11:00"}
    assert verificar_disponibilidad(reservas, nueva) == False