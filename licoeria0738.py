print("Examen v2 Angel Miguel Valencia Carrillo 0738")
class licoreria0738 :
    
    def Diccionario_empleados_datos0738 (self):
        print("EMPLEADOS")
        diccempleados0738 = {
        "Nombre :": "Gustavo Rodrigues",
        "Id :": "12345",
        "Edad :": "26",
        "Direccion :": "calle hollywood",
        "Telefono :": "656 478 9999",
        "Horario :": "12 pm- 9 pm",
        "num.seguro social :": "09843732"
        }
        print(diccempleados0738)
        for empleado0738, datos0738 in diccempleados0738.items():
            print(empleado0738, datos0738)
            
    def Diccionario_Provedores_datos0738 (self):
        print("PROVEDORES")
        diccprovedores0738 = {
        "Nombre :": "Bacardi",
        "Id :": "8888",
        "Cant.Paquetes :": "26",
        "Direccion :": "Avenida zaragoza",
        "Tipo de bebida :": "alcholica",
        "Contacto :": "656 777 8889",
        "Precio :": "15,000$"
        }
        print(diccprovedores0738)
        for provedores0738, datos0738 in diccprovedores0738.items():
            print(provedores0738, datos0738)
            
    def Diccionario_bebidas_datos0738 (self):
        print("BEBIDAS")
        diccbebidas0738 = {
        "Nombre :": "Sky",
        "Id :": "675300",
        "Tipo :": "Alcholica",
        "Sabor :": "Manzana verde",
        "Tanmaño :": "750 ml",
        "Precio :": "35.00$",
        "Cantidad:": "1"
        }
        print(diccbebidas0738)
        for bebidas0738, datos0738 in diccbebidas0738.items():
            print(bebidas0738, datos0738)
        
    def Diccionario_clientes_datos0738 (self):
        print("CLIENTES")
        dicClientes0738 = {
        "Nombre :": "Oscar lopez",
        "Id :": "337337",
        "Cuenta :": "Activa",
        "Edad :": "22",
        "Telefono :": "656 478 9999",
        "Correo :": "oscarL12345@gmail.com",
        "Bebida comprada :": "Sky sabor manzana verde"
        }
        print(dicClientes0738)
        for cliente0738, datos0738 in dicClientes0738.items():
            print(cliente0738, datos0738)
info=licoreria0738()
info.Diccionario_empleados_datos0738()
print("")
info.Diccionario_Provedores_datos0738()
print("")
info.Diccionario_bebidas_datos0738()
print("")
info.Diccionario_clientes_datos0738()
print("")