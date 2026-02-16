def validar_nombre(nombre):
    if not nombre.replace(" ", "").isalpha():
        raise ValueError("El nombre solo debe contener letras.")
    return nombre

def validar_email(email):
    if "@" not in email or "." not in email:
        raise ValueError("El formato de correo electrónico no es válido (ej: usuario@mail.com).")
    return email

def validar_telefono(telefono):
    if not telefono.isdigit():
        raise ValueError("El teléfono solo debe contener números.")
    return telefono

def validar_monto(monto_str):
    try:
        monto = float(monto_str)
        if monto < 0:
            raise ValueError("El monto no puede ser negativo.")
        return monto
    except ValueError:
        raise ValueError("El monto debe ser un número válido.")
    

def validar_descuento(descuento_str):
    try:
        desc = float(descuento_str)
        if not (0 <= desc <= 0.9):
            raise ValueError("El descuento debe estar entre 0.0 y 0.9 (0% a 90%).")
        return desc
    except ValueError as e:
        if "could not convert string to float" in str(e):
            raise ValueError("El descuento debe ser un número decimal (ej: 0.15).")
        raise e