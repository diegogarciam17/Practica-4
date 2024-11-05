import random

# Definimos los protagonistas, ubicaciones y herramientas
protagonistas = [
    {"nombre": "Juan", "ocupacion": "Piloto"},
    {"nombre": "Ana", "ocupacion": "Abogada"},
    {"nombre": "Diego", "ocupacion": "Programador"},
    {"nombre": "Laura", "ocupacion": "Músico"},
    {"nombre": "Andrés", "ocupacion": "Arquitecto"}
]

ubicaciones = ["Oficina", "Parque", "Restaurante", "Gimnasio", "Teatro"]
herramientas = ["Bate de béisbol", "Llave inglesa", "Martillo", "Veneno", "Cuerda"]

# Historias para cada incidente
historias_incidentes = {
    "Juan": [
        "Ana quería que Juan dejara de trabajar en el proyecto y decidió apartarlo del camino.",
        "Diego pensaba que Juan estaba interfiriendo en su trabajo y quería detenerlo.",
        "Laura estaba molesta con Juan porque él había rechazado colaborar en un evento importante.",
        "Andrés culpaba a Juan de haber interferido en una de sus propuestas importantes."
    ],
    "Ana": [
        "Juan estaba molesto con Ana por divulgar información importante del proyecto.",
        "Diego sospechaba que Ana estaba interfiriendo con su trabajo y quería enfrentarse a ella.",
        "Laura tenía celos del éxito de Ana y decidió vengarse.",
        "Andrés perdió la confianza en Ana después de un desacuerdo en un proyecto."
    ],
    "Diego": [
        "Juan descubrió que Diego estaba utilizando datos sin permiso y decidió confrontarlo.",
        "Ana estaba preocupada de que Diego pudiera descubrir sus planes y quería detenerlo.",
        "Laura pensaba que Diego estaba interfiriendo con su carrera musical y quería apartarlo.",
        "Andrés tenía problemas con Diego porque este había intervenido en uno de sus proyectos."
    ],
    "Laura": [
        "Juan no perdonaba a Laura por haber arruinado un evento importante.",
        "Ana descubrió que Laura estaba manipulando ciertos aspectos del proyecto y decidió enfrentarse a ella.",
        "Diego se sintió traicionado cuando Laura compartió información importante sin permiso.",
        "Andrés perdió un patrocinio importante debido a los rumores difundidos por Laura."
    ],
    "Andrés": [
        "Juan quería vengarse de Andrés por haberse apropiado de una idea suya.",
        "Ana estaba molesta porque Andrés decidió abandonar un proyecto en el que trabajaban juntos.",
        "Diego había descubierto que Andrés estaba utilizando técnicas poco éticas en su trabajo.",
        "Laura quería apartar a Andrés por haber terminado una relación de manera poco amistosa."
    ]
}

# Historias para confirmación o negación de ubicaciones, ajustadas para dar sentido lógico
def generar_historial_ubicaciones(sospechosos, culpable_nombre):
    ubicaciones_declaraciones = []
    for sospechoso in sospechosos:
        if sospechoso["nombre"] == culpable_nombre:
            ubicaciones_declaraciones.append(f"Nadie puede confirmar el paradero de {sospechoso['nombre']} durante el incidente.")
        else:
            ubicacion_aleatoria = random.choice(ubicaciones)
            ubicaciones_declaraciones.append(f"{sospechoso['nombre']} afirma que estaba en {ubicacion_aleatoria} durante el incidente.")
    return ubicaciones_declaraciones

# Función para iniciar una sesión
def iniciar_sesion():
    # Elegir al azar el incidente en el que un protagonista es atacado
    victima = random.choice(protagonistas)
    sospechosos = [p for p in protagonistas if p != victima]
    culpable = random.choice(sospechosos)
    herramienta = random.choice(herramientas)
    ubicacion = random.choice(ubicaciones)

    # Guardar la solución
    solucion = {
        "culpable": culpable["nombre"],
        "herramienta": herramienta,
        "ubicacion": ubicacion,
        "victima": victima["nombre"]
    }
    
    historias = historias_incidentes[victima["nombre"]]
    ubicaciones_declaraciones = generar_historial_ubicaciones(sospechosos, culpable["nombre"])
    return solucion, sospechosos, historias, ubicaciones_declaraciones

# Función para hacer preguntas y obtener pistas
def realizar_pregunta(sospechosos, historias, ubicaciones_declaraciones, intentos_restantes):
    print(f"\nTe quedan {intentos_restantes} intentos para resolver el incidente.")
    print("Opciones: ")
    print("1. Preguntar los motivos de los sospechosos")
    print("2. Preguntar dónde estaban los sospechosos")
    print("3. Preguntar qué herramienta estaba cerca de los sospechosos")
    print("4. Preguntar si los sospechosos confirman el paradero de otros sospechosos")
    print("5. Hacer una acusación")
    opcion = input("Selecciona una opción (1-5): ")

    if opcion == "1":
        for i, sospechoso in enumerate(sospechosos):
            print(f"{sospechoso['nombre']} ({sospechoso['ocupacion']}): {historias[i]}")
    elif opcion == "2":
        for sospechoso in sospechosos:
            ubicacion_aleatoria = random.choice(ubicaciones)
            print(f"{sospechoso['nombre']} estaba en {ubicacion_aleatoria}.")
    elif opcion == "3":
        for sospechoso in sospechosos:
            herramienta_aleatoria = random.choice(herramientas)
            print(f"Cerca de {sospechoso['nombre']} había un(a) {herramienta_aleatoria}.")
    elif opcion == "4":
        for ubicacion in ubicaciones_declaraciones:
            print(ubicacion)
    elif opcion == "5":
        sospechoso = input("¿Quién es el culpable?: ")
        herramienta_pregunta = input("¿Cuál fue la herramienta utilizada?: ")
        ubicacion_pregunta = input("¿Dónde ocurrió el incidente?: ")
        return sospechoso, herramienta_pregunta, ubicacion_pregunta
    else:
        print("Opción no válida. Intenta de nuevo.")
    return None, None, None

# Función principal para jugar
def main():
    jugar_otra_vez = True
    while jugar_otra_vez:
        solucion, sospechosos, historias, ubicaciones_declaraciones = iniciar_sesion()
        print(f"La víctima es: {solucion['victima']}")
        resuelto = False
        intentos = 5
        while not resuelto and intentos > 0:
            sospechoso, herramienta, ubicacion = realizar_pregunta(sospechosos, historias, ubicaciones_declaraciones, intentos)
            intentos -= 1
            if sospechoso:
                if (sospechoso == solucion["culpable"] and
                    herramienta == solucion["herramienta"] and
                    ubicacion == solucion["ubicacion"]):
                    print("¡Felicidades! Has resuelto el incidente correctamente.")
                    resuelto = True
                else:
                    print("La acusación es incorrecta. Sigue investigando.")
        if not resuelto:
            print("\nLo siento, se te han acabado los intentos. No lograste resolver el incidente.")
        print(f"La solución era: Culpable: {solucion['culpable']}, Herramienta: {solucion['herramienta']}, Ubicación: {solucion['ubicacion']}")
        
        jugar_otra_vez = input("¿Quieres jugar otra vez? (s/n): ").lower() == 's'

if __name__ == "__main__":
    main()
