from applorenzo.models import Familiar

Familiar(nombre="Facundo", direccion="Los Colibríes 2714", numero_pasaporte=123123).save()
Familiar(nombre="Marge", direccion="Calle Falsa 123", numero_pasaporte=890890).save()
Familiar(nombre="Gonzalo", direccion="Hernandarias 945", numero_pasaporte=345345).save()
Familiar(nombre="Jésica", direccion="Belgrano 1345", numero_pasaporte=567567).save()

print("Se cargaron con éxito los usuarios de pruebas")