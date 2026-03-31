# Recetas para ejercicios menos repetitivos (mejora continua + refactor)

La repetición suele venir de practicar *siempre el mismo smell* (p. ej. `if/else` anidados) con *el mismo objetivo* (p. ej. “mejorar legibilidad”). Para variar sin perder foco, combina 4 ejes:

1) **Dominio**: pedidos, envíos, facturación, permisos, alertas, inventario, parsing de CSV, etc.  
2) **Smell principal**: condicionales, duplicación, estado global, side effects mezclados, validación dispersa, manejo de errores “silencioso”, etc.  
3) **Técnica**: tabla de decisión, estrategia, pipeline, separación core/IO, objetos de valor, inyección de dependencias, etc.  
4) **Restricción verificable**: “tests primero”, “máx. 3 pasos”, “sin cambiar firmas”, “sin nuevas deps”, “máx. N líneas por función”.

Usa estos prompts como “menú” (copia/pega) y rota el objetivo cada vez.

---

## 1) Diagnóstico (para no refactorizar por refactorizar)

**Prompt**

> Actúa como ingeniero senior. Lee el archivo `before` y el test existente.  
> 1) Lista 6–10 code smells concretos (con ejemplos del código).  
> 2) Prioriza (impacto × esfuerzo) y sugiere un “refactor objetivo” único (uno solo).  
> 3) Propón 3 micro-pasos que preserven comportamiento.  
> Restricciones: no cambies la interfaz pública ni el output observable.

---

## 2) “Tres caminos” (para variar el tipo de refactor)

**Prompt**

> Con el mismo `before`, propón 3 rutas de refactor *distintas* (A/B/C), cada una con:  
> - objetivo (p. ej. testabilidad / legibilidad / separación de responsabilidades / performance sin cambiar resultados)  
> - pasos mínimos  
> - riesgos  
> - criterio de terminado (“definition of done”)  
> Luego recomienda una ruta y justifica por qué.

---

## 3) Refactor incremental con límites (evita reescrituras)

**Prompt**

> Refactoriza en pasos pequeños. En cada paso: muestra el diff, explica el porqué en 1–2 líneas y ejecuta/actualiza los tests mínimos.  
> Límites:  
> - no más de 25 líneas modificadas por paso  
> - funciones nuevas ≤ 20 líneas  
> - no nuevas dependencias  
> - mismo comportamiento observable

---

## 4) “Golden master” / equivalencia (para refactors más libres)

**Prompt**

> Antes de tocar el código, crea/ajusta un test de equivalencia (“golden master”) que capture el comportamiento actual con casos representativos y edge cases.  
> Luego refactoriza con confianza (sin cambiar outputs) y demuestra que el test sigue pasando.

Idea: esto encaja con ejercicios como `node/ex01_pure_vs_io/test_equivalence.js` o `python/**/test.py`.

---

## 5) Revisión tipo PR (para convertir el ejercicio en aprendizaje)

**Prompt**

> Revisa mi refactor como si fuera un PR.  
> - Señala 5 mejoras concretas (nombres, cohesión, errores, diseño)  
> - Señala 3 riesgos (cambios de comportamiento, regresiones, performance)  
> - Sugiere 2 tests adicionales de alto valor  
> Manténte práctico y específico.

---

## 6) Generador de variantes (anti-repetición)

**Prompt**

> Genera 5 variantes del ejercicio sin repetir el patrón principal (no uses “extraer función + renombrar” como solución principal).  
> Para cada variante define:  
> - dominio distinto  
> - smell principal distinto  
> - técnica distinta  
> - 3 casos de prueba mínimos (inputs/outputs)  
> Mantén el tamaño del ejercicio pequeño (≤ 40 líneas de `before`).

---

## 7) Crear un ejercicio nuevo en el mismo formato del repo

**Prompt**

> Crea un nuevo ejercicio en formato `exNN_*` para este repo. Debe incluir:  
> - `before` con 2–3 smells intencionales  
> - `after` vacío o con TODOs  
> - un test de equivalencia o unit test mínimo  
> - un `README.md` corto con objetivo, restricciones y hints  
> Reglas: nada de dependencias nuevas; que corra con el tooling actual del proyecto.

---

## Sugerencia práctica de rotación

- Un día: **separación core/IO** (pure vs IO)  
- Otro día: **tabla de decisión** + tests de casos límite  
- Otro día: **manejo de errores explícito** (sin silencios)  
- Otro día: **diseño para testabilidad** (inyección de dependencias / puertos y adaptadores)  
- Otro día: **refactor de performance** (mismo resultado, menos trabajo)

