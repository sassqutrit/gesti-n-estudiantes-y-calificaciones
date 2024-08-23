import sys
import os
import pandas as pd
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton
from PyQt6.QtWidgets import QLineEdit, QLabel, QMessageBox, QComboBox, QHBoxLayout, QStackedWidget


class RegistroCalificaciones(QWidget):
    def __init__(self):
        super().__init__()
        self.base = self.cargar_base_estudiantes()
        self.notas = pd.DataFrame(columns=['Key', 'Materia', 'Nota'])  # Inicializar con columnas correctas

        self.initUI()

    def cargar_base_estudiantes(self):
        if os.path.exists('estudiantes.csv'):
            return pd.read_csv('estudiantes.csv')
        else:
            QMessageBox.critical(self, 'Error', 'No se encontró el archivo estudiantes.csv.')
            self.close()
            return pd.DataFrame()

    def initUI(self):
        self.setWindowTitle('Registro de Calificaciones')

        self.layout = QVBoxLayout()

        # Crear el QStackedWidget
        self.stackedWidget = QStackedWidget()

        # Crear la página del menú
        menu_widget = QWidget()
        menu_layout = QVBoxLayout()

        menu_label = QLabel('Menu de Opciones:', self)
        menu_layout.addWidget(menu_label)

        self.btnIngresar = QPushButton('1. Ingresar calificaciones', self)
        self.btnIngresar.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(1))
        menu_layout.addWidget(self.btnIngresar)

        self.btnVer = QPushButton('2. Ver calificaciones', self)
        self.btnVer.clicked.connect(self.verCalificaciones)
        menu_layout.addWidget(self.btnVer)

        self.btnGuardar = QPushButton('3. Guardar avance', self)
        self.btnGuardar.clicked.connect(self.guardarCalificaciones)
        menu_layout.addWidget(self.btnGuardar)

        self.btnModificar = QPushButton('4. Modificar calificaciones', self)
        self.btnModificar.clicked.connect(self.modificarCalificaciones)
        menu_layout.addWidget(self.btnModificar)

        self.btnEnviar = QPushButton('5. Enviar calificaciones', self)
        self.btnEnviar.clicked.connect(self.enviarCalificaciones)
        menu_layout.addWidget(self.btnEnviar)

        self.btnSalir = QPushButton('6. Salir', self)
        self.btnSalir.clicked.connect(self.close)
        menu_layout.addWidget(self.btnSalir)

        menu_widget.setLayout(menu_layout)
        self.stackedWidget.addWidget(menu_widget)

        # Crear la página para ingresar calificaciones
        self.registro_widget = QWidget()
        registro_layout = QVBoxLayout()

        materia_layout = QHBoxLayout()
        materia_label = QLabel('Materia:', self)
        self.materia_input = QComboBox(self)
        self.materia_input.addItems(['Matematicas', 'Historia', 'Ingles', 'Español', 'Frances'])
        self.materia_input.currentIndexChanged.connect(self.actualizarEstudiantes)
        materia_layout.addWidget(materia_label)
        materia_layout.addWidget(self.materia_input)
        registro_layout.addLayout(materia_layout)

        estudiante_layout = QHBoxLayout()
        estudiante_label = QLabel('Estudiante:', self)
        self.estudiante_input = QComboBox(self)
        estudiante_layout.addWidget(estudiante_label)
        estudiante_layout.addWidget(self.estudiante_input)
        registro_layout.addLayout(estudiante_layout)

        calificacion_layout = QHBoxLayout()
        calificacion_label = QLabel('Calificación:', self)
        self.calificacion_input = QLineEdit(self)
        calificacion_layout.addWidget(calificacion_label)
        calificacion_layout.addWidget(self.calificacion_input)
        registro_layout.addLayout(calificacion_layout)

        self.calificar_btn = QPushButton('Calificar', self)
        self.calificar_btn.clicked.connect(self.calificar)
        registro_layout.addWidget(self.calificar_btn)

        volver_btn = QPushButton('Volver al menú', self)
        volver_btn.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(0))
        registro_layout.addWidget(volver_btn)

        self.registro_widget.setLayout(registro_layout)
        self.stackedWidget.addWidget(self.registro_widget)

        self.layout.addWidget(self.stackedWidget)
        self.setLayout(self.layout)

        self.actualizarEstudiantes()

    def actualizarEstudiantes(self):
        self.estudiante_input.clear()
        materia = self.materia_input.currentText()
        if not self.base.empty:
            for i in range(len(self.base)):
                if materia in self.base.loc[i, 'Materias']:
                    estudiante = f"{self.base.loc[i, 'Key']} - {self.base.loc[i, 'Nombre']} {self.base.loc[i, 'Apellido']}"
                    self.estudiante_input.addItem(estudiante)
    
    def calificar(self):
        estudiante = self.estudiante_input.currentText()
        if not estudiante:
            QMessageBox.warning(self, 'Error', 'Por favor, seleccione un estudiante.')
            return
        
        key, _ = estudiante.split(' - ')
        calificacion = self.calificacion_input.text()
        
        if not calificacion.isdigit():
            QMessageBox.warning(self, 'Error', 'Por favor, ingrese una calificación válida.')
            return
        
        calificacion = int(calificacion)
        materia = self.materia_input.currentText()

        # Verificar que el DataFrame tenga las columnas correctas antes de eliminar registros
        if 'Key' in self.notas.columns and 'Materia' in self.notas.columns:
            # Filtrar para eliminar cualquier calificación existente para el mismo estudiante en la misma materia
            self.notas = self.notas[~((self.notas['Key'] == int(key)) & (self.notas['Materia'] == materia))]
        
        nueva_nota = pd.DataFrame({'Key': [int(key)], 'Materia': [materia], 'Nota': [calificacion]})
        self.notas = pd.concat([self.notas, nueva_nota], ignore_index=True)
        
        QMessageBox.information(self, 'Calificación', f'Calificación registrada para {materia}.')
        self.calificacion_input.clear()
        
         # Volver a activar el botón de guardar después de ingresar una nueva calificación
        self.btnGuardar.setEnabled(True)

    def guardarCalificaciones(self):
        # Desactivar el botón para evitar múltiples clics
        self.btnGuardar.setEnabled(False)
        
        if not self.notas.empty:
            materia = self.materia_input.currentText()

            # Filtrar las notas de la materia actual antes de guardarlas
            notas_materia_actual = self.notas[self.notas['Materia'] == materia]

            archivo = f'notas_{materia.lower()}.csv'
            
            if os.path.exists(archivo):
                # Si el archivo ya existe, cargar el archivo existente
                notas_existentes = pd.read_csv(archivo)
                # Eliminar las calificaciones existentes en el CSV para los estudiantes de la misma materia
                notas_existentes = notas_existentes[~((notas_existentes['Key'].isin(notas_materia_actual['Key'])) & (notas_existentes['Materia'] == materia))]
                # Concatenar las nuevas notas de la materia actual con las restantes
                notas_materia_actual = pd.concat([notas_existentes, notas_materia_actual], ignore_index=True)
            
            # Guardar las calificaciones en el archivo CSV
            notas_materia_actual.to_csv(archivo, index=False)
            QMessageBox.information(self, 'Guardado', f'Calificaciones guardadas exitosamente para {materia}.')
            
        else:
            QMessageBox.warning(self, 'Error', 'No hay calificaciones para guardar.')
            

    def verCalificaciones(self):
        materia = self.materia_input.currentText()
        archivo = f'notas_{materia.lower()}.csv'
        if os.path.exists(archivo):
            notas = pd.read_csv(archivo)
            # Filtrar solo las notas de la materia actual
            notas = notas[notas['Materia'] == materia]
            QMessageBox.information(self, 'Calificaciones', notas.to_string(index=False))
        else:
            QMessageBox.warning(self, 'Error', f'No hay calificaciones guardadas para la materia {materia}.')
    
    def modificarCalificaciones(self):
        QMessageBox.information(self, 'Modificar Calificaciones', 'Funcionalidad en desarrollo.')
    
    def enviarCalificaciones(self):
        QMessageBox.information(self, 'Enviar Calificaciones', 'Calificaciones enviadas exitosamente.')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = RegistroCalificaciones()
    window.show()
    sys.exit(app.exec())
