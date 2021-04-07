class Person():
    def __init__(self):
        self.first_name = ''
        self.last_name = ''
        self.email = ''
        self.id_number = ''
        self.phone = ''


people = []

def detail():
    for i in person:
        print (i)

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


def update():

	show()
	print ()
	op = int(input("Ingrese el numero de la persona que desea actualizar: "))
	op = - 1
	print()
	person = Person()
	people.pop(op)
	person.first_name = input ("Ingrese el nombre: ")
	person.last_name = input ("Ingrese el apellido: ")
	person.email = input ("Ingrese el correo: ")
	person.id_number = input ("Ingrese la cedula: ")
	person.phone = input ("Ingrese el Telefono: ")
	people.insert(op, person)
	print()
	print("Lista actualizada: ")
	show()		

def delete():
	show()
	print()
	op = int(input("Ingrese el numero de la persona que desea Eliminar: "))
	op = op - 1
	print()
	people.pop(op)


def show():
    print()
    i = 1
    print('Lista de Personas')
    print('Nro  |  Nombre  |  Apellido  |  Correo  |  Cédula  |  Teléfono  |')
    for person in people:
        print( "#", i , " | ",
            person.first_name + ' | ' + person.last_name + ' | ' +
            person.email + ' | ' + person.id_number + ' | ' + person.phone)
        		
        i += 1
    print()



def menu():
    print()
    band = True
    while band:
        print('1. Registrar')
        print('2. Actualizar')
        print('3. Eliminar')
        print('4. Mostrar Lista')
        print('5. Salir')
        print()
        option = int(input('Elija una opción: '))
        if option == 1:
            create()
        elif option == 2:
            update()
            pass
        elif option == 3:
            delete()
            pass
        elif option == 4:
            show()
        elif option == 5:
            band = False
            print('Has salido de la aplicación.')


if __name__ == '__main__':
    print ('Bienvenido al Registro de Personas: ')
    menu()