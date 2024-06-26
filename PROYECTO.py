import pymysql
import sys
import matplotlib.pyplot as plt

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QMessageBox, QTableWidgetItem, QTextBrowser
from PyQt5.uic import loadUi

#-------------------------------------------------------------------------------------------------------------

#Ventana que muestra las las tablas (Clientes, Facturas, MIA vendidos) para crear registros. 
class Seleccionar_tabla_crear(QDialog):
    def __init__(self, seleccionar_tabla_window, connection):
        super().__init__()
        loadUi("seleccion_crear.ui", self)
        self.seleccionar_tabla_window = seleccionar_tabla_window
        self.connection = connection

        self.combo_crear.addItem("Clientes")
        self.combo_crear.addItem("Facturas")
        self.combo_crear.addItem("MIAs")
            
        # Boton para volver a la ventana de registros
        self.boton_volver.clicked.connect(self.volver_al_registro)

        # Boton para ir a la ventana indicada en el ComboBox
        self.combo_crear.currentIndexChanged.connect(self.update_function)

    # Función que identifica el texto del Combo y conecta con su respectiva ventana
    def update_function(self):
        try:
            self.boton_ir.clicked.disconnect()
        except TypeError:
            pass
        
        if self.combo_crear.currentText() == "Clientes":
            self.boton_ir.clicked.connect(self.connect_to_crear_registro_cliente)
                
        elif self.combo_crear.currentText() == "Facturas":
            self.boton_ir.clicked.connect(self.connect_to_crear_registro_factura)
                
        elif self.combo_crear.currentText() == "MIAs":
            self.boton_ir.clicked.connect(self.connect_to_crear_registro_mia)

    # Funcion que vuelve a la ventana de registros
    def volver_al_registro(self):
        self.registro = Registros(self, self.connection)
        self.registro.show()
        self.hide()

    # Función que conecta con la ventana para Crear un registro de clientes
    def connect_to_crear_registro_cliente(self):
        self.main_window = Crear_registro_cliente(self, self.connection)
        self.main_window.show()
        self.hide()

    # Función que conecta con la ventana para Crear un registro de facturas
    def connect_to_crear_registro_factura(self):
        self.main_window = Crear_registro_factura(self, self.connection)
        self.main_window.show()
        self.hide()

    # Función que conecta con la ventana para Crear un registro de MIAs
    def connect_to_crear_registro_mia(self):
        self.main_window = Crear_registro_mia(self, self.connection)
        self.main_window.show()
        self.hide()

########################################################################################################################################

# Ventana que muestra las opciones de tablas para modificar
class Seleccionar_tabla_modificar(QDialog):
    def __init__(self, seleccionar_tabla_window, connection):
        super().__init__()
        loadUi("seleccion_crear.ui", self)
        self.seleccionar_tabla_window = seleccionar_tabla_window
        self.connection = connection

        self.combo_crear.addItem('Clientes')
        self.combo_crear.addItem('Facturas')
        self.combo_crear.addItem('MIAs')

        # Boton para volver a la ventana de registros
        self.boton_volver.clicked.connect(self.volver_al_registro)

        # Botón para ir a la ventana seleccionada en el ComboBox
        self.combo_crear.currentIndexChanged.connect(self.update_function)

    # Función que identifica el texto del Combo y conecta con su respectiva ventana
    def update_function(self):
        try:
            self.boton_ir.clicked.disconnect()
        except TypeError:
            pass

        if self.combo_crear.currentText() == "Clientes":
            self.boton_ir.clicked.connect(self.connect_to_modificar_registro_cliente)
            
        elif self.combo_crear.currentText() == "Facturas":
            self.boton_ir.clicked.connect(self.connect_to_modificar_registro_factura)
            
        elif self.combo_crear.currentText() == "MIAs":
            self.boton_ir.clicked.connect(self.connect_to_modificar_registro_mia)
        
    # Funcion que vuelve a la ventana de registros
    def volver_al_registro(self):
        self.registro = Registros(self, self.connection)
        self.registro.show()
        self.hide()

    # Funcion que conencta con la ventana para modificar un registro de Cliente
    def connect_to_modificar_registro_cliente(self):
        self.main_window = Modificar_registros_clientes(self, self.connection)
        self.main_window.show()
        self.hide()

    # Funcion que conencta con la ventana para modificar un registro de Facturas
    def connect_to_modificar_registro_factura(self):
        self.main_window = Modificar_registros_facturas(self, self.connection)
        self.main_window.show()
        self.hide()

    # Funcion que conencta con la ventana para modificar un registro de MIAs
    def connect_to_modificar_registro_mia(self):
        self.main_window = Modificar_registro_mia(self, self.connection)
        self.main_window.show()
        self.hide()

