def check_availability(bookings, new_booking):
    for r in bookings:
        if r["sala"] == new_booking["sala"] and r["hora"] == new_booking["hora"]:
            return False
    return True