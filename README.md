## Descripción General

Este proyecto consiste en una aplicación para la gestión de estudiantes y sus calificaciones, utilizando la biblioteca `PyQt6` para la creación de la interfaz gráfica de usuario (GUI). La aplicación está dividida en dos módulos principales:

1. **registroEstudiantes.py**: Maneja el registro de estudiantes y almacena la información en un archivo CSV.
2. **menuOpciones.py**: Permite ingresar y gestionar las calificaciones de los estudiantes previamente registrados.

## Archivos

### 1. `registroEstudiantes.py`

Este archivo contiene la clase `RegistroEstudiantes`, que se encarga de la gestión del registro de estudiantes. Aquí se describe su funcionamiento:

- **Librerías Utilizadas**:
  - `sys`: Para la gestión de argumentos y control del flujo de la aplicación.
  - `pandas` y `numpy`: Para la gestión y manipulación de datos.
  - `PyQt6.QtWidgets`: Para la creación de la interfaz gráfica de usuario (GUI).

- **Clases y Métodos**:
  - **Clase `RegistroEstudiantes(QWidget)`**: Hereda de `QWidget` y maneja la ventana principal de registro.
    - `__init__(self)`: Constructor de la clase. Inicializa la interfaz y las listas que almacenarán los datos de los estudiantes.
    - `initUI(self)`: Configura la interfaz de usuario (formularios, botones) para ingresar los datos de los estudiantes.
    - `registrarAlumno(self)`: Recoge los datos introducidos por el usuario y los almacena en listas. Muestra un mensaje de confirmación si el registro es exitoso.
    - `finalizarRegistro(self)`: Guarda los datos de los estudiantes registrados en un archivo CSV llamado `estudiantes.csv` y cierra la aplicación.

### 2. `menuOpciones.py`

Este archivo contiene la clase `RegistroCalificaciones`, que permite gestionar las calificaciones de los estudiantes registrados. Aquí se describe su funcionamiento:

- **Librerías Utilizadas**:
  - `sys`: Para la gestión de argumentos y control del flujo de la aplicación.
  - `os`: Para la verificación de la existencia de archivos.
  - `pandas`: Para la gestión y manipulación de datos.
  - `PyQt6.QtWidgets`: Para la creación de la interfaz gráfica de usuario (GUI).

- **Clases y Métodos**:
  - **Clase `RegistroCalificaciones(QWidget)`**: Hereda de `QWidget` y maneja la ventana principal de gestión de calificaciones.
    - `__init__(self)`: Constructor de la clase. Inicializa la interfaz y carga la base de datos de estudiantes desde el archivo `estudiantes.csv`.
    - `cargar_base_estudiantes(self)`: Carga el archivo CSV con los datos de los estudiantes. Si no se encuentra el archivo, muestra un mensaje de error y cierra la aplicación.
    - `initUI(self)`: Configura la interfaz de usuario (menús, formularios) para gestionar las calificaciones.
    - `actualizarEstudiantes(self)`: Actualiza la lista de estudiantes según la materia seleccionada.
    - `calificar(self)`: Registra la calificación de un estudiante para una materia específica y la guarda en un DataFrame.
    - `guardarCalificaciones(self)`: Guarda las calificaciones en un archivo CSV separado por cada materia.
    - `verCalificaciones(self)`: Muestra las calificaciones guardadas para la materia seleccionada.
    - `modificarCalificaciones(self)`: Función aún en desarrollo para modificar las calificaciones existentes.
    - `enviarCalificaciones(self)`: Simula el envío de calificaciones (funcionalidad aún en desarrollo).

## Requisitos

Para ejecutar estos archivos, necesitas tener instalado:
- Python 3.x
- PyQt6
- pandas
- numpy

Puedes instalar las dependencias necesarias usando pip:

pip install PyQt6 pandas numpy

## Ejecución

1. Ejecuta primero `registroEstudiantes.py` para registrar los estudiantes. Asegúrate de que el archivo `estudiantes.csv` se crea correctamente.
   
   python registroEstudiantes.py
   
3. Luego, ejecuta menuOpciones.py para gestionar las calificaciones de los estudiantes.

   python menuOpciones.py

## Notas

- El archivo `estudiantes.csv` es crucial para que `menuOpciones.py` funcione correctamente, ya que contiene la lista de estudiantes registrados.
- La funcionalidad para modificar y enviar calificaciones está en desarrollo y podría no estar completamente operativa.

