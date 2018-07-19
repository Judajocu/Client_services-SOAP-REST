import json
import unirest

def Menu():
    print("Servicio REST")
    print("1-Para ver todos los estudiantes")
    print("2-Para un estudiante en particuliar")
    print("3-Para agregar un estudiante")
    print("4-Para salir")

    x = input("Digite una opcion")
    Client(x)

def Client(x):
    if x == 1:
        data = unirest.get('http://localhost:4567/rest/estudiantes/', headers={"Accept": "application/json"})
        print(data.body)
        return Menu()

    elif x == 2:
        y = input("Digite una matricula")
        data2 = unirest.get('http://localhost:4567/rest/estudiantes/{}'.format(y), headers={"Accept": "application/json"})
        print(data2.body)
        return Menu()

    elif x == 3:
        nom = raw_input("Digite el nombre del nuevo estudiante")
        email = raw_input("Digite el correo del nuevo estudiante")
        carrera = raw_input("Digite la carrera del nuevo estudiante")
        data3 = unirest.post('http://localhost:4567/rest/estudiantes/',
                             headers={"Content-Type": "application/json", "Accept": "application/json"},
                             params=json.dumps({"nombre": nom, "correo": email, "carrera": carrera}))
        print(data3.body)
        return Menu()
    else:
        return 0

if __name__ == '__main__':
    Menu()