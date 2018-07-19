from zeep import Client

def Menu():
    print("Servicio SOAP")
    print("1-Para ver todos los estudiantes")
    print("2-Para ver una asignatura")
    print("3-Para ver un profesor")
    print("4-Para salir")

    x = input("Digite una opcion")
    client = Client('http://localhost:7777/ws/AcademicoWebService?wsdl')
    ClientSOAP(x, client)


def ClientSOAP(x,client):
    if x == 1:
        data = client.service.getAllEstudiante()
        print data
        Menu()
    elif x == 2:
        y = input("Digite un id")
        data2 = client.service.getAsignatura(y)
        print data2
        Menu()
    elif x == 3:
        y = raw_input("Digite una cedula")
        data3 = client.service.getProfesor(y)
        print data3
        Menu()
    else:
        return 0

if __name__ == '__main__':
    Menu()