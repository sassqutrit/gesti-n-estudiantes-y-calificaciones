import sys
import pandas as pd
import numpy as np
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLineEdit
from PyQt6.QtWidgets import QLabel, QFormLayout, QMessageBox


class RegistroEstudiantes(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.nombre = []
        self.apellido = []
        self.materia = []
        
    def initUI(self):
        self.setWindowTitle('Registro de Estudiantes')
        
        layout = QFormLayout()
        self.alumnos_input = QLineEdit(self)
        layout.addRow('Cantidad de Alumnos:', self.alumnos_input)
        
        self.nombre_input = QLineEdit(self)
        layout.addRow('Nombre:', self.nombre_input)
        
        self.apellido_input = QLineEdit(self)
        layout.addRow('Apellido:', self.apellido_input)
        
        self.materias_input = QLineEdit(self)
        layout.addRow('Materias (Separadas por coma):', self.materias_input)
        
        self.registrar_btn = QPushButton('Registrar Alumno', self)
        self.registrar_btn.clicked.connect(self.registrarAlumno)
        layout.addWidget(self.registrar_btn)
        
        self.finalizar_btn = QPushButton('Finalizar Registro', self)
        self.finalizar_btn.clicked.connect(self.finalizarRegistro)
        layout.addWidget(self.finalizar_btn)
        
        self.setLayout(layout)
        
    def registrarAlumno(self):
        nombre = self.nombre_input.text()
        apellido = self.apellido_input.text()
        materias = self.materias_input.text().split(',')
        
        if nombre and apellido and materias:
            self.nombre.append(nombre)
            self.apellido.append(apellido)
            self.materia.append(materias)
            QMessageBox.information(self, 'Registro Exitoso', f'Alumno {nombre} {apellido} registrado.')
            self.nombre_input.clear()
            self.apellido_input.clear()
            self.materias_input.clear()
        else:
            QMessageBox.warning(self, 'Error', 'Por favor complete todos los campos.')
    
    def finalizarRegistro(self):
        alumnos = len(self.nombre)
        if alumnos > 0:
            estudiantes = pd.DataFrame({
                'Key': np.random.choice(10000, size=alumnos, replace=False),
                'Nombre': self.nombre,
                'Apellido': self.apellido,
                'Materias': [', '.join(m) for m in self.materia]
            })
            estudiantes.to_csv('estudiantes.csv', index=False)
            QMessageBox.information(self, 'Guardado', 'Registro de estudiantes guardado exitosamente.')
            self.close()
        else:
            QMessageBox.warning(self, 'Error', 'No hay alumnos registrados para guardar.')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = RegistroEstudiantes()
    window.show()
    sys.exit(app.exec())