########################################################################################################################################

# Ventana que muestra las opciones de tablas para eliminar registros 
class Seleccionar_tabla_eliminar(QDialog):
    def __init__(self, seleccionar_tabla_window, connection):
        super().__init__()
        loadUi("seleccion_crear.ui", self)
        self.seleccionar_tabla_window = seleccionar_tabla_window
        self.connection = connection

        self.combo_crear.addItem('Clientes')
        self.combo_crear.addItem('Facturas')
        self.combo_crear.addItem('MIAs')

        # Boton para volver a la ventana de registros
        self.boton_volver.clicked.connect(self.volver_al_registro)

        # Botón para ir a la ventana seleccionada en el ComboBox
        self.combo_crear.currentIndexChanged.connect(self.update_function)

    # Función que identifica el texto del Combo y conecta con su respectiva ventana
    def update_function(self):
        try:
            self.boton_ir.clicked.disconnect()
        except TypeError:
            pass

        if self.combo_crear.currentText() == "Clientes":
            self.boton_ir.clicked.connect(self.connect_to_modificar_registro_cliente)
            
        elif self.combo_crear.currentText() == "Facturas":
            self.boton_ir.clicked.connect(self.connect_to_modificar_registro_factura)
            
        elif self.combo_crear.currentText() == "MIAs":
            self.boton_ir.clicked.connect(self.connect_to_modificar_registro_mia)
        
    # Funcion que vuelve a la ventana de registros
    def volver_al_registro(self):
        self.registro = Registros(self, self.connection)
        self.registro.show()
        self.hide()

    # Funcion que conecta con la ventana para eliminar un registro de Clientes
    def connect_to_modificar_registro_cliente(self):
        self.main_window = Eliminar_registros_clientes(self, self.connection)
        self.main_window.show()
        self.hide()

    # Funcion que conecta con la ventana para eliminar un registro de Facturas
    def connect_to_modificar_registro_factura(self):
        self.main_window = Eliminar_registros_facturas(self, self.connection)
        self.main_window.show()
        self.hide()

    # Funcion que conecta con la ventana para eliminar un registro de MIAs
    def connect_to_modificar_registro_mia(self):
        self.main_window = Eliminar_registros_mia(self, self.connection)
        self.main_window.show()
        self.hide()

        
########################################################################################################################################

# Ventana que contiene los campos para modificar registros de Clientes
class Modificar_registros_clientes(QDialog):
    def __init__(self, modificar_registros_window, connection):
        super().__init__()
        loadUi("modificar_registro_clientes.ui", self)
        self.modificar_registros_window = modificar_registros_window
        self.connection = connection

        # Boton para modificar un registro
        self.boton_modificar.clicked.connect(self.modificar_registro)

        # Boton para volver a la ventana de seleccion
        self.boton_volver.clicked.connect(self.volver_a_la_seleccion)

    # Funcion que vuelve a la ventana de seleccion
    def volver_a_la_seleccion(self):
        self.registro = Seleccionar_tabla_modificar(self, self.connection)
        self.registro.show()
        self.hide()
    
    # Funcion que moidifica un registro de Clientes de sql
    def modificar_registro(self):
        # Obtener el código del registro a modificar y los nuevos valores
        id_cliente = self.crear_cliente_codigo.text()
        Nombre = self.crear_cliente_nombre.text()

        if not (id_cliente and Nombre):
            QMessageBox.critical(self, "Error", "Todos los campos deben estar llenos")
            return
  
        try:
            with self.connection.cursor() as cursor:
                # Ejecutar la consulta SQL para modificar el registro
                cursor.execute("""UPDATE Clientes SET Nombre = %s WHERE id_cliente = %s """, (Nombre, id_cliente))
                self.connection.commit()

                QMessageBox.information(self, "Éxito", "Registro modificado exitosamente")
        except pymysql.MySQLError as e:
            QMessageBox.critical(self, "Error", str(e))
    
