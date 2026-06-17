from usuario import usuario
from operador_turistico import operadorturistico
from datetime import datetime

def crear_usuario(nombre, correo, fecha_registro):
    try:
        nuevo_usuario = usuario(nombre, correo, fecha_registro)
        nuevo_usuario.validar() 
        return nuevo_usuario
    except ValueError as e:
        print(f"Error al crear usuario: {e}")
        return None

    
def crear_operador(nombre, correo, empresa):
    try:
        operador = operadorturistico(nombre, correo, empresa)
        operador.validar()
        return operador
    except ValueError as e:
        print(f"error al crear al operador: {e}")
        return None


def validar_calificacion(valor):
    try:
        valor_int = int(valor)
        if valor_int < 1 or valor_int > 5:
            raise ValueError(f"La calificacion debe estar entre 1 y 5, se recibio: {valor_int}")
        return valor_int
    except ValueError as e:
        print(f"Error en calificacion: {e}")
        return None
 
 
def validar_fechas_itinerario(fecha_inicio, fecha_fin):
    try:
        inicio = datetime.strptime(fecha_inicio, "%Y-%m-%d")
        fin    = datetime.strptime(fecha_fin,    "%Y-%m-%d")
        if inicio >= fin:
            raise ValueError("La fecha de inicio debe ser anterior a la fecha de fin.")
        return True
    except ValueError as e:
        print(f"Error en fechas: {e}")
        return False
 
 
def actualizar_nombre_usuario(usuario, nuevo_nombre):
    try:
        usuario.set_nombre(nuevo_nombre)
        print(f"Nombre actualizado correctamente: {usuario.get_nombre()}")
        return True
    except ValueError as e:
        print(f"Error al actualizar nombre: {e}")
        return False
 
 
def actualizar_correo_usuario(usuario, nuevo_correo):
    try:
        usuario.set_correo(nuevo_correo)
        print(f"Correo actualizado correctamente: {usuario.get_correo()}")
        return True
    except ValueError as e:
        print(f"Error al actualizar correo: {e}")
        return False