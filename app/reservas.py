def verificar_disponibilidad(reservas, nueva):
    for r in reservas:
        if r["sala"] == nueva["sala"] and r["hora"] == nueva["hora"]:
            return False
    return True