# Ventana que contiene los campos para modificar registros de Facturas
class Modificar_registros_facturas(QDialog):
    def __init__(self, modificar_registros_window, connection):
        super().__init__()
        loadUi("modificar_registro_factura.ui", self)
        self.modificar_registros_window = modificar_registros_window
        self.connection = connection

        # Boton para modificar un registro
        self.boton_modificar.clicked.connect(self.modificar_registro)

        # Boton para volver a la ventana de seleccion
        self.boton_volver.clicked.connect(self.volver_a_la_seleccion)

    # Funcion que vuelve a la ventana de seleccion
    def volver_a_la_seleccion(self):
        self.registro = Seleccionar_tabla_modificar(self, self.connection)
        self.registro.show()
        self.hide()
    
    # Funcion que moidifica un registro de Factura de sql
    def modificar_registro(self):
        # Obtener el código del registro a modificar y los nuevos valores
        id_factura = self.crear_factura_codigo.text()
        id_cliente = self.crear_factura_codigoclient.text()
        monto_total = self.crear_factura_monto.text()
        fecha = self.crea_factura_fecha.text()

        if not (id_factura and id_cliente and monto_total and fecha):
            QMessageBox.critical(self, "Error", "Todos los campos deben estar llenos")
            return

        try:
            with self.connection.cursor() as cursor:
                # Ejecutar la consulta SQL para modificar el registro
                cursor.execute("""UPDATE Facturas SET id_cliente = %s, monto_total = %s, fecha = %s WHERE id_factura = %s""", (id_cliente, monto_total, fecha, id_factura))
                self.connection.commit()

                QMessageBox.information(self, "Éxito", "Registro modificado exitosamente")
        except pymysql.MySQLError as e:
            QMessageBox.critical(self, "Error", str(e))

# Ventana que contiene los campos para modificar registros de los MIAs
class Modificar_registro_mia(QDialog):
    def __init__(self, modificar_registros_window, connection):
        super().__init__()
        loadUi("modificar_registro_mia.ui", self)
        self.modificar_registros_window = modificar_registros_window
        self.connection = connection

        # Boton para modificar un registro de un MIA
        self.boton_modificar.clicked.connect(self.modificar_registro_mia)

        # Boton para volver a la ventana de seleccion
        self.boton_volver.clicked.connect(self.volver_a_la_seleccion)

    # Funcion que vuelve a la ventana de seleccion
    def volver_a_la_seleccion(self):
        self.registro = Seleccionar_tabla_modificar(self, self.connection)
        self.registro.show()
        self.hide()
    
    # Funcion que moidifica un registro de un MIA en sql
    def modificar_registro_mia(self):
        # Obtener el código del registro a modificar y los nuevos valores
        MIA = self.crear_factura_mia.text()
        id_factura = self.crear_factura_codigofact.text()
        CIF = self.crear_factura_cif.text()
        peso = self.crear_factura_pesp.text()
        total_aduana = self.crear_factura_aduana.text()

        if not (MIA and id_factura and CIF and peso and total_aduana):
            QMessageBox.critical(self, "Error", "Todos los campos deben estar llenos")
            return

        try:
            with self.connection.cursor() as cursor:
                # Ejecutar la consulta SQL para modificar el registro
                cursor.execute("""UPDATE MIA_vendidos SET id_factura = %s, CIF = %s, peso = %s, total_aduana = %s WHERE MIA = %s """, (id_factura, CIF, peso, total_aduana, MIA))
                self.connection.commit()

                QMessageBox.information(self, "Éxito", "Registro modificado exitosamente")
        except pymysql.MySQLError as e:
            QMessageBox.critical(self, "Error", str(e))
    

    
