<div align="center">

# 08 · .NET 10: la madurez

**11 de noviembre de 2025 · LTS · C# 14 · F# 10 · El costo de la abstracción baja, poscuántica y aplicaciones de un archivo**

[⬅ 07 · .NET 9](07-net-9-la-adaptacion.md) · [🏠 Índice](../README.md) · [09 · .NET 11 ➡](09-net-11-la-reescritura-silenciosa.md)

</div>

> [!TIP]
> 🟢 **.NET 10 es la versión recomendada para producción hoy.** Soporte hasta el **14 de noviembre de 2028**.
> Parche vigente: **10.0.14** · SDK **10.0.403**.

---

## Contenido

1. [Ficha técnica](#1-ficha-técnica)
2. [La tesis: abstraer ya casi no cuesta](#2-la-tesis-abstraer-ya-casi-no-cuesta)
3. [JIT en detalle](#3-jit-en-detalle)
4. [C# 14](#4-c-14)
5. [Bibliotecas](#5-bibliotecas)
6. [Criptografía poscuántica](#6-criptografía-poscuántica)
7. [SDK: .NET como lenguaje de scripts](#7-sdk-net-como-lenguaje-de-scripts)
8. [ASP.NET Core 10](#8-aspnet-core-10)
9. [EF Core 10](#9-ef-core-10)
10. [.NET MAUI, WPF y Windows Forms](#10-net-maui-wpf-y-windows-forms)
11. [Contenedores](#11-contenedores)
12. [Lo que suele romperse](#12-lo-que-suele-romperse)
13. [Referencias](#13-referencias)

---

## 1. Ficha técnica

| Dato | Valor |
|---|---|
| Publicación | 11 de noviembre de 2025 |
| Tipo | LTS |
| Fin de soporte | 14 de noviembre de 2028 |
| Último parche | 10.0.14 (25-oct-2026) |
| Último SDK | 10.0.403 |
| Parches publicados | 14, de los cuales 11 con seguridad |
| CVE corregidos | 97 |
| Lenguajes | C# 14 · F# 10 · Visual Basic 17.13 |
| Visual Studio | 2026 (18.0) |
| Compañeros | Aspire 13 |

---

## 2. La tesis: abstraer ya casi no cuesta

.NET 10 declara como foco **reducir la sobrecarga de abstracción**. Un `foreach` sobre `IEnumerable<int>` que en
realidad es un array ha sido históricamente mucho más caro que un `for`, porque el enumerador vive en el heap y
cada llamada es virtual. El objetivo: que el JIT lo vea a través de la interfaz.

```mermaid
flowchart LR
    A["foreach sobre IEnumerable"] --> B["Devirtualiza<br/>métodos de interfaz de array"]
    B --> C["Inlining de<br/>MoveNext y Current"]
    C --> D["Análisis de escape:<br/>el enumerador no escapa"]
    D --> E["Asignación en pila"]
    E --> F["Promoción a registros"]
    F --> G["Se parece a un for"]
    classDef a fill:#3987e5,color:#fff,stroke:#1d4f8f
    classDef b fill:#d95926,color:#fff,stroke:#7f3312
    classDef c fill:#199e70,color:#04121a,stroke:#0b5a3f
    class A a
    class B,C,D,E,F b
    class G c
```

Es un cambio arquitectónico: la distancia entre el código "limpio" y el código "rápido" se reduce. El
[laboratorio](24-laboratorio.md) mide exactamente este caso.

---

## 3. JIT en detalle

| Optimización | Mecanismo | Beneficio |
|---|---|---|
| **Argumentos struct** | Coloca miembros promovidos en registros compartidos | Sin paso por memoria al pasar structs pequeños |
| **Inversión de ciclos** | Reconocimiento por grafo en vez de análisis léxico | Habilita clonado, desenrollado y variables de inducción |
| **Devirtualización de arrays** | Métodos de interfaz de array | Primer paso hacia paridad total |
| **Layout de código** | Reordenar bloques como **TSP asimétrico con heurística 3-opt** | Más densidad en el camino caliente |
| **Inlining** | Métodos con `try-finally`, tipos de retorno precisos, perfil heredado | Más oportunidades en cadena |
| **Pila** | Arrays pequeños de valor y de referencia; análisis de escape de campos struct y delegados | Menos presión de GC |
| **AVX10.2** | Intrínsecos incluidos; deshabilitados por defecto por falta de hardware al salir | Preparación |
| **Barrera de escritura Arm64** | Cambio dinámico como en x64, más preciso con regiones | Pausas de GC de **8 % a más de 20 %** menores en pruebas de Microsoft |

```csharp
static int Sum()
{
    int[] numeros = { 1, 2, 3 };   // .NET 10 puede ubicarlo en la pila
    int suma = 0;
    foreach (var n in numeros) suma += n;
    return suma;
}
```

Ejemplo oficial del paso de `struct` en registros compartidos, cuando `Point` tiene dos `int` en x64:

```asm
Program:Main() (FullOpts):
       mov      rdi, 0x140000000A
       tail.jmp [Program:Consume(Program+Point)]
```

El valor `0x14_0000000A` es `20` y `10` empaquetados en un solo registro: ya no hay acceso a memoria.

---

## 4. C# 14

```csharp
public static class Extensiones
{
    // Bloque extension: propiedades y miembros estáticos, no solo métodos
    extension<T>(IEnumerable<T> fuente)
    {
        public bool EstaVacia => !fuente.Any();
        public IEnumerable<T> Muestra(int n) => fuente.Take(n);
    }

    extension<T>(IEnumerable<T>)
    {
        public static IEnumerable<T> Nada => [];
    }
}

public class Usuario
{
    // field: lógica en un accesor sin campo manual
    public string Nombre
    {
        get;
        set => field = value?.Trim() ?? throw new ArgumentNullException(nameof(value));
    } = "";
}
```

```csharp
// Asignación condicional nula
cliente?.Direccion = nuevaDireccion;

// nameof sobre genérico sin enlazar
Console.WriteLine(nameof(List<>));

// Modificadores en lambdas sin escribir tipos
delegate bool Analizar(string texto, out int valor);
Analizar f = (texto, out valor) => int.TryParse(texto, out valor);
```

| Función | Impacto |
|---|---|
| Miembros de extensión | Mayor cambio del lenguaje en años |
| `field` | Termina con el campo manual de una línea |
| Conversiones implícitas de `Span` | `T[]` a `Span<T>` y `ReadOnlySpan<T>` |
| `?.=` | Menos `if` nulos |
| Operadores compuestos definidos | `+=` sin crear un nuevo objeto |
| Constructores y eventos `partial` | Para generadores |

> [!WARNING]
> **Dos cambios a vigilar.** Las conversiones de `Span` alteran la resolución de sobrecargas: una llamada a `Contains`
> sobre un array puede resolver ahora a `MemoryExtensions`. Y `field` es palabra clave contextual: si tienes un
> miembro llamado `field` dentro de un accesor, usa `@field` o `this.field`.

---

## 5. Bibliotecas

| Área | Novedades |
|---|---|
| JSON | `AllowDuplicateProperties=false`, `JsonSerializerOptions.Strict`, soporte de `PipeReader`, `ReferenceHandler` en opciones de generación |
| LINQ | `LeftJoin`, `RightJoin`; `AsyncEnumerable` en la BCL |
| Colecciones | Sobrecargas `TryAdd` y `TryGetValue` con índice en `OrderedDictionary` |
| Cadenas | Normalización sobre `Span`, hex en UTF-8, comparación numérica con `CompareOptions.NumericOrdering` |
| Red | `WebSocketStream`, TLS 1.3 en macOS (cliente) |
| Compresión | Mejoras de memoria y rendimiento en `ZipArchive`, API asíncronas de ZIP |
| Procesos | Grupos de procesos en Windows |
| Diagnóstico | URL de esquema en `ActivitySource` y `Meter`, muestreo limitado de trazas |
| Tensores | API **estable**, en el paquete `System.Numerics.Tensors` |

```csharp
using System.Globalization;

var opciones = new JsonSerializerOptions(JsonSerializerOptions.Strict);

StringComparer comparador = StringComparer.Create(CultureInfo.InvariantCulture, CompareOptions.NumericOrdering);
string[] nombres = ["archivo10", "archivo2"];
Array.Sort(nombres, comparador);   // archivo2, archivo10
```

---

## 6. Criptografía poscuántica

.NET 10 incorpora tres algoritmos asimétricos estandarizados por NIST:

| Algoritmo | Estándar | Tipo | Clase | Estado |
|---|---|---|---|---|
| ML-KEM | FIPS 203 | Encapsulamiento de claves | `MLKem` | 🟢 Estable |
| ML-DSA | FIPS 204 | Firma | `MLDsa` | 🟢 Estable |
| SLH-DSA | FIPS 205 | Firma sin estado basada en hash | `SlhDsa` | 🧪 `SYSLIB5006` |
| Composite ML-DSA | Borrador IETF | Híbrido clásico + PQC | `CompositeMLDsa` | 🧪 `SYSLIB5006` |

Comprobado al compilar: usar `SlhDsa` o `CompositeMLDsa` produce el error `SYSLIB5006` hasta que lo suprimes de forma
explícita, tanto en `net10.0` como en `net11.0`.

```csharp
using System.Security.Cryptography;

if (MLKem.IsSupported)
{
    using MLKem clave = MLKem.GenerateKey(MLKemAlgorithm.MLKem768);
    clave.Encapsulate(out byte[] cifrado, out byte[] secreto);
}
```

Requiere **OpenSSL 3.5 o superior** o **Windows CNG con soporte PQC**. Comprueba siempre `IsSupported`. Más en el
[capítulo 20](20-seguridad-y-cadena-de-suministro.md).

---

## 7. SDK: .NET como lenguaje de scripts

```csharp
#!/usr/bin/env dotnet
#:package Humanizer@2.14.1
#:property PublishAot=false

using Humanizer;

Console.WriteLine(TimeSpan.FromDays(3).Humanize());
```

```bash
chmod +x hola.cs
./hola.cs
dotnet run hola.cs
dotnet publish hola.cs         # Native AOT por defecto en file-based apps
```

| Función | Comando |
|---|---|
| Aplicaciones de un archivo | `dotnet run app.cs` |
| Directivas | `#:package`, `#:sdk`, `#:project`, `#:property` |
| Ejecución única de herramientas | `dotnet tool exec`, `dnx` |
| Herramientas por plataforma | RID específico o `any` |
| Introspección | `--cli-schema` |
| Formato de solución | `.slnx` por defecto en `dotnet new sln` |
| Pruebas | `dotnet test` con Microsoft.Testing.Platform |
| Autocompletado | Scripts nativos para shells |
| Contenedores | Apps de consola sin configuración extra |
| Paquetes | Poda de referencias que ya aporta el framework |

---

## 8. ASP.NET Core 10

| Función | Detalle |
|---|---|
| **Passkeys** | Soporte en Identity con WebAuthn |
| **Validación en Minimal APIs** | `AddValidation()`, con generación de código |
| **Server-Sent Events** | `TypedResults.ServerSentEvents` |
| **OpenAPI 3.1** | Versión predeterminada |
| Blazor | Precarga de activos WebAssembly, estado persistente declarativo, persistencia de circuitos |
| Memoria | Expulsión automática de los *pools* de memoria en Kestrel |
| Diagnóstico | Métricas nuevas de Identity, Blazor y autenticación |

---

## 9. EF Core 10

```csharp
// Filtros con nombre: se desactivan por separado
modelBuilder.Entity<Pedido>()
    .HasQueryFilter("BorradoLogico", p => !p.Borrado)
    .HasQueryFilter("Tenant", p => p.TenantId == tenantId);

var todos = await db.Pedidos.IgnoreQueryFilters(["BorradoLogico"]).ToListAsync();

// LeftJoin ya es un operador
var informe = db.Clientes.LeftJoin(
    db.Pedidos,
    c => c.Id,
    p => p.ClienteId,
    (c, p) => new { c.Nombre, Total = (decimal?)p!.Total });
```

| Función | Proveedor |
|---|---|
| Tipo `vector` y `VectorDistance` | SQL Server y Azure SQL |
| Tipo `json` nativo | SQL Server y Azure SQL |
| Búsqueda de texto, híbrida y vectorial | Cosmos DB |
| Tipos complejos: división de tablas, JSON, structs | Relacional |
| `ExecuteUpdate` sobre JSON | Relacional |
| Constantes redactadas en logs | Seguridad |

---

## 10. .NET MAUI, WPF y Windows Forms

**.NET MAUI 10**: generador de XAML, integración con Aspire, enlaces para Android 16 e iOS 26, mejoras en `MediaPicker`
e interceptación de solicitudes en `WebView`.

**WPF**: mejoras de rendimiento y estilos Fluent.

**Windows Forms**: cambios en el portapapeles y `UITypeEditors` portados desde .NET Framework.

---

## 11. Contenedores

| Cambio | Detalle |
|---|---|
| **Imagen por defecto** | **Ubuntu 24.04 (noble)** en lugar de Debian: etiqueta `10.0` |
| Consola | `dotnet publish` crea imágenes sin configuración extra |
| Formato | `ContainerImageFormat` para Docker u OCI |

---

## 12. Lo que suele romperse

| Cambio | Tipo | Qué hacer |
|---|---|---|
| Resolución de sobrecargas con `Span` | Comportamiento | Recompilar y probar |
| `BackgroundService` ejecuta todo `ExecuteAsync` como `Task` | Comportamiento | Revisar código previo al primer `await` |
| Valores `null` conservados en configuración | Comportamiento | Revisar defaults |
| `dotnet restore` audita transitivos | Comportamiento | Espera nuevas advertencias, y errores si usas *warnings as errors* |
| `dotnet new sln` genera `.slnx` | Comportamiento | Verifica tus scripts de CI |
| OpenSSL 1.1.1 mínimo | Comportamiento | Revisar Linux antiguos |
| `System.Linq.AsyncEnumerable` en core | Fuente | Puede chocar con `System.Linq.Async` |
| El runtime ya no instala manejadores predeterminados de señales de terminación | Comportamiento | Revisar apagado |
| HTTP/3 deshabilitado con `PublishTrimmed` | Fuente | Actívalo explícitamente si lo usas |

Lista ampliada en el [capítulo 21](21-migracion-y-cambios-disruptivos.md).

---

## 13. Referencias

- [What's new in .NET 10](https://learn.microsoft.com/dotnet/core/whats-new/dotnet-10/overview)
- [What's new in the .NET 10 runtime](https://learn.microsoft.com/dotnet/core/whats-new/dotnet-10/runtime)
- [What's new in .NET 10 libraries](https://learn.microsoft.com/dotnet/core/whats-new/dotnet-10/libraries)
- [What's new in the SDK for .NET 10](https://learn.microsoft.com/dotnet/core/whats-new/dotnet-10/sdk)
- [What's new in C# 14](https://learn.microsoft.com/dotnet/csharp/whats-new/csharp-14)
- [Breaking changes in .NET 10](https://learn.microsoft.com/dotnet/core/compatibility/10)
- [What's new in EF Core 10](https://learn.microsoft.com/ef/core/what-is-new/ef-core-10.0/whatsnew)
- [Announcing .NET 10](https://devblogs.microsoft.com/dotnet/announcing-dotnet-10/)
- [Ejemplo ejecutable](../ejemplos/net10-madurez.cs)

---

<div align="center">

[⬅ 07 · .NET 9](07-net-9-la-adaptacion.md) · [🏠 Índice](../README.md) · [09 · .NET 11 ➡](09-net-11-la-reescritura-silenciosa.md)

</div>
