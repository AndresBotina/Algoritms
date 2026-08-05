# 🧠 Algoritms

> Repositorio personal para **practicar, estudiar y resolver algoritmos**.
> La meta no es coleccionar soluciones: es afilar la lógica de programación.

---

## ¿De qué va esto?

Aquí vive todo lo que hago para mejorar como programador:

- **Practicar** — repetir hasta que los patrones salgan solos.
- **Estudiar** — entender *por qué* funciona una solución, no solo que funcione.
- **Resolver** — problemas de plataformas, de entrevistas, de cursos o de puro gusto.

Cada archivo es un intento de pensar mejor. Si una solución quedó fea pero la
entendí, se queda: el historial también enseña.

---

## Estructura

```
.
├── README.md
├── estructuras-de-datos/   # arrays, listas, pilas, colas, árboles, grafos, hash
├── algoritmos/
│   ├── busqueda/           # lineal, binaria, BFS, DFS
│   ├── ordenamiento/       # bubble, insertion, merge, quick, heap
│   ├── recursion/          # backtracking, divide y vencerás
│   ├── programacion-dinamica/
│   └── greedy/
├── retos/                  # LeetCode, HackerRank, Codeforces, etc.
└── notas/                  # apuntes, complejidades, trucos que se olvidan
```

> Las carpetas se crean a medida que hacen falta. Nada de estructura vacía
> esperando a ser llenada.

---

## Cómo trabajo cada problema

1. **Leer y entender.** Escribir el enunciado con mis palabras.
2. **Casos de prueba a mano.** Al menos uno normal y dos bordes.
3. **Fuerza bruta primero.** Que funcione, aunque sea lento.
4. **Optimizar.** ¿Dónde se va el tiempo? ¿Qué estructura lo arregla?
5. **Anotar la complejidad.** Tiempo y espacio, arriba del archivo.

Plantilla de encabezado que uso en cada solución:

```
/*
 * Problema : <nombre / enlace>
 * Idea     : <una o dos líneas con la intuición>
 * Tiempo   : O(?)
 * Espacio  : O(?)
 * Aprendí  : <lo que no sabía antes de resolverlo>
 */
```

---

## Chuleta de complejidades

| Operación                  | Promedio   | Peor caso  |
|----------------------------|------------|------------|
| Búsqueda binaria           | O(log n)   | O(log n)   |
| Merge / Heap sort          | O(n log n) | O(n log n) |
| Quick sort                 | O(n log n) | O(n²)      |
| Hash table (buscar)        | O(1)       | O(n)       |
| BFS / DFS en grafo         | O(V + E)   | O(V + E)   |
| Árbol binario de búsqueda  | O(log n)   | O(n)       |

---

## Reglas de la casa

- Sin copiar y pegar sin entender. Si no lo puedo explicar, no lo aprendí.
- Un problema al día vale más que veinte el domingo.
- Si me trabo más de 40 minutos: leo la pista, resuelvo, y lo repito en frío días después.
- Los errores también se comitean. El progreso se ve en el historial.

---

## Progreso

| Tema                    | Estado        |
|-------------------------|---------------|
| Estructuras de datos    |  Por iniciar |
| Búsqueda y ordenamiento |  Por iniciar |
| Recursión               |  Por iniciar |
| Programación dinámica   |  Por iniciar |
| Grafos                  |  Por iniciar |

---

*Hecho con paciencia, café y muchos casos de prueba fallidos.* ☕
