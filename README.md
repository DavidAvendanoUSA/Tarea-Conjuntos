# Tarea Conjuntos

Analizar gramáticas formales y calcular los conjuntos FIRST y FOLLOW de cada símbolo no terminal.

---

## ¿Qué es?

Este repositorio contiene una pequeña herramienta que permite leer una gramática escrita en un archivo de texto y obtener, de forma automática, los conjuntos:

- FIRST (Primeros)
- FOLLOW (Siguientes)

Esto es útil en cursos de compiladores, lenguajes formales y análisis sintáctico, ya que permite estudiar cómo se derivan los símbolos dentro de una gramática libre de contexto.

---

## ¿Qué hace?

El programa realiza lo siguiente:

- Lee una gramática desde un archivo `.txt`
- Identifica los no terminales
- Calcula el conjunto FIRST para cada no terminal
- Calcula el conjunto FOLLOW para cada no terminal
- Muestra los resultados en consola

La lógica principal está implementada en `tarea.py`, y la gramática se define en archivos como `gramatica.txt` o `gramatica_2.txt`.

## Estructura del proyecto

```text
Tarea-Conjuntos/
├── tarea.py
├── gramatica.txt
├── gramatica_2.txt
├── README.md
└── .gitignore
```

---

## Descripción de cada archivo

### `tarea.py`
Archivo principal del proyecto. Aquí se encuentra la lógica para:

- Parsear la gramática
- Determinar si un símbolo es terminal o no terminal
- Calcular FIRST
- Calcular FOLLOW
- Imprimir los resultados en pantalla

Este script recibe como argumento la ruta del archivo de gramática que se desea analizar.

### `gramatica.txt`
Archivo de ejemplo con una gramática simple. Contiene producciones en formato:

```text
S -> A B uno
A -> dos B
A -> ε
B -> C D
B -> tres
B -> ε
C -> cuatro A B
C -> cinco
D -> seis
D -> ε
```

### `gramatica_2.txt`
Segundo ejemplo de gramática con una estructura distinta. Sirve para probar que el algoritmo funciona con múltiples variantes de producción.

### `README.md`
Documento explicativo del proyecto con instrucciones de uso, estructura y detalles generales.

---

## Requisitos

- Python 3.x
- No se requieren librerías externas
- Solo se usa la biblioteca estándar de Python

## Cómo ejecutarlo

Desde la terminal, escribe:

```bash
python tarea.py gramatica.txt
```

o:

```bash
python3 tarea.py gramatica_2.txt
```

El programa espera recibir como argumento el nombre del archivo de gramática que se quiere analizar.

Ejemplo:

```bash
python tarea.py gramatica.txt
```

---

## Formato de la gramática

Las reglas deben escribirse con este formato:

```text
NoTerminal -> Produccion1 Produccion2 Produccion3
```

Cada símbolo se separa por espacios. Por ejemplo:

```text
S -> A B uno
```

También se puede usar `ε` para representar producción vacía, por ejemplo:

```text
A -> ε
```

---

## Ejemplo de uso

Supongamos que ejecutas:

```bash
python tarea.py gramatica.txt
```

La salida:

<img width="950" height="554" alt="image" src="https://github.com/user-attachments/assets/4c913e81-b5e3-4ef0-aa6f-8cccd50d9a34" />

---

## ¿Qué son FIRST y FOLLOW?

### FIRST
El conjunto FIRST de un símbolo no terminal contiene todos los terminales que pueden aparecer al inicio de una derivación de ese símbolo.

Ejemplo:

```text
FIRST(A) = {dos, tres, ε}
```

### FOLLOW
El conjunto FOLLOW de un símbolo no terminal contiene todos los terminales que pueden aparecer justo después de ese símbolo en alguna derivación.

Ejemplo:

```text
FOLLOW(S) = {$}
```

## Notas importantes

- El programa asume que la gramática está en una forma simple, lineal y escrita con una regla por línea.
- El archivo de entrada debe estar codificado en UTF-8.
- Debe pasarse correctamente la ruta o nombre del archivo como argumento.

---

## Objetivo

Aprender:

- Gramáticas libres de contexto
- Conjuntos FIRST
- Conjuntos FOLLOW
- Conceptos básicos de compiladores

---

## Integrantes
- David Avendaño
- Brayan Paredes
- Laura Niño
