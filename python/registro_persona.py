# nombre, apellido, cedula, telefono, correo


class Person():
    """!
    Contiene los datos de las personas

    @author William Páez <paez.william8@gmail.com>
    @copyright <a href='​http://www.gnu.org/licenses/gpl-2.0.html'>
        GNU Public License versión 2 (GPLv2)</a>
    """

    def __init__(self):
        """!
        Método que inicializa la clase

        @author William Páez <paez.william8@gmail.com>
        """

        self.first_name = ''
        self.last_name = ''
        self.email = ''
        self.id_number = ''
        self.phone = ''


print('Bienvenido al Registro de Personas')
print()
person = Person()
person.first_namo = input('Nombres: ')
person.last_name = input('Apellidos: ')
person.email = input('Correo Electrónico: ')
person.id_number = input('Cédula de Identidad: ')
person.phone = input('Teléfono: ')
print()

print('Personas registradas:')
print('Nombres: ', person.first_namo)
print('Apellidos: ', person.last_name)
print('Correo Electrónico: ', person.email)
print('Cédula de Identidad: ', person.id_number)
print('phone: ', person.phone)
