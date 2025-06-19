from app.bookings import check_availability

def test_check_availability():
    bookings = [
        {"sala": "A", "hora": "10:00"},
        {"sala": "A", "hora": "11:00"}
    ]
    
    new_bookings = {"sala": "A", "hora": "12:00"}
    assert check_availability(bookings, new_bookings) == True
    
def test_room_not_available():
    bookings = [
        {"sala": "A", "hora": "10:00"},
        {"sala": "A", "hora": "11:00"}
    ]
    
    new_bookings = {"sala": "A", "hora": "11:00"}
    assert check_availability(bookings, new_bookings) == False