# Ejemplos ejecutables

Un archivo por versión. Son *file-based apps*: no necesitan proyecto.

| Archivo | Muestra | SDK mínimo |
|---|---|---|
| [`net05-records.cs`](net05-records.cs) | C# 9: `record`, `with`, patrones | 10 |
| [`net06-consolidacion.cs`](net06-consolidacion.cs) | `DateOnly`, `PriorityQueue`, LINQ | 10 |
| [`net07-matematica-generica.cs`](net07-matematica-generica.cs) | `INumber<T>`, list patterns, `GeneratedRegex` | 10 |
| [`net08-rendimiento.cs`](net08-rendimiento.cs) | Colecciones, `Frozen`, `SearchValues`, `TimeProvider` | 10 |
| [`net09-adaptacion.cs`](net09-adaptacion.cs) | `params Span`, `Lock`, `Task.WhenEach`, `CountBy` | 10 |
| [`net10-madurez.cs`](net10-madurez.cs) | `extension`, `field`, `LeftJoin`, JSON estricto | 10 |
| [`net11-uniones.cs`](net11-uniones.cs) | `union`, `closed`, `Decimal64`, Zstandard | 11 RC |

```bash
dotnet run ejemplos/net10-madurez.cs
```

> Los archivos usan el SDK instalado, aunque muestren funciones de versiones anteriores. El SDK de .NET 10 es el mínimo
> porque las *file-based apps* llegaron en esa versión.

`tools/validar_ejemplos.sh` compila y ejecuta todos.
