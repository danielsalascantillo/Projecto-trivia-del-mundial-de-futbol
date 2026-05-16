import random

PREGUNTAS = {
    "Facil": [
        {
            "pregunta": "¿Que seleccion ha ganado mas Copas del Mundo?",
            "opciones": ["Alemania", "Argentina", "Italia", "Brasil"],
            "respuesta": "D",
            "dato": "Brasil tiene 5 titulos: Suecia 58, Chile 62, México 70, EEUU 94 y Corea-Japón 2002."
        },
        {
            "pregunta": "¿Cual fue la primera selección en ser Bicampeona del mundo (Ganar dos mundiales seguidos)?",
            "opciones": ["Uruguay", "Brasil", "Italia", "Alemania"],
            "respuesta": "C",
            "dato": "Italia fue la primera Bicampeona del mundo al ganar las ediciones de Italia 34 y Francia 38."
        },
        {
            "pregunta": "¿Quién fue él único jugador capáz de ganar 3 mundiales?",
            "opciones": ["Cafu", "Maradona", "Pelé", "Garrincha"],
            "respuesta": "C",
            "dato": "O rei fue el único en ganar 3 mundiales, Suecia 58, Chile 62 y México 70."
        },
        {
            "pregunta": "¿Que pais organizará el Mundial 2034?",
            "opciones": ["Siria", "Arabia Saudí", "China", "España"],
            "respuesta": "B",
            "dato": "Arabia Saudita sera la sede del mundial 2034, siendo el tercero de Asia en serlo."
        },
        {
            "pregunta": "¿Que seleccion gano el Mundial de Alemania 2006?",
            "opciones": ["Francia", "Brasil", "Italia", "España"],
            "respuesta": "C",
            "dato": "Italia venció a Francia en 2006 por penales, siendo de las finales mas recordadas de la historia."
        },
        {
            "pregunta": "¿En que país se jugo el primer Mundial de futbol?",
            "opciones": ["Francia", "Italia", "Uruguay", "Argentina"],
            "respuesta": "C",
            "dato": "Uruguay 1930 fue el anfitrión del primer Mundial de la historia."
        },
        {
            "pregunta": "¿En que mundial fue introducida la tarjeta roja?",
            "opciones": ["Uruguay 30", "Italia 90", "Francia 98", "México 70"],
            "respuesta": "D",
            "dato": "La tarjeta roja fue introducida por Ken Aston en el Mundial de 1970."
        },
        {
            "pregunta": "¿Quien gano el Mundial de 2014 en Brasil?",
            "opciones": ["Brasil", "Argentina", "Francia", "Alemania"],
            "respuesta": "D",
            "dato": "Alemania vencio 1-0 a Argentina en la final con gol de Gotze en prorroga."
        },
        {
            "pregunta": "¿Cuantos goles marco Lionel Messi en el Mundial 2022?",
            "opciones": ["7", "6", "5", "8"],
            "respuesta": "A",
            "dato": "Messi marco 7 goles en Qatar 2022 y gano el Balon de Oro del torneo."
        },
        {
            "pregunta": "¿Cual fue el primer mundial disputado por la selección colombia?",
            "opciones": ["Chile 62", "Italia 90", "Argentina 78", "EEUU 94"],
            "respuesta": "A",
            "dato": "El primer mundial de Colombia fue Chile 62, con el recordado gol olímpico a Lev Yashin."
        },
    ],
    "Medio": [
        {
            "pregunta": "¿En que año se jugo el Mundial en Suiza?",
            "opciones": ["1946", "1954", "1934", "1958"],
            "respuesta": "B",
            "dato": "Suiza 54 es recordado como uno de los mejores mundiales de la historia, con el promedio de gol mas alto de la historia."
        },
        {
            "pregunta": "¿Cuantos goles marco Miroslav Klose en Mundiales (record historico)?",
            "opciones": ["14", "15", "16", "17"],
            "respuesta": "C",
            "dato": "Klose marco 16 goles en cuatro Mundiales (2002-2014) con Alemania."
        },
        {
            "pregunta": "¿Quien gano el Balon de Oro del Mundial 2014?",
            "opciones": ["Lionel Messi", "Manuel Neuer", "Arjen Robben", "James Rodriguez"],
            "respuesta": "A",
            "dato": "Messi gano el Balon de Oro en Brasil 2014, en una polémica decisión."
        },
        {
            "pregunta": "¿Cuantos paises participaron en el Mundial de Qatar 2022?",
            "opciones": ["16", "24", "32", "48"],
            "respuesta": "C",
            "dato": "Qatar 2022 tuvo 32 selecciones. Desde 2026 seran 48."
        },
        {
            "pregunta": "¿En que Mundial Maradona debutó?",
            "opciones": ["España 82", "Mexico 86", "Italia 90", "Argentina 78"],
            "respuesta": "A",
            "dato": "Su debut en mundiales fue en España 82, aunque es el menos iconico de los 4 mundiales que disputo."
        },
        {
            "pregunta": "¿Quién es el maximo goleador Brasileño en mundiales?",
            "opciones": ["Neymar", "Romario", "Pelé", "Ronaldo Nazario"],
            "respuesta": "D",
            "dato": "Ronaldo Nazario es el maximo goleador de Brasil en mundiales y lo era en general hasta que lo supero Miroslav Klose."
        },
        {
            "pregunta": "¿Quien fue el maximo goleador del Mundial 2018?",
            "opciones": ["Cristiano Ronaldo", "Harry Kane", "Romelu Lukaku", "Antoine Griezmann"],
            "respuesta": "B",
            "dato": "Harry Kane marco 6 goles en Rusia 2018 y gano la Bota de Oro del torneo."
        },
        {
            "pregunta": "¿En que pais(es) se celebrara el Mundial 2030?",
            "opciones": ["Australia", "Arabia Saudita", "EE.UU., Canada y Mexico", "España, Portugal y Marruecos"],
            "respuesta": "D",
            "dato": "El Mundial 2030 tendra 48 equipos en ciudades de Portugal, España y Marruecos, con ligeras aportaciones de algunos sudamericanos."
        },
        {
            "pregunta": "¿Que jugador es conocido como 'El hombre que murío de pie'?",
            "opciones": ["Roberto Baggio", "Zinedine Zidane", "Luis Figo", "Thierry Henry"],
            "respuesta": "A",
            "dato": "Roberto Baggio obtuvo esta este infame apodo luego de su fallo en la tanda de penales de la final del 94."
        },
        {
            "pregunta": "¿Cual fue el resultado de la final del Mundial 2014 (Alemania vs Argentina)?",
            "opciones": ["1-0 (reglamentario)", "2-1", "1-0 (prorroga)", "0-0 y penales", "1-1 y penales"],
            "respuesta": "C",
            "dato": "Mario Gotze marco en el minuto 113 de prorroga para dar a Alemania su 4a estrella."
        },
    ],
    "Dificil": [
        {
            "pregunta": "¿Quien marco el primer gol de la historia de los Mundiales?",
            "opciones": ["Hector Castro", "Lucien Laurent", "Bert Patenaude", "Pedro Cea"],
            "respuesta": "B",
            "dato": "El frances Lucien Laurent marco el primer gol mundialista el 13 de julio de 1930 ante Mexico."
        },
        {
            "pregunta": "¿Cual es el partido con la mayor goleada en la historia de los Mundiales?",
            "opciones": ["Brasil - Suecia (Suecia 58)", "Austria - Suiza (Suiza 54)", "Hungria - El Salvador (España 82)", "Alemania - Arabia Saudita (Corea-Japón 2002)"],
            "respuesta": "C",
            "dato": "Hungría - El salvador en 1982 con un resultado de 10 - 1, es el partido con la mayor goleada de la historia de los mundiales."
        },
        {
            "pregunta": "¿Que seleccion gano el Mundial de 1950 en el famoso Maracanazo?",
            "opciones": ["Brasil", "Uruguay", "España", "Suecia"],
            "respuesta": "B",
            "dato": "Uruguay vencio 2-1 a Brasil ante unos 200.000 espectadores. No hubo partido final oficial ese año."
        },
        {
            "pregunta": "¿En que año se introdujo el 'Ojo de halcón' en los mundiales?",
            "opciones": ["2014", "2018", "2010", "2022"],
            "respuesta": "A",
            "dato": "El 'Ojo de halcón' debuto en el Mundial de Brasil 2014 y se uso por primera vez en fase de grupos."
        },
        {
            "pregunta": "¿Que seleccion africana llego mas lejos en la historia de los Mundiales?",
            "opciones": ["Nigeria", "Camerun", "Ghana", "Marruecos"],
            "respuesta": "D",
            "dato": "Marruecos alcanzo las semifinales en Qatar 2022, el mejor resultado de Africa en un Mundial."
        },
        {
            "pregunta": "¿Cuantas finales consecutivas disputo Lothar Matthaus (record)?",
            "opciones": ["5", "4", "2", "3"],
            "respuesta": "D",
            "dato": "Matthaus jugo 3 finales consecutivas en España 82, México 86 e Italia 90, ganando solo la última."
        },
        {
            "pregunta": "¿Que seleccion goleo 7-0 a Corea del Norte en el Mundial de Sudáfrica 2010?",
            "opciones": ["Brasil", "Portugal", "Argentina", "Alemania"],
            "respuesta": "B",
            "dato": "Portugal derrotó 7-0 a Corea del Norte en 2010, siendo la mayor goleada de la historia reciente de los mundiales junto con la de España a Costa Rica en 2022."
        },
        {
            "pregunta": "¿Quien fue el portero de Brasil en la final del Mundial 2002 contra Alemania?",
            "opciones": ["Marcos", "Dida", "Rogerio Ceni", "Julio Cesar"],
            "respuesta": "A",
            "dato": "Marcos era el portero de Brasil; Alemania contaba con Oliver Khan."
        },
        {
            "pregunta": "¿En que Mundial se uso por primera vez la tanda de penaltis?",
            "opciones": ["Argentina 1978", "España 1982", "Mexico 1986", "Italia 1990"],
            "respuesta": "B",
            "dato": "La tanda de penaltis se uso por primera vez en Espana 1982, en el partido Alemania Occ. vs Francia."
        },
        {
            "pregunta": "¿Cuantos Mundiales gano Didier Deschamps como jugador y entrenador combinados?",
            "opciones": ["1", "2", "3", "4"],
            "respuesta": "B",
            "dato": "Deschamps gano el Mundial 1998 como capitan de Francia y el 2018 como seleccionador."
        },
    ],
}

