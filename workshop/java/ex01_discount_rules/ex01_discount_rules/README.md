# ex01_discount_rules (Java)

**Timebox:** 10 minutos.

## Objetivo
Refactorizar reglas de descuento (segmento/cupón/black friday) sin cambiar el comportamiento.

## Tarea
Implementa `DiscountCalculatorAfter.finalPrice(...)` para que sea equivalente a `DiscountCalculatorBefore.finalPrice(...)` y pase el test.

## Restricciones
- No cambies `DiscountCalculatorBefore.java` ni `DiscountEquivalenceTest.java`.
- No agregues dependencias.
- Mantén la firma pública exacta:
  - `public static double finalPrice(double price, String seg, boolean coupon, boolean bf)`

## Cómo validar
Desde `java/ex01_discount_rules/ex01_discount_rules`:
- `mvn test`

## Prompt (consulta lineal)
Desde la raíz del repo:
- `bash prompts/make_prompt.sh java/ex01_discount_rules/ex01_discount_rules`

