from usuario import usuario
from operador_turistico import operadorturistico
from validaciones import (
    crear_usuario,
    crear_operador,
    validar_calificacion,
    validar_fechas_itinerario,
    actualizar_nombre_usuario,
    actualizar_correo_usuario,
)


print("  USUARIOS  \n")
 

print(" usuario valido ")
u = crear_usuario("Sergio Gonzalez", "sergio@zuqara.com", "2026-06-01")
if u:
    print(u.describir())
 

print("\n Creando usuario con correo invalido ")
u2 = crear_usuario("Daniel", "correo-sin-arroba", "2026-06-01")

 

print("\n Creando operador valido ")
o = crear_operador("Carlos", "carlos@tours.com", "Colombia Tours")
if o:
    print(o.describir())
 

print("\n Creando operador sin empresa ")
o2 = crear_operador("Pedro", "pedro@ops.com", "")
 
print("\n Validando calificaciones ")
print(validar_calificacion("4"))    
print(validar_calificacion("8"))     
print(validar_calificacion("abc"))   


print("\n Validando fechas de itinerario ")
print(validar_fechas_itinerario("2026-07-01", "2026-07-10"))  
print(validar_fechas_itinerario("2026-07-10", "2026-07-01"))  
print(validar_fechas_itinerario("2026-13-01", "2026-07-10"))  
 

print("\n Actualizando datos de usuario ")
if u:
    actualizar_nombre_usuario(u, "Sergio G.")   
    actualizar_nombre_usuario(u, "")            
    actualizar_correo_usuario(u, "nuevo@mail.com")  
    actualizar_correo_usuario(u, "sinArroba")   