########################################################################################################################################

# Ventana que contiene el campo para eliminar un registro de Clientes
class Eliminar_registros_clientes(QDialog):
    def __init__(self, elimar_registros_window, connection):
        super().__init__()
        loadUi("eliminar_registro.ui", self)
        self.elimar_registros_window = elimar_registros_window
        self.connection = connection

        # Boton para elimnar un registro
        self.boton_eliminar_registro.clicked.connect(self.eliminar_registro_cliente)

        # Boton para volver a la ventana de seleccion
        self.boton_volver.clicked.connect(self.volver_a_la_seleccion)

    # Funcion que vuelve a la ventana de seleccion
    def volver_a_la_seleccion(self):
        self.registro = Seleccionar_tabla_eliminar(self, self.connection)
        self.registro.show()
        self.hide()

    # Funcion que elimina un registro
    def eliminar_registro_cliente(self):
        # Obtener el ID del registro a eliminar
        id_registro = self.codigo_eliminar.text()

        if not id_registro:
            QMessageBox.critical(self, "Error", "Debes ingresar un ID de registro")
            return

        try:
            with self.connection.cursor() as cursor:
                # Ejecutar la consulta SQL para eliminar el registro
                cursor.execute("DELETE FROM Clientes WHERE id_cliente = %s", (id_registro,))
                self.connection.commit()

                QMessageBox.information(self, "Éxito", "Registro eliminado exitosamente")
                
        except pymysql.MySQLError as e:
            QMessageBox.critical(self, "Error", str(e))


# Ventana que contiene el campo para eliminar un registro de Facturas
class Eliminar_registros_facturas(QDialog):
    def __init__(self, elimar_registros_window, connection):
        super().__init__()
        loadUi("eliminar_registro.ui", self)
        self.elimar_registros_window = elimar_registros_window
        self.connection = connection

        # Boton para elimnar un registro
        self.boton_eliminar_registro.clicked.connect(self.eliminar_registro_factura)

        # Boton para volver a la ventana de seleccion
        self.boton_volver.clicked.connect(self.volver_a_la_seleccion)

    # Funcion que vuelve a la ventana de registros
    def volver_a_la_seleccion(self):
        self.registro = Seleccionar_tabla_eliminar(self, self.connection)
        self.registro.show()
        self.hide()
        
    # Funcion que elimina un registro de una factura 
    def eliminar_registro_factura(self):
        # Obtener el ID del registro a eliminar
        id_registro = self.codigo_eliminar.text()

        if not id_registro:
            QMessageBox.critical(self, "Error", "Debes ingresar un ID de registro")
            return

        try:
            with self.connection.cursor() as cursor:
                # Ejecutar la consulta SQL para eliminar el registro
                cursor.execute("DELETE FROM Facturas WHERE id_factura = %s", (id_registro,))
                self.connection.commit()

                QMessageBox.information(self, "Éxito", "Registro eliminado exitosamente")
                
        except pymysql.MySQLError as e:
            QMessageBox.critical(self, "Error", str(e))

# Ventana que contiene el campo para eliminar un registro de un MIA
class Eliminar_registros_mia(QDialog):
    def __init__(self, elimar_registros_window, connection):
        super().__init__()
        loadUi("eliminar_registro.ui", self)
        self.elimar_registros_window = elimar_registros_window
        self.connection = connection

        # Boton para elimnar un registro de un MIA
        self.boton_eliminar_registro.clicked.connect(self.eliminar_registro_mia)

        # Boton para volver a la ventana de seleccion
        self.boton_volver.clicked.connect(self.volver_a_la_seleccion)

    # Funcion que vuelve a la ventana de registros
    def volver_a_la_seleccion(self):
        self.registro = Seleccionar_tabla_eliminar(self, self.connection)
        self.registro.show()
        self.hide()

    # Funcion que elimina un registro de un MIA
    def eliminar_registro_mia(self):
        # Obtener el ID del registro a eliminar
        id_registro = self.codigo_eliminar.text()

        if not id_registro:
            QMessageBox.critical(self, "Error", "Debes ingresar un ID de registro")
            return

        try:
            with self.connection.cursor() as cursor:
                # Ejecutar la consulta SQL para eliminar el registro
                cursor.execute("DELETE FROM MIA_vendidos WHERE MIA = %s", (id_registro,))
                self.connection.commit()

                QMessageBox.information(self, "Éxito", "Registro eliminado exitosamente")
                
        except pymysql.MySQLError as e:
            QMessageBox.critical(self, "Error", str(e))


