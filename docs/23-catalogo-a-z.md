<div align="center">

# 23 · Catálogo A–Z

**180 capacidades de la plataforma, de .NET 5 a .NET 11, con su versión de origen y estado**

[⬅ 22 · Guías de decisión](22-guias-de-decision.md) · [🏠 Índice](../README.md) · [24 · Laboratorio ➡](24-laboratorio.md)

</div>

> [!NOTE]
> Este capítulo se **genera** desde `data/caracteristicas.csv` con `python3 tools/generar_atlas.py`. No lo edites a mano.
> Estado verificado al **4 de noviembre de 2026**. La columna *Desde* indica la primera versión de .NET con la capacidad, no la última que la mejoró.

---

## Resumen

| .NET | Tema | Capacidades catalogadas |
|---|---|---:|
| **5** | La unificación | 13 |
| **6** | La consolidación | 20 |
| **7** | La velocidad | 20 |
| **8** | La nube nativa | 23 |
| **9** | La adaptación | 26 |
| **10** | La madurez | 34 |
| **11** | La reescritura silenciosa | 44 |

| Área | Capacidades |
|---|---:|
| Lenguaje | 37 |
| Bibliotecas base | 32 |
| Runtime | 25 |
| Web | 19 |
| SDK | 13 |
| Datos | 13 |
| AOT y despliegue | 11 |
| Seguridad | 9 |
| IA | 8 |
| Clientes | 7 |
| Nube | 6 |

