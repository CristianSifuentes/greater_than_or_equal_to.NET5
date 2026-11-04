<div align="center">

# 13 · Bibliotecas base

**System.Text.Json, LINQ, colecciones, red, compresión, numéricos y las API que reemplazan código propio**

[⬅ 12 · AOT y despliegue](12-aot-despliegue-y-contenedores.md) · [🏠 Índice](../README.md) · [14 · ASP.NET Core ➡](14-aspnet-core-y-blazor.md)

</div>

---

## Contenido

1. [Mapa de evolución](#1-mapa-de-evolución)
2. [System.Text.Json](#2-systemtextjson)
3. [LINQ](#3-linq)
4. [Colecciones](#4-colecciones)
5. [Cadenas y texto](#5-cadenas-y-texto)
6. [Numéricos](#6-numéricos)
7. [Tiempo, tareas y concurrencia](#7-tiempo-tareas-y-concurrencia)
8. [Red y HTTP](#8-red-y-http)
9. [Compresión y archivos](#9-compresión-y-archivos)
10. [Procesos](#10-procesos)
11. [Extensions: DI, opciones, configuración](#11-extensions-di-opciones-configuración)
12. [Código propio que ya puedes borrar](#12-código-propio-que-ya-puedes-borrar)
13. [Referencias](#13-referencias)

---

## 1. Mapa de evolución

| Área | .NET 5–6 | .NET 7–8 | .NET 9–10 | .NET 11 🆕 |
|---|---|---|---|---|
| JSON | Generador, `JsonNode` | Polimorfismo, contratos | `Schema`, `Strict`, `PipeReader` | Uniones, JSONL |
| LINQ | `Chunk`, `MaxBy` | Vectorización | `CountBy`, `LeftJoin`, `AsyncEnumerable` | `FullJoin` |
| Colecciones | `PriorityQueue` | `Frozen*` | `OrderedDictionary` | `BitArray` sobre `Span` |
| Texto | `DateOnly` | `SearchValues`, `GeneratedRegex` | `Base64Url` | `Rune` en `String`, `AnyNewLine` |
| Numéricos | `Half` | `INumber<T>`, `Int128` | `Tensor<T>` | `Decimal32/64/128` |
| Red | HTTP/3 preview | HTTP/3 estable, QUIC | `WebSocketStream`, TLS 1.3 macOS | `DnsResolver`, compresión de solicitud |
| Compresión | Brotli | `ZipFile` con stream | zlib-ng | Zstandard |

---

## 2. System.Text.Json

### 2.1 Ruta recomendada

```csharp
using System.Text.Json;
using System.Text.Json.Serialization;

var json = JsonSerializer.Serialize(new Pedido(1, 99.5m), AppJson.Default.Pedido);
Pedido? p = JsonSerializer.Deserialize(json, AppJson.Default.Pedido);

public record Pedido(int Id, decimal Total);

[JsonSourceGenerationOptions(
    PropertyNamingPolicy = JsonKnownNamingPolicy.CamelCase,
    AllowOutOfOrderMetadataProperties = true)]
[JsonSerializable(typeof(Pedido))]
internal partial class AppJson : JsonSerializerContext { }
```

### 2.2 Línea de tiempo

| Versión | Capacidad |
|---|---|
| .NET 5 | Records, campos, referencias, extensiones de `HttpClient` |
| .NET 6 | Generador, `JsonNode`, `IAsyncEnumerable` |
| .NET 7 | Polimorfismo, contratos, `required` |
| .NET 8 | Interfaces, `snake_case`, `kebab-case`, streaming, modo sin reflexión |
| .NET 9 | `JsonSchemaExporter`, `RespectNullableAnnotations`, `JsonSerializerOptions.Web`, `JsonStringEnumMemberName` |
| .NET 10 | Rechazo de duplicados, `Strict`, `PipeReader` |
| .NET 11 | Uniones, JSON Lines, polimorfismo ampliado |

### 2.3 Modo estricto

```csharp
// .NET 10: rechaza miembros desconocidos, duplicados y nulos no permitidos
var opciones = new JsonSerializerOptions(JsonSerializerOptions.Strict);
```

> [!TIP]
> Las propiedades duplicadas en JSON son una vía conocida de **confusión de parsers**: dos sistemas interpretan el mismo
> documento de forma distinta. Para datos externos, considera `AllowDuplicateProperties = false`.

---

## 3. LINQ

```csharp
var ventas = new[] { ("MX", 10), ("ES", 20), ("MX", 5) };

// .NET 9
var porPais = ventas.AggregateBy(v => v.Item1, 0, (t, v) => t + v.Item2);
foreach (var (indice, venta) in ventas.Index()) Console.WriteLine($"{indice}: {venta}");

// .NET 10
var clientes = new[] { (Id: 1, Nombre: "Ada") };
var pedidos = new[] { (ClienteId: 1, Total: 9m) };
var unidos = clientes.LeftJoin(pedidos, c => c.Id, p => p.ClienteId,
    (c, p) => $"{c.Nombre}: {p.Total}");
```

| Método | Versión | Evita |
|---|:---:|---|
| `Chunk` | 6 | Lotes manuales |
| `MaxBy`, `MinBy`, `DistinctBy` | 6 | `OrderBy().First()` |
| `Order`, `OrderDescending` | 7 | `OrderBy(x => x)` |
| `CountBy`, `AggregateBy`, `Index` | 9 | `GroupBy` intermedio y `Select((x, i) => ...)` |
| `LeftJoin`, `RightJoin` | 10 | `GroupJoin` + `SelectMany` + `DefaultIfEmpty` |
| `AsyncEnumerable` | 10 | Paquete `System.Linq.Async` |
| `FullJoin` | 11 | Dos uniones concatenadas |

> [!WARNING]
> Si un proyecto usa `System.Linq.Async`, en .NET 10 pueden aparecer ambigüedades porque ya existe en la BCL.

---

## 4. Colecciones

| Necesidad | Tipo | Versión |
|---|---|:---:|
| Configuración leída millones de veces | `FrozenDictionary`, `FrozenSet` | 8 |
| Cola con prioridad | `PriorityQueue<T,P>` | 6 |
| Conservar orden de inserción | `OrderedDictionary<K,V>` | 9 |
| Vista de solo lectura de conjunto | `ReadOnlySet<T>` | 9 |
| Búsqueda sin crear `string` | `GetAlternateLookup<ReadOnlySpan<char>>()` | 9 |
| Comparador por clave | `EqualityComparer<T>.Create` | 11 |

```csharp
var conteos = new Dictionary<string, int>(StringComparer.OrdinalIgnoreCase);
var vista = conteos.GetAlternateLookup<ReadOnlySpan<char>>();

foreach (var rango in "uno dos uno".AsSpan().Split(' '))
{
    // Sin asignar cadenas por cada palabra
}
```

---

## 5. Cadenas y texto

| API | Versión | Uso |
|---|:---:|---|
| `string.Create` con interpolación | 6 | Sin búferes intermedios |
| `SearchValues<char>`, `SearchValues<string>` | 8, 9 | Búsqueda vectorizada |
| `CompositeFormat` | 8 | Plantillas repetidas |
| `IUtf8SpanFormattable` | 8 | Escritura directa a UTF-8 |
| `Regex.EnumerateSplits` | 9 | `Split` sin asignar |
| `Base64Url` | 9 | Tokens |
| `CompareOptions.NumericOrdering` | 10 | Orden natural |
| `Convert.ToHexString` con UTF-8 | 10 | Hex sin conversión |
| `Rune` en `String` | 11 | Unicode correcto |
| `RegexOptions.AnyNewLine` | 11 | Finales de línea mixtos |

---

## 6. Numéricos

```csharp
using System.Numerics;

Decimal64 a = Decimal64.Parse("0.1");
Decimal64 b = Decimal64.Parse("0.2");
Console.WriteLine(a + b);       // 0.3
Console.WriteLine(0.1 + 0.2);   // 0.30000000000000004
```

| Tipo | Bits | Base | Cuándo |
|---|---:|:---:|---|
| `float`, `double` | 32, 64 | 2 | Ciencia, gráficos |
| `Half` | 16 | 2 | IA y almacenamiento; hardware en .NET 11 |
| `decimal` | 128 | 10 | Dinero; formato propio de .NET |
| `Decimal32`, `Decimal64`, `Decimal128` 🆕 | 32–128 | 10 | Interoperabilidad con **IEEE 754** |
| `Int128`, `UInt128` | 128 | Entero | Identificadores, criptografía |
| `BigInteger` | Variable | Entero | Aritmética exacta |
| `Complex<T>` 🆕 | Variable | — | Complejos genéricos |

> [!CAUTION]
> 🆕 .NET 11 cambia los resultados de `Math.Round` con dígitos y de las conversiones de `float`/`double` a `decimal` y
> `BigInteger`: ahora se redondean correctamente. Si tu sistema depende de un resultado exacto anterior, **no migres
> sin pruebas de regresión numérica**.

---

## 7. Tiempo, tareas y concurrencia

```csharp
public class Sesion(TimeProvider reloj)
{
    private readonly DateTimeOffset _inicio = reloj.GetUtcNow();
    public bool Expirada => reloj.GetUtcNow() - _inicio > TimeSpan.FromMinutes(30);
}
```

| API | Versión | Reemplaza |
|---|:---:|---|
| `PeriodicTimer` | 6 | `Timer` con `async` |
| `Parallel.ForEachAsync` | 6 | Semáforos manuales |
| `Task.WaitAsync` | 6 | `Task.WhenAny` con `Delay` |
| `TimeProvider` | 8 | `IClock` propio |
| `Task.WhenEach` | 9 | `WhenAny` en ciclo, que es O(n²) |
| `System.Threading.Lock` | 9 | `lock (object)` |
| `Channel.CreateUnboundedPrioritized` | 9 | Colas propias |

---

## 8. Red y HTTP

| Función | Versión |
|---|:---:|
| HTTP/3 en `HttpClient` | 7 |
| `SocketsHttpHandler` en `HttpClientFactory` | 9 |
| `System.Net.ServerSentEvents` | 9 |
| `WebSocketStream` | 10 |
| TLS 1.3 en macOS (cliente) | 10 |
| `DnsResolver` tipado | 11 |
| Compresión del cuerpo de la solicitud | 11 |
| `QuicStream.Priority` | 11 |

> [!WARNING]
> `HttpClient` debe reutilizarse. Usa `IHttpClientFactory` o una instancia estática con
> `PooledConnectionLifetime`. Crear uno por solicitud agota sockets.

```csharp
builder.Services.AddHttpClient<ClienteCatalogo>(c => c.BaseAddress = new("https://api.ejemplo"))
    .AddStandardResilienceHandler();
```

`AddStandardResilienceHandler` (paquete `Microsoft.Extensions.Http.Resilience`) combina reintentos, tiempo de espera,
limitación y *circuit breaker* usando Polly.

---

## 9. Compresión y archivos

| Función | Versión | Nota |
|---|:---:|---|
| Brotli | Core 2.1 | Web |
| API de Tar | 7 | `System.Formats.Tar` |
| zlib-ng | 9 | Reemplazo de zlib |
| API asíncronas de ZIP | 10 | |
| **Zstandard** | 11 | `ZstandardStream`, `ZstandardEncoder` |
| ZIP con contraseña y CRC32 | 11 | CRC32 lanza ante datos corruptos |

Prueba propia en RC3: 10 000 caracteres `a` comprimidos con `ZstandardStream` ocupan **18 bytes**.

---

## 10. Procesos

```csharp
using System.Diagnostics;

// Antes: ~10 líneas con ProcessStartInfo, redirecciones y lectura de streams
var r = Process.RunAndCaptureText("git", ["rev-parse", "HEAD"]);
Console.WriteLine(r.StandardOutput.Trim());
```

| API .NET 11 | Función |
|---|---|
| `Process.Run`, `RunAsync` | Ejecutar y obtener estado de salida |
| `RunAndCaptureText`, `RunAndCaptureTextAsync` | Capturar stdout, stderr y código |
| `Process.Signal(PosixSignal)` | Enviar señales |
| `ProcessStartInfo.StartSuspended` | Iniciar suspendido |
| `Process.TryGetProcessById` | Sin excepciones |

---

## 11. Extensions: DI, opciones, configuración

```csharp
builder.Services.AddOptions<OpcionesCorreo>()
    .BindConfiguration("Correo")
    .ValidateDataAnnotations()
    .ValidateOnStart();
```

| Función | Versión |
|---|:---:|
| `LoggerMessage` generado | 6 |
| `ValidateOnStart` | 6 |
| Keyed services | 8 |
| `IHostedLifecycleService` | 8 |
| `HybridCache` | 9 |
| Validación asíncrona | 11 |
| Reglas declarativas de `Activity` | 11 |

> [!WARNING]
> 🆕 En .NET 11, una cadena vacía en un proveedor de configuración encadenado **sobrescribe** al anterior, y el acceso
> síncrono a opciones validadas de forma asíncrona lanza excepción.

---

## 12. Código propio que ya puedes borrar

| Código típico | Sustituto | Desde |
|---|---|:---:|
| `IDateTimeProvider` | `TimeProvider` | 8 |
| `Clock` falso en pruebas | `FakeTimeProvider` | 8 |
| Métodos de extensión `Batch` | `Chunk` | 6 |
| `ProcessRunner` | `Process.RunAndCaptureText` | 11 |
| `Guid` ordenable casero | `Guid.CreateVersion7()` | 9 |
| Política Polly manual | `AddStandardResilienceHandler` | 8 |
| Wrapper de `IMemoryCache` + Redis | `HybridCache` | 9 |
| Campo `_field` con validación | `field` | 10 |
| `LeftOuterJoin` | `LeftJoin` | 10 |
| Base64Url manual | `Base64Url` | 9 |
| Serialización `snake_case` manual | `JsonNamingPolicy.SnakeCaseLower` | 8 |

---

## 13. Referencias

- [What's new in .NET 11 libraries](https://learn.microsoft.com/dotnet/core/whats-new/dotnet-11/libraries)
- [What's new in .NET 10 libraries](https://learn.microsoft.com/dotnet/core/whats-new/dotnet-10/libraries)
- [What's new in .NET 9 libraries](https://learn.microsoft.com/dotnet/core/whats-new/dotnet-9/libraries)
- [System.Text.Json overview](https://learn.microsoft.com/dotnet/standard/serialization/system-text-json/overview)
- [Build resilient HTTP apps](https://learn.microsoft.com/dotnet/core/resilience/http-resilience)

---

<div align="center">

[⬅ 12 · AOT y despliegue](12-aot-despliegue-y-contenedores.md) · [🏠 Índice](../README.md) · [14 · ASP.NET Core ➡](14-aspnet-core-y-blazor.md)

</div>