#######################################################################################################################################

# Ventana que contiene los campos para crear registros de Clientes 
class Crear_registro_cliente(QDialog):
    def __init__(self, cliente_window, connection):
        super().__init__()
        loadUi("crear_registro_clientes.ui", self)
        self.cliente_window = cliente_window
        self.connection = connection

        # Boton para agregar un registro de Cliente
        self.boton_agregar.clicked.connect(self.insert_data)
        
        # Boton para volver a la ventana de registros
        self.boton_volver.clicked.connect(self.volver_a_la_seleccion)
    
    # Funcion que vuelve a la ventana de registros
    def volver_a_la_seleccion(self):
        self.registro = Seleccionar_tabla_crear(self, self.connection)
        self.registro.show()
        self.hide()
    
    # Funcion que agrega datos
    def insert_data(self):
    # Obtener los datos de los campos de entrada
        codigo = self.crear_cliente_codigo.text()
        nombre = self.crear_cliente_nombre.text()

        if not (codigo and nombre):
            QMessageBox.critical(self, "Error", "All fields must be filled")
            return

        insert_query = "INSERT INTO Clientes (id_cliente, Nombre) VALUES (%s, %s)"

        try:
            with self.connection.cursor() as cursor:
                cursor.execute(insert_query, (codigo, nombre))
                self.connection.commit()
                QMessageBox.information(self, "Success", "Data inserted successfully")
                #self.execute_query()  # Refresh the displayed data            
            
        except pymysql.MySQLError as e:
            QMessageBox.critical(self, "Insertion Error", str(e))
    
class Crear_registro_factura(QDialog):
    def __init__(self, factura_window, connection):
        super().__init__()
        loadUi("crear_registro_factura.ui", self)
        self.factura_window = factura_window
        self.connection = connection

        # Boton para agregar un registro
        self.agregar.clicked.connect(self.insert_data)
        # Boton para volver a la ventana de registros
        self.boton_volver.clicked.connect(self.volver_a_la_seleccion)

    # Funcion que vuelve a la ventana de registros
    def volver_a_la_seleccion(self):
        self.registro = Seleccionar_tabla_crear(self, self.connection)
        self.registro.show()
        self.hide()

    # Funcion que agrega datos a la tabla partidos
    def insert_data(self):
    # Obtener los datos de los campos de entrada
        id_factura = self.crear_factura_codigo.text()
        id_cliente = self.crear_factura_codigoclient.text()
        monto_total = self.crear_factura_monto.text()
        fecha = self.crea_factura_fecha.text()

        if not (id_factura and id_cliente and monto_total and fecha):
            QMessageBox.critical(self, "Error", "All fields must be filled")
            return

        insert_query = "INSERT INTO Facturas (id_factura, id_cliente, monto_total, fecha) VALUES (%s, %s, %s, %s)"

        try:
            with self.connection.cursor() as cursor:
                cursor.execute(insert_query, (id_factura, id_cliente, monto_total, fecha))
                self.connection.commit()
                QMessageBox.information(self, "Success", "Data inserted successfully")
                #self.execute_query()  # Refresh the displayed data            
            
        except pymysql.MySQLError as e:
            QMessageBox.critical(self, "Insertion Error", str(e))

