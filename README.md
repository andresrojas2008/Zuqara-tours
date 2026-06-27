# Zuqara Tours

Aplicativo web para la planificación, recomendación y reserva de tours turísticos.

---

#  Integrantes del proyecto

| Integrante | Rol | Responsabilidades |
|------------|-----|-------------------|
| Sergio Enrique González Salinas | Líder del proyecto | Coordinar el equipo, tomar decisiones técnicas, supervisar avances y apoyar el desarrollo. |
| Andrés Felipe Rojas Pagote | Backend y Documentación | Desarrollo del backend, base de datos, documentación técnica, control de cambios y evidencias. |
| Daniel Felipe Rodríguez Henao | Frontend y Análisis | Desarrollo de interfaces, diagramas, historias de usuario y documentación funcional. |

---

#  Descripción del proyecto

Zuqara Tours es un aplicativo web diseñado para centralizar la información de tours turísticos en una única plataforma.

Su principal innovación consiste en recomendar automáticamente los tours más adecuados para cada usuario teniendo en cuenta características como:

- Edad
- Movilidad
- Viaje con niños
- Viaje con adultos mayores
- Nivel de dificultad física
- Preferencias de comodidad
- Accesibilidad
- Seguridad

De esta manera los usuarios pueden reservar experiencias realmente compatibles con sus necesidades.

---

#  Problema que resuelve

Actualmente muchas plataformas de turismo únicamente permiten visualizar y reservar paquetes turísticos.

Sin embargo:

- No consideran las condiciones físicas del viajero.
- No indican el nivel de accesibilidad.
- No ayudan a seleccionar el tour más adecuado.
- No apoyan suficientemente a pequeños operadores turísticos.
- Pueden generar malas experiencias por incompatibilidad entre el usuario y el tour.

---

#  Objetivo General

Construir un sistema de información web que mejore los procesos de recomendación, accesibilidad y reserva de tours turísticos mediante un sistema inteligente basado en el perfil del usuario.

---

#  Usuarios del sistema

## Turista

- Registrarse
- Iniciar sesión
- Buscar tours
- Recibir recomendaciones
- Reservar tours
- Realizar pagos
- Calificar experiencias
- Editar perfil
- Comunicarse con operadores

---

## Operador Turístico

- Crear empresa
- Publicar tours
- Modificar tours
- Gestionar reservas
- Responder comentarios
- Administrar su perfil
- Gestionar suscripción

---

## Administrador

- Gestionar usuarios
- Gestionar operadores turísticos
- Supervisar publicaciones
- Administrar pagos
- Configurar el sistema
- Generar reportes

---

#  Funcionalidades principales

- Registro e inicio de sesión
- Gestión de perfiles
- Publicación de tours
- Recomendación inteligente según perfil
- Sistema de accesibilidad
- Reserva de tours
- Pasarela de pagos
- Sistema de calificaciones
- Comentarios y opiniones
- Comunicación entre turistas y operadores

---

#  Características diferenciadoras

- Recomendación personalizada.
- Compatibilidad entre usuario y tour.
- Información de accesibilidad.
- Inclusión de personas con movilidad reducida.
- Apoyo a pequeños operadores turísticos.
- Mejor experiencia para el viajero.

---

#  Arquitectura

Arquitectura Inicial Elegida: Arquitectura MVC (Modelo - Vista - Controlador)

¿Por qué?

Para el desarrollo de Zuqara Tours se eligió la arquitectura MVC (Modelo - Vista - Controlador) porque permite organizar el sistema de forma clara y estructurada, separando las responsabilidades de cada componente:

Modelo: administra la información relacionada con los usuarios, paquetes turísticos, reservas y demás datos del sistema.
Vista: presenta la interfaz gráfica con la que interactúan los clientes y administradores de Zuqara Tours.
Controlador: procesa las solicitudes de los usuarios, coordina la comunicación entre la Vista y el Modelo, y gestiona la lógica de negocio.

Esta arquitectura facilita el mantenimiento, la escalabilidad y el desarrollo colaborativo del proyecto, permitiendo que Zuqara Tours pueda incorporar nuevas funcionalidades, como métodos de pago, promociones o nuevos servicios turísticos, sin afectar el funcionamiento de los demás módulos del sistema.

---

#  Metodología

## Scrum

Se utiliza Scrum debido a que permite:

- Desarrollo incremental.
- Entregas continuas.
- Adaptación a cambios.
- Organización mediante Sprints.
- Trabajo colaborativo.
teniendo en uenta esto facilita la comunicacion y mejora la organizacion de trabajos del equipo de proyecto

---

#  Tecnologías

## Backend
-Python
-Flask
-Flask Blueprints (para la organización de los controladores)
## Frontend
-HTML5
-Jinja2 (motor de plantillas de Flask)
-CSS3
-JavaScript
## Base de datos
-PostgreSQL
-SQLAlchemy ORM
## APIs y servicios externos
-API REST
-Pasarela de pagos: PSE, Tarjeta y Wompi
-Mapas: Google Maps u OpenStreetMap
-Notificaciones: Email y SMS
## Control de versiones
-Git
-GitHub
---

#  Alcance

El sistema permitirá:

- Registro de usuarios
- Registro de empresas
- Publicación de tours
- Recomendaciones inteligentes
- Gestión de reservas
- Pagos
- Opiniones
- Calificaciones

No contempla actividades fuera del proceso de gestión turística definido en el proyecto.

---

#  Estado del proyecto

 En desarrollo

Actualmente se encuentra en fase de construcción del sistema conforme al anteproyecto y a la especificación de requerimientos.

---

#  Proyecto académico

**Tecnólogo en Análisis y Desarrollo de Software**

Servicio Nacional de Aprendizaje - SENA

Ficha: **3407179**

---

## Autores

- Sergio Enrique González Salinas
- Andrés Felipe Rojas Pagote
- Daniel Felipe Rodríguez Henao



<img width="1112" height="762" alt="Tours Zuqara" src="https://github.com/user-attachments/assets/1a3c4b2f-aef6-4de6-9169-895ca8307c61" />
