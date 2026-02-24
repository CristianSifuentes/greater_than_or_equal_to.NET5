# .NET Versions Highlights (5 to 11)

## Table of Contents

-   [1. .NET 5 (November 10, 2020)](#1-net-5-november-10-2020)
-   [2. .NET 6 (November 8, 2021 - LTS)](#2-net-6-november-8-2021---lts)
-   [3. .NET 7 (November 8, 2022)](#3-net-7-november-8-2022)
-   [4. .NET 8 (November 14, 2023 -
    LTS)](#4-net-8-november-14-2023---lts)
-   [5. .NET 9 (November 12, 2024)](#5-net-9-november-12-2024)
-   [6. .NET 10 (November 11, 2025 -
    LTS)](#6-net-10-november-11-2025---lts)
-   [7. .NET 11 (Planned November
    2026)](#7-net-11-planned-november-2026)

------------------------------------------------------------------------

## 1. .NET 5 (November 10, 2020)

**Overview**: - First release of the unified .NET platform (merging .NET
Core and .NET Framework). - Marked the beginning of the modern .NET
(post-Core).

**Key Features**: - Single SDK and runtime across project types. -
Improved performance and GC enhancements. - Windows ARM64 support. - C#
9.0 support with top-level statements, records, and pattern matching
improvements. - System.Text.Json enhancements.

**Advanced Technical Highlights**: - Introduction of source
generators. - Enhanced RyuJIT performance. - Cross-platform development
improvements. - Reduced container image sizes.

[More information about .NET 5
here.](https://github.com/CristianSifuentes/.NET5)

------------------------------------------------------------------------

## 2. .NET 6 (November 8, 2021 - LTS)

**Overview**: - Long-Term Support (LTS) release. - First full-fledged
unified platform.

**Key Features**: - Hot reload for improved development cycle. - Minimal
APIs for lightweight web applications. - Better cloud-native support. -
C# 10 support (global usings, file-scoped namespaces, record structs).

**Advanced Technical Highlights**: - Significant Blazor performance
improvements. - Profile-guided optimization (PGO). - Improved startup
time and reduced memory usage. - Native AOT (Ahead-of-Time) compilation
improvements.

[More information about .NET 6
here.](https://github.com/CristianSifuentes/.NET6)

------------------------------------------------------------------------

## 3. .NET 7 (November 8, 2022)

**Overview**: - Current (non-LTS) release with strong focus on
performance.

**Key Features**: - Continued enhancements to Minimal APIs. -
Performance-focused updates across the base class library. - C# 11
support (list patterns, raw string literals, required members).

**Advanced Technical Highlights**: - Native AOT becomes generally
available. - On-stack replacement (OSR) for runtime method
replacement. - Dynamic PGO. - System.Linq and LINQ improvements with
better allocations and speed.

[More information about .NET 7
here.](https://github.com/CristianSifuentes/.NET7)

------------------------------------------------------------------------

## 4. .NET 8 (November 14, 2023 - LTS)

**Overview**: - LTS version with major enhancements in cloud, desktop,
and mobile support.

**Key Features**: - Unified MAUI and Blazor Hybrid application model. -
Built-in support for AI/ML workloads. - ASP.NET Core performance and
observability enhancements. - C# 12 support (primary constructors, alias
directives).

**Advanced Technical Highlights**: - Native AOT support for ASP.NET Core
apps. - Improvements to GC pause time and throughput. - SIMD and
hardware intrinsics extended. - Enhanced diagnostics with EventPipe and
dotnet-monitor.

[More information about .NET 8
here.](https://github.com/CristianSifuentes/.NET8)

------------------------------------------------------------------------

## 5. .NET 9 (November 12, 2024)

**Overview**: - Standard-Term Support (STS) release focused on
cloud-native and AI workload enhancements.

**Key Features**: - Deeper integration with AI tooling (e.g., ONNX,
ML.NET). - Enhanced microservice templates and Dapr integration. -
Expanded MAUI functionality and ecosystem. - C# 13 support.

**Advanced Technical Highlights**: - Further improvements to Native
AOT. - JIT enhancements for cloud-native scenarios. - Better startup and
memory footprint. - Distributed tracing and logging enhancements.

[More information about .NET 9
here.](https://github.com/CristianSifuentes/.NET9)

------------------------------------------------------------------------

## 6. .NET 10 (November 11, 2025 - LTS)

**Overview**: - Major Long-Term Support (LTS) milestone. - Fully
optimized for AI-native, distributed, and cloud-native application
paradigms.

**Key Features**: - Full support for WASM with threads and GC. - Native
integration of AI code assistance. - Support for persistent memory and
next-gen hardware. - C# 14 support.

**Advanced Technical Highlights**: - Enhanced GPU compute support via
DirectML and CUDA bindings. - Fully modular runtime and SDK
improvements. - Optimized support for serverless architectures. - Deep
integration with confidential computing environments.

[More information about .NET 10
here.](https://github.com/CristianSifuentes/.NET10)

------------------------------------------------------------------------

## 7. .NET 11 (Planned November 2026)

**Overview**: - Next Standard-Term Support (STS) release in the annual
cadence. - Preview 1 released February 10, 2026. - General Availability
planned for November 2026.

**Projected Key Features**: - Deep AI-first framework primitives
integrated directly into ASP.NET Core and the BCL. - Advanced native
container publishing with improved trimming and AOT defaults. - Enhanced
cloud-native templates with built-in resilience and observability. -
Anticipated C# 15 support.

**Expected Technical Enhancements**: - Next-generation JIT optimizations
with hybrid AOT/JIT adaptive execution. - Further GC evolution targeting
ultra-low latency microservices. - First-class support for distributed
actors and event-driven systems. - Expanded hardware acceleration
support (AI accelerators and ARM optimizations).

[More information about .NET 11 here.](https://github.com/dotnet)

------------------------------------------------------------------------

> **Note**: .NET follows an annual November release cadence. LTS
> releases occur every two years (even-numbered versions). .NET 11 is
> currently in preview as of 2026 and is planned for GA in November
> 2026.
