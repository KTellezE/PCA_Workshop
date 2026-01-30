```text
[S] Situación
Eres un ingeniero senior enfocado en refactorización segura y mejora continua de código. Trabajas en un arquetipo/base de proyecto y ayudas a mejorar legibilidad, mantenibilidad y pruebas sin romper comportamiento.

[A] Acción
Cuando recibas código y objetivo:
1) Identifica smells (duplicación, complejidad cognitiva, complejidad cliclomática, nombres, acoplamiento, efectos secundarios, etc.).
2) Propón un plan de refactor en pasos pequeños.
3) Genera cambios concretos.
4) Explica brevemente el “por qué” de cada paso.

[L] Limitaciones
- No inventes APIs/funciones que no existan; si necesitas algo, dilo explícitamente.
- Evita cambios de comportamiento. Si detectas ambigüedad, señala riesgos.
- Mantén el estilo y convenciones del proyecto.
- Respuestas concisas y accionables; nada de teoría larga.

[T] Tono
Claro, pedagógico, práctico. Usa listas y bloques de código. Prioriza seguridad y verificabilidad.
```

```python
import csv
from datetime import datetime

import psycopg2

# MALA PRACTICA: credenciales hardcodeadas en el codigo
DB_HOST = "localhost"
DB_NAME = "etl_workshop"
DB_USER = "etl_user"
DB_PASSWORD = "etl_password"
DB_PORT = 5432

# MALA PRACTICA: path hardcodeado y dependiente del cwd
CSV_PATH = "data/raw/customers.csv"

# MALA PRACTICA: estado global compartido y sin cierre correcto
conn = psycopg2.connect(
    host=DB_HOST,
    dbname=DB_NAME,
    user=DB_USER,
    password=DB_PASSWORD,
    port=DB_PORT,
)
conn.autocommit = True  # MALA PRACTICA: sin transacciones
cur = conn.cursor()


def extract():
    # MALA PRACTICA: sin manejo de errores ni validaciones
    with open(CSV_PATH, newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def load_raw(rows):
    for row in rows:
        # MALA PRACTICA: concatenacion de SQL (inyeccion y errores por escape)
        sql = (
            "INSERT INTO raw_customers (id, first_name, last_name, email, birth_date, country, signup_date, amount_spent) "
            "VALUES ('{id}', '{first_name}', '{last_name}', '{email}', '{birth_date}', '{country}', '{signup_date}', '{amount_spent}')"
        ).format(**row)

        try:
            cur.execute(sql)
        except Exception:
            # MALA PRACTICA: se silencian errores
            pass


def transform_and_load():
    # MALA PRACTICA: SELECT * y sin limitar columnas
    cur.execute("SELECT * FROM raw_customers")
    rows = cur.fetchall()

    for row in rows:
        rid, first_name, last_name, email, birth_date, country, signup_date, amount_spent = row

        # MALA PRACTICA: transformaciones sin validacion
        full_name = (str(first_name) + " " + str(last_name)).upper()

        try:
            bd = datetime.strptime(str(birth_date), "%Y-%m-%d").date()
        except Exception:
            # MALA PRACTICA: default silencioso
            bd = datetime(1900, 1, 1).date()

        try:
            sd = datetime.strptime(str(signup_date), "%Y-%m-%d %H:%M:%S")
        except Exception:
            # MALA PRACTICA: usar fecha actual sin registrar
            sd = datetime.now()

        try:
            amount = float(str(amount_spent))
        except Exception:
            # MALA PRACTICA: se pierde el dato sin alertar
            amount = 0.0

        sql = (
            "INSERT INTO customers (customer_id, full_name, email, birth_date, country, signup_date, amount_spent) "
            "VALUES ({id}, '{full_name}', '{email}', '{birth_date}', '{country}', '{signup_date}', {amount})"
        ).format(
            id=rid,
            full_name=full_name,
            email=email,
            birth_date=bd,
            country=country,
            signup_date=sd,
            amount=amount,
        )

        try:
            cur.execute(sql)
        except Exception:
            # MALA PRACTICA: se ignoran violaciones de PK o errores de datos
            pass


def main():
    rows = extract()
    load_raw(rows)
    transform_and_load()
    # MALA PRACTICA: no se cierra la conexion ni el cursor


if __name__ == "__main__":
    main()

```