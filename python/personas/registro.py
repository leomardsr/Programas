class Person():
    def __init__(self):
        self.first_name = ''
        self.last_name = ''
        self.email = ''
        self.id_number = ''
        self.phone = ''


people = []


def create():
    print()
    person = Person()
    person.first_name = input('Ingrese el nombre: ')
    person.last_name = input('Ingrese el apellido: ')
    person.email = input('Ingrese el correo: ')
    person.id_number = input('Ingrese la cédula: ')
    person.phone = input('Ingrese el teléfono: ')
    people.append(person)
    print()


def show():
    print()
    i = 1
    print('Lista de Personas')
    print('Nombre  |  Apellido  |  Correo  |  Cédula  |  Teléfono  |  Nro')
    for person in people:
        print(
            person.first_name + ' | ' + person.last_name + ' | ' +
            person.email + ' | ' + person.id_number + ' | ' + person.phone +
            ' | #%s' % i
        )
        i += 1
    print()


def menu():
    print()
    band = True
    while band:
        print('1. Registrar')
        print('2. Actualizar')
        print('3. Eliminar')
        print('4. Listar')
        print('5. Salir')
        option = int(input('Elija una opción: '))
        if option == 1:
            create()
        elif option == 2:
            # update()
            pass
        elif option == 3:
            # delete()
            pass
        elif option == 4:
            show()
        elif option == 5:
            band = False
            print('Has salido de la aplicación.')


if __name__ == '__main__':
    print ('Bienvenido al Registro de Personas: ')
    menu()
