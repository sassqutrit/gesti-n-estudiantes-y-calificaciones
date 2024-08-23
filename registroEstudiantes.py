import sys
import pandas as pd
import numpy as np
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLineEdit
from PyQt6.QtWidgets import QLabel, QFormLayout, QMessageBox


class RegistroEstudiantes(QWidget):
    def __init__(self):
        super().__init__()
        # Inicializa la interfaz gráfica del usuario
        self.initUI()
        # Creación de variables de tipo listas vacías de uso general
        self.nombre = []
        self.apellido = []
        self.materia = []
        
    def initUI(self):
        # Título de la ventana
        self.setWindowTitle('Registro de Estudiantes')
        
        # Configuración del formulario para ingresar los datos de los estudiantes
        layout = QFormLayout()
        self.alumnos_input = QLineEdit(self)
        layout.addRow('Cantidad de Alumnos:', self.alumnos_input)
        
        self.nombre_input = QLineEdit(self)
        layout.addRow('Nombre:', self.nombre_input)
        
        self.apellido_input = QLineEdit(self)
        layout.addRow('Apellido:', self.apellido_input)
        
        self.materias_input = QLineEdit(self)
        layout.addRow('Materias (Separadas por coma):', self.materias_input)
        
        # Botón para registrar a un alumno
        self.registrar_btn = QPushButton('Registrar Alumno', self)
        self.registrar_btn.clicked.connect(self.registrarAlumno)
        layout.addWidget(self.registrar_btn)
        
        # Botón para finalizar el registro y guardar los datos
        self.finalizar_btn = QPushButton('Finalizar Registro', self)
        self.finalizar_btn.clicked.connect(self.finalizarRegistro)
        layout.addWidget(self.finalizar_btn)
        
        self.setLayout(layout)
        
    def registrarAlumno(self):
        # Obtiene los datos del estudiante desde los campos de entrada
        nombre = self.nombre_input.text()
        apellido = self.apellido_input.text()
        materias = self.materias_input.text().split(',')
        # Verifica si se han llenado todos los campos antes de registrar al estudiante
        if nombre and apellido and materias:
            self.nombre.append(nombre)
            self.apellido.append(apellido)
            self.materia.append(materias)
            # Manda un mensaje en caja de texto sobre el registro exitoso de cada alumno registrado
            QMessageBox.information(self, 'Registro Exitoso', f'Alumno {nombre} {apellido} registrado.')
            # Limpia los campos de entrada después de registrar
            self.nombre_input.clear()
            self.apellido_input.clear()
            self.materias_input.clear()
        else:
            # Manda mensaje de error en caso de no completar el llenado de los campos
            QMessageBox.warning(self, 'Error', 'Por favor complete todos los campos.')
    
    def finalizarRegistro(self):
        alumnos = len(self.nombre)
        # Verifica si hay alumnos registrados antes de intentar guardar
        if alumnos > 0:
            estudiantes = pd.DataFrame({
                # Genera un identificador único para cada estudiante
                'Key': np.random.choice(10000, size=alumnos, replace=False),
                'Nombre': self.nombre,
                'Apellido': self.apellido,
                # Junta las materias en una cadena separada por comas
                'Materias': [', '.join(m) for m in self.materia]
            })
            # Guarda los datos en un archivo CSV
            estudiantes.to_csv('estudiantes.csv', index=False)
            QMessageBox.information(self, 'Guardado', 'Registro de estudiantes guardado exitosamente.')
            # Cierra la aplicación
            self.close()
        else:
            QMessageBox.warning(self, 'Error', 'No hay alumnos registrados para guardar.')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = RegistroEstudiantes()
    # Muestra la ventana de la aplicación
    window.show()
    # Ejecuta la aplicación
    sys.exit(app.exec())