class Crear_registro_mia(QDialog):
    def __init__(self, mia_window, connection):
        super().__init__()
        loadUi("crear_registro_mia.ui", self)
        self.mia_window = mia_window
        self.connection = connection

        # Boton para agregar un registro
        self.agregar.clicked.connect(self.insert_data)
        
        # Boton para volver a la ventana de registros
        self.boton_volver.clicked.connect(self.volver_a_la_seleccion)

    # Funcion que vuelve a la ventana de registros
    def volver_a_la_seleccion(self):
        self.registro = Seleccionar_tabla_crear(self, self.connection)
        self.registro.show()
        self.hide()

    # Funcion que agrega datos a la tabla partidos
    def insert_data(self):
    # Obtener los datos de los campos de entrada
        MIA = self.crear_factura_mia.text()
        id_factura = self.crear_factura_codigofact.text()
        CIF = self.crear_factura_cif.text()
        peso = self.crear_factura_pesp.text()
        total_aduana = self.crear_factura_aduana.text()

        if not (MIA and id_factura and CIF and peso and total_aduana):
            QMessageBox.critical(self, "Error", "All fields must be filled")
            return

        insert_query = "INSERT INTO MIA_vendidos (MIA, id_factura, CIF, peso, total_aduana) VALUES (%s, %s, %s, %s, %s)"

        try:
            with self.connection.cursor() as cursor:
                cursor.execute(insert_query, (MIA, id_factura, CIF, peso, total_aduana))
                self.connection.commit()
                QMessageBox.information(self, "Success", "Data inserted successfully")
                #self.execute_query()  # Refresh the displayed data            
            
        except pymysql.MySQLError as e:
            QMessageBox.critical(self, "Insertion Error", str(e))

###########################################################################################################################################################

class Registros(QDialog):
    def __init__(self, registros_window, connection):
        super().__init__()
        loadUi("registros.ui", self)
        self.registros_window = registros_window
        self.connection = connection
   
        self.registros_combobox.addItem('Visualizar tabla')
        self.registros_combobox.addItem('Visualizar Ventas Mensuales')
        self.registros_combobox.addItem('Gráfica de Ventas Mensuales')
        self.registros_combobox.addItem('TOP 5 Clientes')

        # Conectar el botón a la función de ejecución de consulta
        self.registros_boton_visualizar.clicked.connect(self.execute_query)

        # Boton para ir a la ventana de crear un registro
        self.registros_crear.clicked.connect(self.connect_to_seleccionar_tabla_crear)

        # Boton para ir a la ventana de modificar un registro
        self.registros_modificar.clicked.connect(self.connect_to_seleccionar_tabla_modificar)
        
        # Boton para ir a la ventana de elimnar un registro
        self.registros_eliminar.clicked.connect(self.connect_to_seleccionar_tabla_eliminar)


    def connect_to_seleccionar_tabla_crear(self):
        self.main_window = Seleccionar_tabla_crear(self, self.connection)
        self.main_window.show()
        self.hide()

    def connect_to_seleccionar_tabla_modificar(self):
        self.main_window = Seleccionar_tabla_modificar(self, self.connection)
        self.main_window.show()
        self.hide()

    def connect_to_seleccionar_tabla_eliminar(self):
        self.main_window = Seleccionar_tabla_eliminar(self, self.connection)
        self.main_window.show()
        self.hide()
    
    def execute_query(self):
        if not self.connection:
            QMessageBox.critical(self, "Error", "No database connection")
            return

        query = self.get_query(self.registros_combobox.currentText())
        
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(query)
                result = cursor.fetchall()
                print(result)
                    
                if self.registros_combobox.currentText() == "Visualizar tabla":
                    # Obtener los nombres de las columnas
                    cursor.execute(f"SHOW COLUMNS FROM {self.query_table.text()}")
                    column_names = [column[0] for column in cursor.fetchall()]
                    self.display_results(result, column_names)

                elif self.registros_combobox.currentText() == "Visualizar Ventas Mensuales":
                    # Obtener los nombres de las columnas
                    #cursor.execute(f"SHOW COLUMNS FROM {self.query_table.text()}")
                    column_names = ["Periodo", "Ventas TOTALES del periodo"]
                    self.display_results(result, column_names)
                    
                elif self.registros_combobox.currentText() == "Gráfica de Ventas Mensuales":
                    # Crear una instancia de MyWindow con los resultados
                    self.window = MyWindow(result)
                    # Mostrar la ventana
                    self.window.show()

                elif self.registros_combobox.currentText() == "TOP 5 Clientes":
                    # Definir los nombres de las columnas de la tabla
                    column_names = ["Nombre", "Compras totales"]
                    # Mostrar los resultados de la consulta
                    self.display_results(result, column_names)
                    
        except pymysql.MySQLError as e:
            QMessageBox.critical(self, "Query Error", str(e))

    def display_results(self, results, column_names):
        print(results)
        self.mostrar.setRowCount(len(results))
        self.mostrar.setColumnCount(len(results[0]) if results else 0)

        # Establecer los nombres de las columnas
        self.mostrar.setHorizontalHeaderLabels(column_names)

        for i, row in enumerate(results):
            for j, item in enumerate(row):
                self.mostrar.setItem(i, j, QtWidgets.QTableWidgetItem(str(item)))

    def get_query(self, query_name):
        # Definir las consultas SQL aquí
        tabla = self.query_table.text()
        queries = {
            "Visualizar tabla": f"SELECT * FROM {tabla}",
            "Visualizar Ventas Mensuales": f"SELECT DATE_FORMAT(fecha, '%Y-%m') AS 'Año-Mes', SUM(monto_total) AS 'Total facturado'FROM Facturas GROUP BY DATE_FORMAT(fecha, '%Y-%m')ORDER BY 'Año-Mes'",
            "TOP 5 Clientes": f"SELECT c.Nombre, SUM(f.monto_total) AS Total_Compras FROM Clientes c JOIN Facturas f ON c.id_cliente = f.id_cliente GROUP BY c.Nombre ORDER BY Total_Compras DESC LIMIT 5",
            "Gráfica de Ventas Mensuales": f"SELECT DATE_FORMAT(fecha, '%Y-%m') AS 'Año-Mes', SUM(monto_total) AS 'Total facturado' FROM Facturas GROUP BY DATE_FORMAT(fecha, '%Y-%m') ORDER BY 'Año-Mes'",
        }
        return queries.get(query_name, "")

