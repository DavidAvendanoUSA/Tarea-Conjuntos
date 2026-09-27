import sys


def es_no_terminal(simbolo, gramatica):
    return simbolo in gramatica


def calcular_first(gramatica):
    first = {}

    for no_terminal in gramatica:
        first[no_terminal] = set()

    cambio = True

    while cambio:
        cambio = False

        for no_terminal, producciones in gramatica.items():

            for produccion in producciones:

                tam_anterior = len(first[no_terminal])

                # Iteramos sobre cada símbolo de la producción
                puede_ser_epsilon = True
                
                for simbolo in produccion:

                    if not es_no_terminal(simbolo, gramatica):
                        # Es terminal
                        first[no_terminal].add(simbolo)
                        puede_ser_epsilon = False
                        break

                    else:
                        # Es no-terminal, agregamos sus primeros
                        for f in first[simbolo]:

                            if f != "ε":
                                first[no_terminal].add(f)

                        # Si no contiene epsilon, paramos
                        if "ε" not in first[simbolo]:
                            puede_ser_epsilon = False
                            break

                # Si todos los símbolos pueden ser epsilon, agregamos epsilon
                if puede_ser_epsilon:
                    first[no_terminal].add("ε")

                if len(first[no_terminal]) > tam_anterior:
                    cambio = True

    return first


def calcular_siguientes(gramatica, first):

    siguientes = {}

    for no_terminal in gramatica:
        siguientes[no_terminal] = set()

    simbolo_inicial = list(gramatica.keys())[0]
    siguientes[simbolo_inicial].add("$")

    cambio = True

    while cambio:
        cambio = False

        for no_terminal, producciones in gramatica.items():

            for produccion in producciones:

                for i in range(len(produccion)):

                    simbolo_actual = produccion[i]

                    if not es_no_terminal(simbolo_actual, gramatica):
                        continue

                    tam_anterior = len(siguientes[simbolo_actual])

                    # Miramos qué viene después del símbolo actual
                    for j in range(i + 1, len(produccion)):

                        simbolo_der = produccion[j]

                        if not es_no_terminal(simbolo_der, gramatica):
                            # Es terminal
                            siguientes[simbolo_actual].add(simbolo_der)
                            break

                        else:
                            # Es no-terminal, agregamos sus primeros (excepto epsilon)
                            for f in first[simbolo_der]:

                                if f != "ε":
                                    siguientes[simbolo_actual].add(f)

                            if "ε" not in first[simbolo_der]:
                                break

                    else:
                        # Si llegamos aquí, todos los símbolos después pueden ser epsilon
                        # Agregamos los siguientes del no-terminal actual
                        for s in siguientes[no_terminal]:
                            siguientes[simbolo_actual].add(s)

                    if len(siguientes[simbolo_actual]) > tam_anterior:
                        cambio = True

    return siguientes




with open(sys.argv[1], encoding="utf-8") as gramatica:

    contenido = gramatica.read()
    lines = contenido.splitlines()


dict_gramatica = {}

for line in lines:
    # Ignoramos líneas vacías
    if line.strip() == "":
        continue
        
    if "->" in line:

        no_terminales, productos = line.split("->")

        productos = productos.strip().split()

        if no_terminales.strip() not in dict_gramatica:
            dict_gramatica[no_terminales.strip()] = []

        dict_gramatica[no_terminales.strip()].append(productos)



first = calcular_first(dict_gramatica)

siguientes = calcular_siguientes(dict_gramatica, first)


print("\ngramatica")
print(dict_gramatica)

print("\nprimeros")

for nt in first:
    # Convertir a lista ordenada para salida consistente
    first_sorted = sorted(list(first[nt]))
    print(f"P({nt}) = {{{', '.join(first_sorted)}}}")


print("\nsiguientes")

for nt in siguientes:
    # Convertir a lista ordenada para salida consistente
    siguiente_sorted = sorted(list(siguientes[nt]))
    print(f"S({nt}) = {{{', '.join(siguiente_sorted)}}}")
