try:
    from .estudiante import Estudiante
    from .docente import Docente
except ImportError:
    from estudiante import Estudiante
    from docente import Docente

estudiantes = [
    Estudiante("Alexander", "Juela", "0150287894", "0983680684", "ajuela425@gmail.com", 19, "Miraflores", "PROGRAMACION", [10, 9, 8, 7, 6]),
    Estudiante("Andersson", "Bermejo", "0107945529", "0990854589", "mauriciober23@gmail.com", 22, "Miraflores", "TDSU", [10, 10, 10, 10, 10]),
    Estudiante("Alex", "Minchala", "0107945529", "0990854589", "alexm@gmail.com", 15, "Redondel", "TDSU", [9, 4, 10, 10, 10]),
    Estudiante("Lisa", "Simpson", "0107945529", "0990854589", "lisa@gmail.com", 8, "Miraflores", "TDSU", [10, 10, 8, 7, 8]),
    Estudiante("Pablo", "Pablin", "0107945529", "0990854589", "mauriciober23@gmail.com", 45, "Parque Industrial", "TDSU", [10, 10, 10, 10, 10]),
]

print("ESTUDIANTES")
for estudiante in estudiantes:
    print(estudiante.validar_edad())
    print(estudiante.promedio())
    print()

docentes = [
    Docente("Andersson", "Bermejo", "0107945529", "0990854589", "mauriciober23@gmail.com", 22, "Miraflores", "POO II", 15),
    Docente("Maria", "Carchi", "0101234567", "0987654321", "maria.carchi@gmail.com", 35, "El Valle", "BASE DE DATOS", 18),
    Docente("Carlos", "Torres", "0102345678", "0987654322", "carlos.torres@gmail.com", 28, "San Joaquin", "PROGRAMACION", 20),
    Docente("Ana", "Perez", "0103456789", "0987654323", "ana.perez@gmail.com", 42, "Totoracocha", "REDES", 12),
    Docente("Luis", "Vega", "0104567890", "0987654324", "luis.vega@gmail.com", 31, "Monay", "SISTEMAS OPERATIVOS", 16),
]

print("DOCENTES")
for docente in docentes:
    docente.calcular_salario()
    print(docente.validar_edad())
    print(docente)
    print()