class MyWindow(QtWidgets.QWidget):
    def __init__(self, results, parent=None):
        super(MyWindow, self).__init__(parent)
        self.figure = plt.figure(figsize=(5, 5))
        self.canvas = FigureCanvas(self.figure)
        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.addWidget(self.canvas)
        self.display_results(results)

    def display_results(self, results):
        if not results:
            print("No hay resultados para mostrar.")
            return
        
        results = results[-12:]
        
        x_values = [row[0] for row in results]
        y_values = [row[1] for row in results]

        ax = self.figure.add_subplot(111)
        bars = ax.bar(x_values, y_values)
        ax.set_title('Resultados')
        ax.set_xlabel('Periodo (Año-Mes)')
        ax.set_ylabel('Ventas totales')
        ax.grid(True)

        # Agregar anotaciones a las barras
        for bar in bars:
            yval = bar.get_height()
            ax.text(bar.get_x() + bar.get_width()/2, yval, round(yval, 2), ha='center', va='bottom')

        self.canvas.draw()
        
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi("main_window.ui", self)
        self.connection = None

        self.main_boton_conectar.clicked.connect(self.connect_to_databse)

    def connect_to_databse(self):
        host = self.main_host.text()
        user = self.main_usuario.text()
        password = self.main_password.text()

        try:
            self.connection = pymysql.connect(
                host = host,
                user = user,
                password = password,
                database = "bdmonov8"
                )
            QMessageBox.information(self, "Éxito", "Conectado a la Base de datos de MonoV8")

            self.registros = Registros(self, self.connection)
            self.registros.show()
            self.hide()
        except pymysql.MyQSLError as e:
            QMessageBox.critical(self, "Error al conectar", str(e))
            

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec())
  
