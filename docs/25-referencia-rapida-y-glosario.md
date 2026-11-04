<div align="center">

# 25 · Referencia rápida y glosario

**Comandos, propiedades MSBuild, variables de entorno, términos y fuentes oficiales en un solo lugar**

[⬅ 24 · Laboratorio](24-laboratorio.md) · [🏠 Índice](../README.md)

</div>

---

## Contenido

1. [Versiones de un vistazo](#1-versiones-de-un-vistazo)
2. [Comandos esenciales](#2-comandos-esenciales)
3. [Propiedades de MSBuild](#3-propiedades-de-msbuild)
4. [Variables de entorno](#4-variables-de-entorno)
5. [Diagnósticos frecuentes](#5-diagnósticos-frecuentes)
6. [Glosario](#6-glosario)
7. [Fuentes oficiales](#7-fuentes-oficiales)

---

## 1. Versiones de un vistazo

| .NET | C# | F# | EF Core | ASP.NET Core | Tipo | Fin | Tema |
|:---:|:---:|:---:|:---:|:---:|:---:|---|---|
| 5 | 9 | 5 | 5 | 5 | STS | ⛔ 10-may-2022 | Unificación |
| 6 | 10 | 6 | 6 | 6 | LTS | ⛔ 12-nov-2024 | Consolidación |
| 7 | 11 | 7 | 7 | 7 | STS | ⛔ 14-may-2024 | Velocidad |
| 8 | 12 | 8 | 8 | 8 | LTS | 🟠 10-nov-2026 | Nube nativa |
| 9 | 13 | 9 | 9 | 9 | STS | 🟠 10-nov-2026 | Adaptación |
| 10 | 14 | 10 | 10 | 10 | LTS | 🟢 14-nov-2028 | Madurez |
| 11 | 15 | 11 | 11 | 11 | STS | 🟡 Nov-2028 | Reescritura silenciosa |

---

## 2. Comandos esenciales

| Tarea | Comando |
|---|---|
| Ver instalación | `dotnet --info` |
| Listar SDK y runtimes | `dotnet --list-sdks` · `dotnet --list-runtimes` |
| Fijar SDK | `dotnet new globaljson --sdk-version 10.0.403` |
| Crear solución | `dotnet new sln` (`.slnx`) |
| Crear API | `dotnet new webapi` |
| Crear API AOT | `dotnet new webapiaot` |
| Crear servidor MCP | `dotnet new mcpserver` |
| Ejecutar un archivo | `dotnet run app.cs` |
| Variable al ejecutar | `dotnet run -e CLAVE=valor` 🆕 |
| Recarga en caliente | `dotnet watch` |
| Herramienta sin instalar | `dnx nombre` |
| Publicar contenedor | `dotnet publish -t:PublishContainer` |
| Publicar AOT | `dotnet publish -p:PublishAot=true` |
| Paquetes vulnerables | `dotnet list package --vulnerable --include-transitive` |
| Por qué hay un paquete | `dotnet nuget why <proyecto> <paquete>` |
| Formato | `dotnet format` |
| Migrar solución | `dotnet sln migrate` |

---

## 3. Propiedades de MSBuild

| Propiedad | Efecto |
|---|---|
| `TargetFramework` | TFM |
| `Nullable` | Análisis de nulos |
| `ImplicitUsings` | `using` globales |
| `LangVersion` | Versión de C# |
| `TreatWarningsAsErrors` | Advertencias como errores |
| `AnalysisLevel` | Nivel de analizadores |
| `PublishAot` | Native AOT |
| `PublishTrimmed` | Recorte |
| `PublishReadyToRun` | Precompilación |
| `PublishSingleFile` | Archivo único |
| `InvariantGlobalization` | Sin ICU |
| `ServerGarbageCollection` | Server GC |
| `TieredPGO` | PGO dinámico |
| `IsAotCompatible` | Analizadores de AOT |
| `NuGetAuditMode` | `direct` o `all` |
| `CheckSdkVulnerabilities` | Aviso con SDK fuera de soporte |
| `ContainerFamily` | Variante de imagen |
| `Features` | `runtime-async=on` 🆕 |
| `UseRuntimeAsync` | `false` para desactivar 🆕 |

---

## 4. Variables de entorno

| Variable | Función |
|---|---|
| `ASPNETCORE_ENVIRONMENT` | Entorno de la app |
| `ASPNETCORE_HTTP_PORTS` | Puertos HTTP |
| `DOTNET_ROLL_FORWARD` | Política de versión |
| `DOTNET_GCHeapHardLimitPercent` | Límite de heap |
| `DOTNET_GCDynamicAdaptationMode` | DATAS |
| `DOTNET_TieredPGO` | PGO |
| `DOTNET_gcServer` | Server GC |
| `DOTNET_JitDisasm` | Muestra ensamblador |
| `DOTNET_EnableCrashReport` | Informe de fallo |
| `DOTNET_CLI_TELEMETRY_OPTOUT` | Desactiva telemetría de la CLI |
| `DOTNET_CLI_ENABLEAOT` | `false` desactiva la entrada AOT de CLI 🆕 |
| `FORCE_COLOR` | Fuerza color en consola 🆕 |
| `OTEL_EXPORTER_OTLP_ENDPOINT` | Destino OTLP |

---

## 5. Diagnósticos frecuentes

| Código | Significado | Acción |
|---|---|---|
| `NETSDK1045` | El SDK no admite el TFM | Actualiza el SDK |
| `NETSDK1138` | TFM fuera de soporte | Migra |
| `NETSDK1239` | SDK fuera de soporte | Actualiza |
| `NU1901`–`NU1904` | Paquete vulnerable | Actualiza |
| `NU1510` | Paquete podable | Quita la referencia |
| `IL2026` | No compatible con recorte | Reemplaza o anota |
| `IL3050` | No compatible con AOT | Reemplaza |
| `SYSLIB0011` | `BinaryFormatter` | Migra |
| `SYSLIB5006` | API poscuántica experimental | Opt-in consciente |
| `CS8509` | `switch` no exhaustivo | Agrega caso |

---

## 6. Glosario

| Término | Definición |
|---|---|
| **AOT** | Compilación antes de ejecutar |
| **Aspire** | Stack para definir y ejecutar apps distribuidas en código |
| **BCL** | Bibliotecas base de .NET |
| **Blazor** | Framework de UI web con C# |
| **Chiseled** | Imagen Ubuntu mínima sin shell ni gestor de paquetes |
| **CLR** | Motor de ejecución de .NET |
| **CoreCLR** | Runtime principal multiplataforma |
| **Crossgen2** | Compilador ReadyToRun |
| **CVE** | Identificador público de vulnerabilidad |
| **DATAS** | Adaptación del heap de Server GC a la carga |
| **De-abstracción** | Eliminar el costo de interfaces y enumeradores en el JIT |
| **Devirtualización** | Convertir una llamada virtual en directa |
| **EventPipe** | Mecanismo de trazas multiplataforma |
| **Feature band** | Serie de SDK, como `10.0.4xx` |
| **File-based app** | App C# de un archivo sin proyecto |
| **Go-Live** | Licencia que permite producción en un RC |
| **Hot Reload** | Aplicar cambios a una app en ejecución |
| **ILC** | Compilador de Native AOT |
| **JIT** | Compilación durante la ejecución |
| **Kestrel** | Servidor web de ASP.NET Core |
| **LTS** | Soporte largo, mínimo 3 años |
| **MCP** | Protocolo para exponer herramientas a modelos |
| **MEAI** | Microsoft.Extensions.AI |
| **Mono** | Runtime alternativo, base de móvil y WASM |
| **MTP** | Microsoft.Testing.Platform |
| **OSR** | Sustituir código de un método en ejecución |
| **OTLP** | Protocolo de OpenTelemetry |
| **PGO** | Optimización guiada por perfil |
| **PQC** | Criptografía poscuántica |
| **R2R** | ReadyToRun: código nativo junto al IL |
| **RAG** | Generación aumentada con recuperación |
| **Regiones** | Unidades de memoria del GC desde .NET 7 |
| **RID** | Identificador de runtime, como `linux-x64` |
| **Roslyn** | Compilador de C# y VB |
| **Runtime Async** | `async` gestionado por el runtime |
| **RyuJIT** | Compilador JIT de CoreCLR |
| **SBOM** | Inventario de componentes de software |
| **Source generator** | Código generado durante la compilación |
| **SSE** | Eventos enviados por el servidor |
| **STS** | Soporte estándar de 24 meses |
| **SVE** | Vectores escalables de Arm |
| **TFM** | Identificador de plataforma de destino |
| **Tier 0 / Tier 1** | Niveles de compilación del JIT |
| **Trimming** | Eliminar código no usado |
| **Union type** | Tipo cuyo valor pertenece a un conjunto cerrado de casos |
| **W^X** | Memoria nunca escribible y ejecutable a la vez |
| **WASM** | WebAssembly |

---

## 7. Fuentes oficiales

| Fuente | Enlace |
|---|---|
| Documentación | [learn.microsoft.com/dotnet](https://learn.microsoft.com/dotnet/) |
| Descargas | [dotnet.microsoft.com/download](https://dotnet.microsoft.com/download) |
| Política de soporte | [Support Policy](https://dotnet.microsoft.com/platform/support/policy/dotnet-core) |
| Notas de versión | [dotnet/core](https://github.com/dotnet/core/tree/main/release-notes) |
| Blog oficial | [devblogs.microsoft.com/dotnet](https://devblogs.microsoft.com/dotnet/) |
| Runtime | [dotnet/runtime](https://github.com/dotnet/runtime) |
| Compilador | [dotnet/roslyn](https://github.com/dotnet/roslyn) |
| ASP.NET Core | [dotnet/aspnetcore](https://github.com/dotnet/aspnetcore) |
| EF Core | [dotnet/efcore](https://github.com/dotnet/efcore) |
| Aspire | [aspire.dev](https://aspire.dev/) |
| Imágenes | [dotnet/dotnet-docker](https://github.com/dotnet/dotnet-docker) |

---

<div align="center">

[⬅ 24 · Laboratorio](24-laboratorio.md) · [🏠 Índice](../README.md)

</div>
