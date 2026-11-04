<div align="center">

# 19 · SDK, herramientas y pruebas

**CLI, MSBuild, NuGet, aplicaciones de un archivo, analizadores y Microsoft.Testing.Platform**

[⬅ 18 · IA](18-ia-en-net.md) · [🏠 Índice](../README.md) · [20 · Seguridad ➡](20-seguridad-y-cadena-de-suministro.md)

</div>

---

## Contenido

1. [Evolución del SDK](#1-evolución-del-sdk)
2. [Aplicaciones de un archivo](#2-aplicaciones-de-un-archivo)
3. [Instalar y gestionar SDK](#3-instalar-y-gestionar-sdk)
4. [Estructura de repositorio recomendada](#4-estructura-de-repositorio-recomendada)
5. [Gestión central de paquetes](#5-gestión-central-de-paquetes)
6. [Herramientas .NET](#6-herramientas-net)
7. [Analizadores y estilo](#7-analizadores-y-estilo)
8. [Pruebas](#8-pruebas)
9. [Rendimiento de compilación](#9-rendimiento-de-compilación)
10. [IDE](#10-ide)
11. [Pipeline de CI de referencia](#11-pipeline-de-ci-de-referencia)
12. [Referencias](#12-referencias)

---

## 1. Evolución del SDK

| .NET | Novedad |
|:---:|---|
| 5 | Generadores de código |
| 6 | Hot Reload, workloads, validación de paquetes |
| 7 | Publicación de contenedores, `dotnet new` renovado |
| 8 | Terminal Logger, salida de artefactos unificada |
| 9 | Terminal Logger por defecto, BuildChecks, workload sets, NuGet más rápido |
| 10 | **File-based apps**, `dnx`, `.slnx` predeterminado, MTP en `dotnet test`, poda de paquetes |
| 11 🆕 | **CLI Native AOT**, MSBuild server por defecto, `#:include`, pruebas móviles, `dotnetup` 🟡 |

---

## 2. Aplicaciones de un archivo

```csharp
#!/usr/bin/env dotnet
#:package Spectre.Console@0.49.1
#:property PublishAot=false

using Spectre.Console;

AnsiConsole.MarkupLine("[green]Hola desde un archivo[/]");
```

| Directiva | Función | Versión |
|---|---|:---:|
| `#:package Nombre@Versión` | Paquete NuGet | 10 |
| `#:sdk Microsoft.NET.Sdk.Web` | Cambia el SDK | 10 |
| `#:property Clave=Valor` | Propiedad MSBuild | 10 |
| `#:project ../Lib/Lib.csproj` | Referencia a proyecto | 10 |
| `#:include archivo.cs` | Otro archivo | 11 🆕 |
| `#:include ./libs/Lib.dll` | Incluir una DLL | 11 🆕 |

| Comando | Efecto |
|---|---|
| `dotnet run app.cs` | Compila y ejecuta |
| `./app.cs` | Con shebang y permiso de ejecución |
| `dotnet publish app.cs` | Native AOT por defecto |
| `dotnet project convert app.cs` | Convierte a proyecto |
| `dotnet run -e CLAVE=valor app.cs` | Variable de entorno 🆕 |

> [!NOTE]
> Todos los ejemplos de [`ejemplos/`](../ejemplos/) son aplicaciones de un archivo.

---

## 3. Instalar y gestionar SDK

| Método | Cuándo |
|---|---|
| Instalador oficial | Desarrollo normal |
| `winget`, `brew`, `apt` | Gestores de sistema |
| `dotnet-install.sh` o `.ps1` | CI y scripts |
| **`dotnetup`** 🟡 | Varios SDK sin privilegios de administrador |

`dotnetup`, anunciado el **15 de octubre de 2026** en preview pública, instala SDK y runtimes en directorios del usuario y
trata las versiones preview como casos de primera clase:

```bash
dotnetup sdk install preview
```

---

## 4. Estructura de repositorio recomendada

```text
.
├── global.json                  ← fija el SDK
├── Directory.Build.props        ← ajustes comunes
├── Directory.Packages.props     ← versiones de NuGet
├── .editorconfig                ← estilo y severidad
├── nuget.config                 ← orígenes
├── Tienda.slnx                  ← solución XML
├── src/
└── tests/
```

```xml
<!-- Tienda.slnx -->
<Solution>
  <Folder Name="/src/">
    <Project Path="src/Api/Api.csproj" />
  </Folder>
  <Folder Name="/tests/">
    <Project Path="tests/Api.Tests/Api.Tests.csproj" />
  </Folder>
</Solution>
```

`.slnx` es legible y genera pocos conflictos de combinación. Convierte con `dotnet sln migrate`.

---

## 5. Gestión central de paquetes

```xml
<!-- Directory.Packages.props -->
<Project>
  <PropertyGroup>
    <ManagePackageVersionsCentrally>true</ManagePackageVersionsCentrally>
    <CentralPackageTransitivePinningEnabled>true</CentralPackageTransitivePinningEnabled>
  </PropertyGroup>
  <ItemGroup>
    <PackageVersion Include="Polly.Core" Version="8.5.0" />
  </ItemGroup>
</Project>
```

---

## 6. Herramientas .NET

```bash
dnx dotnetsay "Hola"                 # Descarga y ejecuta sin instalar
dotnet tool exec dotnet-ef -- --help
dotnet tool install dotnet-ef        # Local, crea manifiesto
```

| Herramienta | Uso |
|---|---|
| `dotnet-ef` | Migraciones |
| `dotnet-counters`, `-trace`, `-dump`, `-gcdump` | Diagnóstico |
| `dotnet-outdated-tool` | Paquetes viejos |
| `dotnet format` | Formato |
| `upgrade-assistant` | Migraciones asistidas |

---

## 7. Analizadores y estilo

```ini
# .editorconfig
root = true

[*.cs]
dotnet_analyzer_diagnostic.category-Security.severity = error
dotnet_analyzer_diagnostic.category-Reliability.severity = warning
dotnet_diagnostic.CA1873.severity = warning      # Argumentos costosos de log
dotnet_diagnostic.CA2007.severity = none         # ConfigureAwait en apps
csharp_style_namespace_declarations = file_scoped:warning
```

| Regla | Detecta |
|---|---|
| `CA1873` | Evaluación costosa en logging; mejorada en .NET 11 |
| `CA1848` | Usa `LoggerMessage` |
| `CA2016` | No propagar `CancellationToken` |
| `CA2200` | Relanzar perdiendo la pila |
| `IDE0410` 🆕 | Banderas o `goto` reemplazables con saltos etiquetados |

---

## 8. Pruebas

### 8.1 Plataformas

| Elemento | Estado |
|---|---|
| **Microsoft.Testing.Platform (MTP)** | Plataforma moderna; reemplaza a VSTest en nuevos proyectos |
| VSTest | Sigue disponible |
| xUnit v3 | MTP por defecto en plantillas .NET 11 🆕 |
| NUnit, MSTest | Soporte de MTP |

```json
{
  "test": { "runner": "Microsoft.Testing.Platform" }
}
```

### 8.2 `dotnet test` en .NET 11 🆕

```bash
dotnet test --timeout 90s --maximum-failed-tests 5
dotnet test --results-directory-layout per-module
```

### 8.3 Pirámide en .NET

| Nivel | Herramienta |
|---|---|
| Unidad | xUnit, `FakeTimeProvider`, `FakeLogger` |
| Integración web | `WebApplicationFactory<T>` |
| Integración con base real | Testcontainers |
| Distribuido | `Aspire.Hosting.Testing` |
| Contratos | OpenAPI, Pact |
| Carga | k6, NBomber |
| Microbenchmark | BenchmarkDotNet |

```csharp
public class PedidosTests(WebApplicationFactory<Program> app) : IClassFixture<WebApplicationFactory<Program>>
{
    [Fact]
    public async Task Devuelve_404_si_no_existe()
    {
        var cliente = app.CreateClient();
        var r = await cliente.GetAsync("/api/v1/pedidos/999");
        Assert.Equal(HttpStatusCode.NotFound, r.StatusCode);
    }
}
```

> [!TIP]
> No uses el proveedor InMemory de EF Core para probar consultas: no se comporta como una base real. Usa Testcontainers.

---

## 9. Rendimiento de compilación

| Mejora | Versión |
|---|---|
| Servidor de MSBuild por defecto | 11 |
| Comodines más rápidos | 11 |
| Entrada Native AOT | 11: omite 600–700 ms al lanzar herramientas |
| Instaladores deduplicados | 11: tarball Linux x64 de 230 a 189 MB |

---

## 10. IDE

| IDE | .NET 10 | .NET 11 |
|---|---|---|
| Visual Studio 2026 | ✅ | Insiders en RC1 |
| VS Code + C# Dev Kit | ✅ | ✅ |
| JetBrains Rider | ✅ | Consulta su versión |
| Visual Studio para Mac | ⛔ Retirado el 31 de agosto de 2024 | ⛔ |

---

## 11. Pipeline de CI de referencia

```yaml
name: ci
on: [push, pull_request]
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-dotnet@v4
        with:
          global-json-file: global.json
      - run: dotnet restore --locked-mode
      - run: dotnet format --verify-no-changes --no-restore
      - run: dotnet build -c Release --no-restore -warnaserror
      - run: dotnet test -c Release --no-build
      - run: dotnet list package --vulnerable --include-transitive
```

---

## 12. Referencias

- [What's new in the SDK for .NET 11](https://learn.microsoft.com/dotnet/core/whats-new/dotnet-11/sdk)
- [What's new in the SDK for .NET 10](https://learn.microsoft.com/dotnet/core/whats-new/dotnet-10/sdk)
- [Microsoft.Testing.Platform overview](https://learn.microsoft.com/dotnet/core/testing/microsoft-testing-platform-intro)
- [Central Package Management](https://learn.microsoft.com/nuget/consume-packages/central-package-management)
- [Introducing dotnetup](https://devblogs.microsoft.com/dotnet/introducing-dotnetup/)

---

<div align="center">

[⬅ 18 · IA](18-ia-en-net.md) · [🏠 Índice](../README.md) · [20 · Seguridad ➡](20-seguridad-y-cadena-de-suministro.md)

</div>
