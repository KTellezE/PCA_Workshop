# ex01_invoice_calculator (.NET)

**Timebox:** 10 minutos.

## Objetivo
Refactorizar reglas de cálculo (orden de aplicación, validaciones) sin cambiar el comportamiento.

## Tarea
Implementa `InvoiceCalculatorAfter.Total(...)` para que sea equivalente a `InvoiceCalculatorBefore.Total(...)` y pase el test de equivalencia.

## Restricciones
- No cambies `InvoiceCalculatorBefore.cs` ni los tests.
- No agregues dependencias.
- Mantén la firma pública:
  - `public static decimal Total(decimal subtotal, bool isVip, bool hasCoupon, bool isInternational)`

## Cómo validar
Desde `dotnet/ex01_invoice_calculator`:
- `dotnet test`

## Prompt (consulta lineal)
Desde la raíz del repo:
- `bash prompts/make_prompt.sh dotnet/ex01_invoice_calculator`