CATEGORIAS = ["Facil", "Medio", "Dificil"]
LETRAS = ["A", "B", "C", "D"]


def mostrar_pregunta(numero, total, categoria, pregunta_data):
    print("\n" + "-" * 50)
    print(f"Categoria: {categoria} | Pregunta {numero} de {total}")
    print()
    print(pregunta_data["pregunta"])
    print()
    for letra, opcion in zip(LETRAS, pregunta_data["opciones"]):
        print(f"  {letra}) {opcion}")
    print()


def pedir_respuesta():
    while True:
        entrada = input("Tu respuesta (A/B/C/D): ").strip().upper()
        if entrada in LETRAS:
            return entrada
        print("Opcion invalida. Escribe A, B, C o D.")


def evaluar_respuesta(eleccion, pregunta_data):
    correcta = pregunta_data["respuesta"]
    if eleccion == correcta:
        print("\nExcelente, esa es la respuesta correcta.")
        acierto = True
    else:
        idx = LETRAS.index(correcta)
        texto = pregunta_data["opciones"][idx]
        print(f"\nTe equivocaste. {correcta}) {texto}")
        acierto = False
    print(f"Dato: {pregunta_data['dato']}")
    return acierto


def jugar_categoria(categoria, previas, total_global):
    preguntas = PREGUNTAS[categoria].copy()
    random.shuffle(preguntas)
    puntaje = 0

    for i, pregunta_data in enumerate(preguntas, start=1):
        mostrar_pregunta(previas + i, total_global, categoria, pregunta_data)
        eleccion = pedir_respuesta()
        if evaluar_respuesta(eleccion, pregunta_data):
            puntaje += 1
        input("\nPresiona Enter para continuar...")

    print("\n" + "=" * 50)
    print(f"Resultado {categoria}: {puntaje}/{len(preguntas)}")
    print("=" * 50)
    input("Presiona Enter para la siguiente categoria...")
    return puntaje


