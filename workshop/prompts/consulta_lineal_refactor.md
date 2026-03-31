# Prompt único (consulta lineal) para resolver ejercicios

Copia/pega este prompt en tu herramienta. Sustituye los bloques `{{...}}` por el contenido real de tu ejercicio.

---

Eres un ingeniero senior enfocado en refactorización segura y mejora continua.

OBJETIVO
- Implementa/refactoriza el archivo `after` para que pase el/los tests de equivalencia.
- Preserva el comportamiento observable definido por los tests (incluyendo salida por consola si el test la valida).

REGLAS
- No cambies `before` ni los tests.
- No agregues dependencias.
- Mantén la API pública (misma firma/mismo export/nombre de método según aplique).
- Manejo de errores: conserva excepciones/validaciones observables del `before`.

ENTRADA

## BEFORE (no modificar)
{{BEFORE_CODE}}

## TEST (no modificar)
{{TEST_CODE}}

## AFTER actual (a reemplazar)
{{AFTER_CODE}}

SALIDA (MUY IMPORTANTE)
- Devuelve **solo** el contenido final del archivo `after` (código completo).
- Sin explicaciones.
- Sin formato Markdown (sin ```).
- No incluyas el contenido de `before` ni del test.

