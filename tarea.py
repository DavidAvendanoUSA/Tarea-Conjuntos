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

                for simbolo in produccion:

                    if not es_no_terminal(simbolo, gramatica):

                        first[no_terminal].add(simbolo)
                        break

                    else:

                        for f in first[simbolo]:

                            if f != "ε":
                                first[no_terminal].add(f)

                        if "ε" not in first[simbolo]:
                            break

                else:

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

                    for j in range(i + 1, len(produccion)):

                        simbolo_der = produccion[j]

                        if not es_no_terminal(simbolo_der, gramatica):

                            siguientes[simbolo_actual].add(simbolo_der)
                            break

                        else:

                            for f in first[simbolo_der]:

                                if f != "ε":
                                    siguientes[simbolo_actual].add(f)

                            if "ε" not in first[simbolo_der]:
                                break

                    else:

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

    if "->" in line:

        no_terminales, productos = line.split("->")

        productos = productos.strip().split()

        if no_terminales.strip() not in dict_gramatica:
            dict_gramatica[no_terminales.strip()] = []

        dict_gramatica[no_terminales.strip()].append(productos)



first = calcular_first(dict_gramatica)

siguientes = calcular_siguientes(dict_gramatica, first)


print("\n gramatica")
print(dict_gramatica)

print("\n primeros")

for nt in first:
    print(f"P({nt}) = {first[nt]}")


print("\n siguientes")

for nt in siguientes:
    print(f"S({nt}) = {siguientes[nt]}")