def mostrar_resultado_final(puntajes):
    total = sum(t for _, t in puntajes.values())
    aciertos = sum(p for p, _ in puntajes.values())
    porcentaje = round(aciertos / total * 100)

    print("\n" + "=" * 50)
    print("RESULTADO FINAL")
    print("=" * 50)
    for cat in CATEGORIAS:
        p, t = puntajes[cat]
        print(f"  {cat}: {p}/{t}")
    print(f"\n  Total: {aciertos}/{total} ({porcentaje}%)")

    if porcentaje >= 90:
        nivel = "Eres un experto."
    elif porcentaje >= 70:
        nivel = "Le sabes al futbol."
    elif porcentaje >= 50:
        nivel = "Algo sabes."
    elif porcentaje >= 30:
        nivel = "Eres un aficionado."
    else:
        nivel = "El fútbol no es lo tuyo."
    print(f"\n  {nivel}")
    print("=" * 50)


def main():
    print("\n" + "=" * 50)
    print("TRIVIA DEL MUNDIAL")
    print("=" * 50)
    print("30 preguntas - 3 categorias: Facil, Medio, Dificil")
    print("Responde con A, B, C o D.")

    while True:
        total_global = sum(len(v) for v in PREGUNTAS.values())
        puntajes = {}
        acumulado = 0

        for categoria in CATEGORIAS:
            print(f"\n--- {categoria.upper()} ---")
            puntaje = jugar_categoria(categoria, acumulado, total_global)
            puntajes[categoria] = (puntaje, len(PREGUNTAS[categoria]))
            acumulado += len(PREGUNTAS[categoria])

        mostrar_resultado_final(puntajes)

        print()
        otra = input("Quieres jugar de nuevo? (s/n): ").strip().lower()
        if otra != "s":
            print("\nGracias por participar.")
            break


if __name__ == "__main__":
    main()