**Saltar a:** [A](#a) · [B](#b) · [C](#c) · [D](#d) · [E](#e) · [F](#f) · [G](#g) · [H](#h) · [I](#i) · [J](#j) · [K](#k) · [L](#l) · [M](#m) · [N](#n) · [O](#o) · [P](#p) · [R](#r) · [S](#s) · [T](#t) · [U](#u) · [V](#v) · [W](#w) · [X](#x) · [Z](#z)

---

## A

| Capacidad | Área | Desde | Estado | Descripción |
|---|---|:---:|---|---|
| [Alias de cualquier tipo](10-lenguajes-csharp-fsharp-vb.md) | Lenguaje | .NET 8 | 🟢 GA | using para tuplas, punteros y arrays (C# 12) |
| [allows ref struct](10-lenguajes-csharp-fsharp-vb.md) | Lenguaje | .NET 9 | 🟢 GA | Genéricos sobre ref struct (C# 13) |
| [Anotaciones de nulabilidad en BCL](13-bibliotecas-base.md) | Bibliotecas base | .NET 5 | 🟢 GA | 80 % de las bibliotecas anotadas para tipos de referencia anulables |
| [Antigüedad mínima de paquete](20-seguridad-y-cadena-de-suministro.md) | Seguridad | .NET 11 | 🟡 RC | --min-publish-age-hours en orígenes NuGet |
| [API de métricas](17-cloud-native-aspire-y-observabilidad.md) | Nube | .NET 6 | 🟢 GA | API de métricas alineada con OpenTelemetry |
| [App trimming](12-aot-despliegue-y-contenedores.md) | AOT y despliegue | .NET 5 | 🟢 GA | Recorte de ensamblados no usados en publicación autocontenida |
| [Apple Silicon](11-runtime-jit-y-gc.md) | Runtime | .NET 6 | 🟢 GA | Soporte nativo de macOS Arm64 y emulación x64 lado a lado |
| [Argumentos en colecciones](10-lenguajes-csharp-fsharp-vb.md) | Lenguaje | .NET 11 | 🟡 RC | with(...) dentro de una expresión de colección (C# 15) |
| [Arm64 SVE](11-runtime-jit-y-gc.md) | Runtime | .NET 9 | 🟢 GA | Soporte inicial de Scalable Vector Extension |
| [Aspire 13](17-cloud-native-aspire-y-observabilidad.md) | Nube | .NET 10 | 🟢 GA | Orquestación políglota y AppHost de un solo archivo |
| [Aspire 9](17-cloud-native-aspire-y-observabilidad.md) | Nube | .NET 9 | 🟢 GA | Panel independiente y control de ciclo de vida de recursos |
| [AsyncEnumerable en BCL](13-bibliotecas-base.md) | Bibliotecas base | .NET 10 | 🟢 GA | LINQ asíncrono como parte de las bibliotecas base |
| [AVX-512 y Vector512](11-runtime-jit-y-gc.md) | Runtime | .NET 8 | 🟢 GA | Vector512<T> e intrínsecos AVX-512 |
| [AVX10.2](11-runtime-jit-y-gc.md) | Runtime | .NET 10 | 🟡 Preview | Intrínsecos incluidos; deshabilitados por defecto al salir .NET 10 |
| [Azure Linux 4.0](12-aot-despliegue-y-contenedores.md) | AOT y despliegue | .NET 11 | 🟡 RC | Etiquetas de imagen para Azure Linux 4.0 |

## B

| Capacidad | Área | Desde | Estado | Descripción |
|---|---|:---:|---|---|
| [Blazor AI components](18-ia-en-net.md) | IA | .NET 11 | 🧪 Experimental | Componentes para interfaces agénticas |
| [Blazor CSS isolation](14-aspnet-core-y-blazor.md) | Web | .NET 5 | 🟢 GA | CSS con ámbito de componente y lazy loading en WebAssembly |
| [Blazor render mode info](14-aspnet-core-y-blazor.md) | Web | .NET 9 | 🟢 GA | RendererInfo y AssignedRenderMode en componentes |
| [Blazor Web App](14-aspnet-core-y-blazor.md) | Web | .NET 8 | 🟢 GA | SSR, modos de renderizado por componente y streaming rendering |
| [Búsqueda vectorial EF Core](15-datos-y-ef-core.md) | Datos | .NET 10 | 🟢 GA | VECTOR y JSON nativos en SQL Server |

## C

| Capacidad | Área | Desde | Estado | Descripción |
|---|---|:---:|---|---|
| [CET](20-seguridad-y-cadena-de-suministro.md) | Seguridad | .NET 9 | 🟢 GA | Control-flow Enforcement Technology por defecto en Windows |
| [CLI con NativeAOT](19-sdk-herramientas-y-pruebas.md) | SDK | .NET 11 | 🟡 RC | Comandos comunes de dotnet sin arranque administrado |
| [Closed hierarchies](10-lenguajes-csharp-fsharp-vb.md) | Lenguaje | .NET 11 | 🟡 RC | Modificador closed para jerarquías exhaustivas (C# 15) |
| [Collection expressions](10-lenguajes-csharp-fsharp-vb.md) | Lenguaje | .NET 8 | 🟢 GA | Sintaxis unificada [1, 2, .. resto] (C# 12) |
| [Complex types EF Core](15-datos-y-ef-core.md) | Datos | .NET 8 | 🟢 GA | Objetos de valor y colecciones primitivas |
| [Complex types en TPT/TPC](15-datos-y-ef-core.md) | Datos | .NET 11 | 🟡 RC | Tipos complejos y JSON con herencia ampliada |
| [Compound assignment definido](10-lenguajes-csharp-fsharp-vb.md) | Lenguaje | .NET 10 | 🟢 GA | Operadores += y ++ definidos por el usuario (C# 14) |
| [Compresión Zstandard HTTP](14-aspnet-core-y-blazor.md) | Web | .NET 11 | 🟡 RC | Respuesta y solicitud con zstd |
| [Consultas híbridas EF Core](15-datos-y-ef-core.md) | Datos | .NET 11 | 🟡 RC | VECTOR_SEARCH, índices vectoriales y búsqueda híbrida |
| [Consultas precompiladas EF Core](15-datos-y-ef-core.md) | Datos | .NET 9 | 🧪 Experimental | Soporte de AOT y consultas precompiladas |
| [Contract customization JSON](13-bibliotecas-base.md) | Bibliotecas base | .NET 7 | 🟢 GA | Contratos personalizables y polimorfismo en System.Text.Json |
| [Conversiones implícitas de Span](10-lenguajes-csharp-fsharp-vb.md) | Lenguaje | .NET 10 | 🟢 GA | Span y ReadOnlySpan como conversión de primera clase (C# 14) |
| [CoreCLR en móvil](16-clientes-maui-wpf-winforms.md) | Runtime | .NET 11 | 🟡 RC | CoreCLR reemplaza a Mono como runtime predeterminado de MAUI |
| [CoreCLR en WebAssembly](11-runtime-jit-y-gc.md) | Runtime | .NET 11 | 🟡 Preview | Avanza la ejecución de CoreCLR en WASM |
| [Cosmos DB provider renovado](15-datos-y-ef-core.md) | Datos | .NET 9 | 🟢 GA | Reescritura importante del proveedor Cosmos DB |
| [Cosmos DB transaccional](15-datos-y-ef-core.md) | Datos | .NET 11 | 🟡 RC | Batch transaccional y ejecución masiva |
| [CountBy y AggregateBy](13-bibliotecas-base.md) | Bibliotecas base | .NET 9 | 🟢 GA | Nuevas agregaciones LINQ sin GroupBy intermedio |
| [Criptografía poscuántica](20-seguridad-y-cadena-de-suministro.md) | Seguridad | .NET 10 | 🟢 GA | ML-KEM y ML-DSA estables; SLH-DSA y Composite ML-DSA experimentales |
| [Crossgen2](12-aot-despliegue-y-contenedores.md) | AOT y despliegue | .NET 6 | 🟢 GA | Compilador ReadyToRun escrito en C# |

## D

| Capacidad | Área | Desde | Estado | Descripción |
|---|---|:---:|---|---|
| [DATAS](11-runtime-jit-y-gc.md) | Runtime | .NET 8 | 🟡 Preview | Adaptación dinámica a tamaño de aplicación; por defecto en Server GC desde .NET 9 |
| [DATAS por defecto](11-runtime-jit-y-gc.md) | Runtime | .NET 9 | 🟢 GA | Server GC adapta el heap al tamaño de datos activos |
| [DateOnly y TimeOnly](13-bibliotecas-base.md) | Bibliotecas base | .NET 6 | 🟢 GA | Fecha y hora como tipos separados |
| [De-abstraction en JIT](11-runtime-jit-y-gc.md) | Runtime | .NET 10 | 🟢 GA | Devirtualización de arrays y asignación en pila de enumeradores |
| [Decimal32/64/128](13-bibliotecas-base.md) | Bibliotecas base | .NET 11 | 🟡 RC | Decimales de coma flotante IEEE 754 |
| [Device Bound Sessions](20-seguridad-y-cadena-de-suministro.md) | Seguridad | .NET 11 | 🧪 Experimental | Sesiones vinculadas al dispositivo |
| [dotnet test móvil](19-sdk-herramientas-y-pruebas.md) | SDK | .NET 11 | 🟡 RC | Pruebas en Android, iOS, macOS y Mac Catalyst |
| [dotnet tool exec y dnx](19-sdk-herramientas-y-pruebas.md) | SDK | .NET 10 | 🟢 GA | Ejecución puntual de herramientas |
| [dotnetup](19-sdk-herramientas-y-pruebas.md) | SDK | .NET 11 | 🟡 Preview | Gestor de SDK y runtimes en el directorio del usuario |
| [Dynamic PGO (opt-in)](11-runtime-jit-y-gc.md) | Runtime | .NET 6 | 🟢 GA | Optimización guiada por perfil durante la ejecución; habilitada por configuración |
| [Dynamic PGO por defecto](11-runtime-jit-y-gc.md) | Runtime | .NET 8 | 🟢 GA | PGO dinámico habilitado de forma predeterminada |

## E

| Capacidad | Área | Desde | Estado | Descripción |
|---|---|:---:|---|---|
| [EF Core 5 muchos a muchos](15-datos-y-ef-core.md) | Datos | .NET 5 | 🟢 GA | Muchos a muchos sin entidad intermedia, TPT y split queries |
| [Endpoint filters](14-aspnet-core-y-blazor.md) | Web | .NET 7 | 🟢 GA | Filtros y route groups en Minimal APIs |
| [Escape analysis](11-runtime-jit-y-gc.md) | Runtime | .NET 10 | 🟢 GA | Asignación en pila de arrays pequeños y delegados |
| [Excepciones administradas](11-runtime-jit-y-gc.md) | Runtime | .NET 9 | 🟢 GA | Nuevo manejo de excepciones derivado de NativeAOT |
| [ExecuteUpdate y ExecuteDelete](15-datos-y-ef-core.md) | Datos | .NET 7 | 🟢 GA | Operaciones masivas sin cargar entidades |
| [Extension indexers](10-lenguajes-csharp-fsharp-vb.md) | Lenguaje | .NET 11 | 🟡 RC | Indexadores en bloques extension (C# 15) |
| [Extension members](10-lenguajes-csharp-fsharp-vb.md) | Lenguaje | .NET 10 | 🟢 GA | Bloques extension con propiedades y miembros estáticos (C# 14) |

## F

| Capacidad | Área | Desde | Estado | Descripción |
|---|---|:---:|---|---|
| [field keyword](10-lenguajes-csharp-fsharp-vb.md) | Lenguaje | .NET 10 | 🟢 GA | Acceso al campo respaldado por el compilador (C# 14) |
| [File-based apps](19-sdk-herramientas-y-pruebas.md) | SDK | .NET 10 | 🟢 GA | dotnet run app.cs sin archivo de proyecto |
| [File-scoped namespaces](10-lenguajes-csharp-fsharp-vb.md) | Lenguaje | .NET 6 | 🟢 GA | namespace X; sin llaves ni sangría adicional (C# 10) |
| [FileStream reescrito](13-bibliotecas-base.md) | Bibliotecas base | .NET 6 | 🟢 GA | Nueva implementación que nunca bloquea con E/S asíncrona en Windows |
| [FP16 en hardware](11-runtime-jit-y-gc.md) | Runtime | .NET 11 | 🟡 RC | Half usa instrucciones nativas donde existen |
| [Frozen collections](13-bibliotecas-base.md) | Bibliotecas base | .NET 8 | 🟢 GA | FrozenDictionary y FrozenSet para lectura intensiva |
| [FullJoin en LINQ](13-bibliotecas-base.md) | Bibliotecas base | .NET 11 | 🟡 RC | FullJoin y sobrecargas de Join que devuelven tuplas |
| [Function pointers](10-lenguajes-csharp-fsharp-vb.md) | Lenguaje | .NET 5 | 🟢 GA | delegate* expone ldftn y calli para interop de alto rendimiento (C# 9) |

## G

| Capacidad | Área | Desde | Estado | Descripción |
|---|---|:---:|---|---|
| [GC Regions](11-runtime-jit-y-gc.md) | Runtime | .NET 7 | 🟢 GA | Regiones en lugar de segmentos en el GC de 64 bits |
| [GC.RefreshMemoryLimit](11-runtime-jit-y-gc.md) | Runtime | .NET 8 | 🟢 GA | Ajuste del límite de memoria en ejecución |
| [Generador de XAML](16-clientes-maui-wpf-winforms.md) | Clientes | .NET 10 | 🟢 GA | Generación de código para XAML en .NET MAUI |
| [Generic math](10-lenguajes-csharp-fsharp-vb.md) | Lenguaje | .NET 7 | 🟢 GA | Miembros static abstract e interfaces INumber<T> (C# 11) |
| [global using](10-lenguajes-csharp-fsharp-vb.md) | Lenguaje | .NET 6 | 🟢 GA | Directivas using compartidas por todo el proyecto (C# 10) |

## H

| Capacidad | Área | Desde | Estado | Descripción |
|---|---|:---:|---|---|
| [Hot Reload](19-sdk-herramientas-y-pruebas.md) | SDK | .NET 6 | 🟢 GA | Aplicar cambios a una app en ejecución con dotnet watch o Visual Studio |
| [HTTP/3 en Kestrel](14-aspnet-core-y-blazor.md) | Web | .NET 7 | 🟢 GA | HTTP/3 y QUIC soportados en servidor |
| [HybridCache](14-aspnet-core-y-blazor.md) | Web | .NET 9 | 🟢 GA | Caché L1 y L2 con protección contra estampidas |

## I

| Capacidad | Área | Desde | Estado | Descripción |
|---|---|:---:|---|---|
| [Identity API endpoints](14-aspnet-core-y-blazor.md) | Web | .NET 8 | 🟢 GA | MapIdentityApi para aplicaciones SPA y móviles |
| [IExceptionHandler](14-aspnet-core-y-blazor.md) | Web | .NET 8 | 🟢 GA | Manejo centralizado de excepciones |
| [Imágenes chiseled](12-aot-despliegue-y-contenedores.md) | AOT y despliegue | .NET 8 | 🟢 GA | Imágenes Ubuntu distroless sin shell ni gestor de paquetes |
| [Imágenes reproducibles](12-aot-despliegue-y-contenedores.md) | AOT y despliegue | .NET 11 | 🟡 RC | SOURCE_DATE_EPOCH en publicación de contenedores |
| [Imágenes Ubuntu por defecto](12-aot-despliegue-y-contenedores.md) | AOT y despliegue | .NET 10 | 🟢 GA | Las imágenes .NET 10 usan Ubuntu 24.04 por defecto |
| [Init-only setters](10-lenguajes-csharp-fsharp-vb.md) | Lenguaje | .NET 5 | 🟢 GA | Propiedades asignables solo durante la inicialización (C# 9) |
| [Inline arrays](10-lenguajes-csharp-fsharp-vb.md) | Lenguaje | .NET 8 | 🟢 GA | Búferes de tamaño fijo seguros en structs (C# 12) |
| [Int128](13-bibliotecas-base.md) | Bibliotecas base | .NET 7 | 🟢 GA | Int128 y UInt128 con generic math |
| [Interceptors](10-lenguajes-csharp-fsharp-vb.md) | Lenguaje | .NET 8 | 🧪 Experimental | Sustitución de llamadas en compilación; experimental en C# 12 |
| [Interpolated string handlers](10-lenguajes-csharp-fsharp-vb.md) | Lenguaje | .NET 6 | 🟢 GA | Interpolación sin asignaciones cuando no hace falta (C# 10) |

## J

| Capacidad | Área | Desde | Estado | Descripción |
|---|---|:---:|---|---|
| [JSON columns EF Core](15-datos-y-ef-core.md) | Datos | .NET 7 | 🟢 GA | Columnas JSON y herencia TPC |
| [JSON Schema exporter](13-bibliotecas-base.md) | Bibliotecas base | .NET 9 | 🟢 GA | JsonSchemaExporter genera esquemas desde tipos |

## K

| Capacidad | Área | Desde | Estado | Descripción |
|---|---|:---:|---|---|
| [Keyed services](13-bibliotecas-base.md) | Bibliotecas base | .NET 8 | 🟢 GA | Inyección de dependencias con clave |

## L

| Capacidad | Área | Desde | Estado | Descripción |
|---|---|:---:|---|---|
| [Labeled break y continue](10-lenguajes-csharp-fsharp-vb.md) | Lenguaje | .NET 11 | 🟡 RC | Saltos con etiqueta en ciclos anidados (C# 15) |
| [Layout con 3-opt](11-runtime-jit-y-gc.md) | Runtime | .NET 10 | 🟢 GA | Ordenamiento de bloques como TSP asimétrico |
| [LeftJoin en EF Core](15-datos-y-ef-core.md) | Datos | .NET 10 | 🟢 GA | Traducción de LeftJoin y RightJoin a SQL |
| [LeftJoin y RightJoin](13-bibliotecas-base.md) | Bibliotecas base | .NET 10 | 🟢 GA | Nuevos operadores LINQ |
| [Línea base x86-64-v2](11-runtime-jit-y-gc.md) | Runtime | .NET 11 | 🟡 RC | Se exige x86-64-v2 y LSE en Windows Arm64 |
| [LINQ Chunk y MaxBy](13-bibliotecas-base.md) | Bibliotecas base | .NET 6 | 🟢 GA | Chunk, MaxBy, MinBy, DistinctBy e índices con Index y Range |
| [List patterns](10-lenguajes-csharp-fsharp-vb.md) | Lenguaje | .NET 7 | 🟢 GA | Patrones sobre listas con [1, .., 9] (C# 11) |
| [LoggerMessage generado](17-cloud-native-aspire-y-observabilidad.md) | Bibliotecas base | .NET 6 | 🟢 GA | Registro de alto rendimiento mediante source generator |

## M

| Capacidad | Área | Desde | Estado | Descripción |
|---|---|:---:|---|---|
| [MapStaticAssets](14-aspnet-core-y-blazor.md) | Web | .NET 9 | 🟢 GA | Activos estáticos con compresión y huellas en compilación |
| [Más de 1024 CPU](11-runtime-jit-y-gc.md) | Runtime | .NET 11 | 🟡 RC | El runtime inicia en servidores con más de 1024 procesadores lógicos |
| [Material 3 en Android](16-clientes-maui-wpf-winforms.md) | Clientes | .NET 11 | 🟡 RC | Controles MAUI con Material 3 |
| [Metrics de ASP.NET Core](17-cloud-native-aspire-y-observabilidad.md) | Nube | .NET 8 | 🟢 GA | Instrumentación integrada e IMeterFactory |
| [Microsoft Agent Framework](18-ia-en-net.md) | IA | .NET 10 | 🟢 GA | Sucesor unificado de Semantic Kernel y AutoGen; 1.0 en abril de 2026 |
| [Microsoft.Extensions.AI](18-ia-en-net.md) | IA | .NET 9 | 🟢 GA | IChatClient y abstracciones comunes de IA |
| [Microsoft.Testing.Platform](19-sdk-herramientas-y-pruebas.md) | SDK | .NET 10 | 🟢 GA | dotnet test con MTP |
| [Minimal APIs](14-aspnet-core-y-blazor.md) | Web | .NET 6 | 🟢 GA | Endpoints HTTP con MapGet y WebApplication |
| [ML-KEM compuesto y HPKE](20-seguridad-y-cadena-de-suministro.md) | Seguridad | .NET 11 | 🧪 Experimental | APIs experimentales SYSLIB5006 |
| [MSBuild server por defecto](19-sdk-herramientas-y-pruebas.md) | SDK | .NET 11 | 🟡 RC | Servidor de MSBuild habilitado por defecto |

## N

| Capacidad | Área | Desde | Estado | Descripción |
|---|---|:---:|---|---|
| [Named query filters](15-datos-y-ef-core.md) | Datos | .NET 10 | 🟢 GA | Múltiples filtros globales por entidad |
| [Native AOT](12-aot-despliegue-y-contenedores.md) | AOT y despliegue | .NET 7 | 🟢 GA | Ejecutable nativo sin JIT; en .NET 7 orientado a consola |
| [Native AOT en ASP.NET Core](12-aot-despliegue-y-contenedores.md) | AOT y despliegue | .NET 8 | 🟢 GA | Minimal APIs y gRPC con publicación nativa |
| [.NET Aspire 8](17-cloud-native-aspire-y-observabilidad.md) | Nube | .NET 8 | 🟢 GA | Orquestación y panel local; GA en mayo de 2024 |
| [.NET MAUI](16-clientes-maui-wpf-winforms.md) | Clientes | .NET 6 | 🟢 GA | UI multiplataforma; GA en mayo de 2022 sobre .NET 6 |
| [NuGet audit transitivo](20-seguridad-y-cadena-de-suministro.md) | Seguridad | .NET 10 | 🟢 GA | dotnet restore audita dependencias transitivas |
| [Null-conditional assignment](10-lenguajes-csharp-fsharp-vb.md) | Lenguaje | .NET 10 | 🟢 GA | a?.B = c (C# 14) |

## O

| Capacidad | Área | Desde | Estado | Descripción |
|---|---|:---:|---|---|
| [On-stack replacement](11-runtime-jit-y-gc.md) | Runtime | .NET 7 | 🟢 GA | Sustitución de código durante la ejecución de un método largo |
| [OpenAPI 3.1](14-aspnet-core-y-blazor.md) | Web | .NET 10 | 🟢 GA | Versión predeterminada de los documentos generados |
| [OpenAPI 3.2](14-aspnet-core-y-blazor.md) | Web | .NET 11 | 🟡 RC | Versión predeterminada y soporte de SSE con itemSchema |
| [OpenAPI integrado](14-aspnet-core-y-blazor.md) | Web | .NET 9 | 🟢 GA | Microsoft.AspNetCore.OpenApi reemplaza a Swashbuckle en las plantillas |
| [OrderedDictionary genérico](13-bibliotecas-base.md) | Bibliotecas base | .NET 9 | 🟢 GA | Diccionario que conserva el orden de inserción |
| [Output caching](14-aspnet-core-y-blazor.md) | Web | .NET 7 | 🟢 GA | Caché de respuestas en servidor |
| [OverloadResolutionPriority](10-lenguajes-csharp-fsharp-vb.md) | Lenguaje | .NET 9 | 🟢 GA | Prioridad explícita de sobrecargas para autores de bibliotecas |

## P

| Capacidad | Área | Desde | Estado | Descripción |
|---|---|:---:|---|---|
| [params collections](10-lenguajes-csharp-fsharp-vb.md) | Lenguaje | .NET 9 | 🟢 GA | params con Span y colecciones (C# 13) |
| [Partial constructors](10-lenguajes-csharp-fsharp-vb.md) | Lenguaje | .NET 10 | 🟢 GA | Constructores y eventos parciales (C# 14) |
| [Partial properties](10-lenguajes-csharp-fsharp-vb.md) | Lenguaje | .NET 9 | 🟢 GA | Propiedades e indexadores parciales (C# 13) |
| [Passkeys en Identity](14-aspnet-core-y-blazor.md) | Seguridad | .NET 10 | 🟢 GA | Soporte de WebAuthn y passkeys en ASP.NET Core Identity |
| [Patrones relacionales y lógicos](10-lenguajes-csharp-fsharp-vb.md) | Lenguaje | .NET 5 | 🟢 GA | and, or, not, <, > dentro de patrones (C# 9) |
| [PersistedAssemblyBuilder](13-bibliotecas-base.md) | Bibliotecas base | .NET 9 | 🟢 GA | Guardar ensamblados emitidos en disco |
| [Persistencia de estado Blazor](14-aspnet-core-y-blazor.md) | Web | .NET 10 | 🟢 GA | Estado declarativo y persistencia de circuitos |
| [Plantilla mcpserver en el SDK](18-ia-en-net.md) | IA | .NET 11 | 🟡 RC | dotnet new mcpserver sin instalar plantillas |
| [Primary constructors](10-lenguajes-csharp-fsharp-vb.md) | Lenguaje | .NET 8 | 🟢 GA | Constructores primarios en clases y structs (C# 12) |
| [PriorityQueue](13-bibliotecas-base.md) | Bibliotecas base | .NET 6 | 🟢 GA | Cola de prioridad con montículo mínimo |
| [Process.RunAndCaptureText](13-bibliotecas-base.md) | Bibliotecas base | .NET 11 | 🟡 RC | Ejecutar un proceso y capturar su salida en una llamada |
| [Publicación de contenedores](12-aot-despliegue-y-contenedores.md) | SDK | .NET 7 | 🟢 GA | dotnet publish crea imágenes OCI sin Dockerfile |

## R

| Capacidad | Área | Desde | Estado | Descripción |
|---|---|:---:|---|---|
| [Rate limiting](14-aspnet-core-y-blazor.md) | Web | .NET 7 | 🟢 GA | Middleware y primitivas System.Threading.RateLimiting |
| [Raw string literals](10-lenguajes-csharp-fsharp-vb.md) | Lenguaje | .NET 7 | 🟢 GA | Cadenas con triple comilla (C# 11) |
| [Record structs](10-lenguajes-csharp-fsharp-vb.md) | Lenguaje | .NET 6 | 🟢 GA | record struct y readonly record struct (C# 10) |
| [Records](10-lenguajes-csharp-fsharp-vb.md) | Lenguaje | .NET 5 | 🟢 GA | Tipos con igualdad por valor y mutación no destructiva con with (C# 9) |
| [ref fields](10-lenguajes-csharp-fsharp-vb.md) | Lenguaje | .NET 7 | 🟢 GA | Campos ref y scoped en ref struct (C# 11) |
| [Regex source generator](13-bibliotecas-base.md) | Bibliotecas base | .NET 7 | 🟢 GA | GeneratedRegex y modo NonBacktracking de tiempo lineal |
| [Reporte de fallos en proceso](11-runtime-jit-y-gc.md) | Runtime | .NET 11 | 🟡 RC | Crash report en Linux y macOS sin monitor externo |
| [required members](10-lenguajes-csharp-fsharp-vb.md) | Lenguaje | .NET 7 | 🟢 GA | Inicialización obligatoria verificada por el compilador (C# 11) |
| [Resolución DNS tipada](13-bibliotecas-base.md) | Bibliotecas base | .NET 11 | 🟡 RC | DnsResolver para registros DNS |
| [Runtime Async](11-runtime-jit-y-gc.md) | Runtime | .NET 11 | 🟡 Preview | Suspensión async gestionada por el runtime; las bibliotecas ya compilan con ella |

## S

| Capacidad | Área | Desde | Estado | Descripción |
|---|---|:---:|---|---|
| [SDK C# de MCP](18-ia-en-net.md) | IA | .NET 10 | 🟢 GA | Plantilla mcpserver y SDK oficial para Model Context Protocol |
| [SearchValues](13-bibliotecas-base.md) | Bibliotecas base | .NET 8 | 🟢 GA | Búsqueda vectorizada de conjuntos |
| [Seguridad de memoria](10-lenguajes-csharp-fsharp-vb.md) | Lenguaje | .NET 11 | 🟡 Preview | Nuevas reglas unsafe; requiere preview y una bandera |
| [Server-Sent Events](14-aspnet-core-y-blazor.md) | Web | .NET 10 | 🟢 GA | TypedResults.ServerSentEvents |
| [Single-file apps](12-aot-despliegue-y-contenedores.md) | AOT y despliegue | .NET 5 | 🟢 GA | Publicación en un solo ejecutable |
| [SLNX](19-sdk-herramientas-y-pruebas.md) | SDK | .NET 10 | 🟢 GA | Formato de solución XML predeterminado en dotnet new sln |
| [Source generator de JSON](13-bibliotecas-base.md) | Bibliotecas base | .NET 6 | 🟢 GA | JsonSerializerContext con metadatos en compilación |
| [Source generators](19-sdk-herramientas-y-pruebas.md) | SDK | .NET 5 | 🟢 GA | Código generado por Roslyn durante la compilación |
| [Stack allocation de boxes](11-runtime-jit-y-gc.md) | Runtime | .NET 9 | 🟢 GA | Asignación en pila de objetos que no escapan |
| [Streams en memoria](13-bibliotecas-base.md) | Bibliotecas base | .NET 11 | 🟡 RC | ReadOnlyMemoryStream, StringStream y afines |
| [System.Text.Json maduro](13-bibliotecas-base.md) | Bibliotecas base | .NET 5 | 🟢 GA | Records, campos, referencias circulares y extensiones de HttpClient |
| [System.Threading.Lock](10-lenguajes-csharp-fsharp-vb.md) | Lenguaje | .NET 9 | 🟢 GA | Nuevo tipo Lock integrado con la instrucción lock (C# 13) |

## T

| Capacidad | Área | Desde | Estado | Descripción |
|---|---|:---:|---|---|
| [Tablas temporales EF Core](15-datos-y-ef-core.md) | Datos | .NET 6 | 🟢 GA | Temporal tables, modelos compilados y migration bundles |
| [Tar APIs](13-bibliotecas-base.md) | Bibliotecas base | .NET 7 | 🟢 GA | System.Formats.Tar en la biblioteca base |
| [Task.WhenEach](13-bibliotecas-base.md) | Bibliotecas base | .NET 9 | 🟢 GA | Procesar tareas a medida que terminan |
| [Tensor<T>](18-ia-en-net.md) | IA | .NET 9 | 🟡 Preview | Tipo tensorial; estable en .NET 10 |
| [Tensor<T> estable](18-ia-en-net.md) | IA | .NET 10 | 🟢 GA | API tensorial finalizada en System.Numerics.Tensors |
| [TensorPrimitives](18-ia-en-net.md) | IA | .NET 8 | 🟢 GA | Operaciones numéricas vectorizadas para IA |
| [TimeProvider](13-bibliotecas-base.md) | Bibliotecas base | .NET 8 | 🟢 GA | Abstracción de tiempo comprobable |
| [Top-level statements](10-lenguajes-csharp-fsharp-vb.md) | Lenguaje | .NET 5 | 🟢 GA | Programa sin clase Program ni Main explícitos (C# 9) |
| [Tracing nativo en ASP.NET Core](17-cloud-native-aspire-y-observabilidad.md) | Nube | .NET 11 | 🟡 RC | Atributos semánticos OpenTelemetry sin biblioteca de instrumentación |

## U

| Capacidad | Área | Desde | Estado | Descripción |
|---|---|:---:|---|---|
| [Ubuntu 26.04 resolute](12-aot-despliegue-y-contenedores.md) | AOT y despliegue | .NET 11 | 🟡 RC | Imagen predeterminada de .NET 11 |
| [Union types](10-lenguajes-csharp-fsharp-vb.md) | Lenguaje | .NET 11 | 🟡 RC | Tipos union con exhaustividad en switch (C# 15) |
| [Uniones en System.Text.Json](13-bibliotecas-base.md) | Bibliotecas base | .NET 11 | 🟡 RC | Serialización de uniones, JSONL y polimorfismo ampliado |
| [Usuario no root y puerto 8080](12-aot-despliegue-y-contenedores.md) | AOT y despliegue | .NET 8 | 🟢 GA | Imágenes con usuario app (UID 1654) y puerto predeterminado 8080 |
| [UTF-8 literals](10-lenguajes-csharp-fsharp-vb.md) | Lenguaje | .NET 7 | 🟢 GA | Sufijo u8 para ReadOnlySpan<byte> (C# 11) |

## V

| Capacidad | Área | Desde | Estado | Descripción |
|---|---|:---:|---|---|
| [Validación asíncrona](13-bibliotecas-base.md) | Bibliotecas base | .NET 11 | 🟡 RC | AsyncValidationAttribute e IAsyncValidatableObject |
| [Validación en Minimal APIs](14-aspnet-core-y-blazor.md) | Web | .NET 10 | 🟢 GA | AddValidation con generación de código |

## W

| Capacidad | Área | Desde | Estado | Descripción |
|---|---|:---:|---|---|
| [W^X](20-seguridad-y-cadena-de-suministro.md) | Seguridad | .NET 6 | 🟢 GA | Páginas nunca escribibles y ejecutables a la vez; por defecto desde .NET 7 |
| [WebSocketStream](13-bibliotecas-base.md) | Bibliotecas base | .NET 10 | 🟢 GA | API de Stream sobre WebSocket |
| [Windows Arm64](11-runtime-jit-y-gc.md) | Runtime | .NET 5 | 🟢 GA | Soporte nativo de Windows sobre Arm64 e intrínsecos Arm64 |
| [WinForms modo oscuro](16-clientes-maui-wpf-winforms.md) | Clientes | .NET 9 | 🧪 Experimental | Color mode y API asíncronas para formularios |
| [WinForms visual styles](16-clientes-maui-wpf-winforms.md) | Clientes | .NET 11 | 🟡 RC | Estilos modernos y escenarios de quiosco |
| [Workloads del SDK](19-sdk-herramientas-y-pruebas.md) | SDK | .NET 6 | 🟢 GA | dotnet workload para componentes opcionales |
| [WPF Fluent](16-clientes-maui-wpf-winforms.md) | Clientes | .NET 9 | 🟢 GA | Tema Fluent para WPF |
| [Write barrier Arm64](11-runtime-jit-y-gc.md) | Runtime | .NET 10 | 🟢 GA | Reducción de pausas de GC de 8 % a más de 20 % en pruebas |

## X

| Capacidad | Área | Desde | Estado | Descripción |
|---|---|:---:|---|---|
| [X25519](20-seguridad-y-cadena-de-suministro.md) | Seguridad | .NET 11 | 🟡 RC | Intercambio de claves X25519 y AES Key Wrap |
| [XAML Incremental Hot Reload](16-clientes-maui-wpf-winforms.md) | Clientes | .NET 11 | 🟡 RC | Motor incremental de Hot Reload para XAML |

## Z

| Capacidad | Área | Desde | Estado | Descripción |
|---|---|:---:|---|---|
| [Zstandard](13-bibliotecas-base.md) | Bibliotecas base | .NET 11 | 🟡 RC | Compresión Zstandard en System.IO.Compression |

---

<div align="center">

[⬅ 22 · Guías de decisión](22-guias-de-decision.md) · [🏠 Índice](../README.md) · [24 · Laboratorio ➡](24-laboratorio.md)

</div>
