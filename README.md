# .NET Versions Highlights (5 to 10)

## Table of Contents

- [1. .NET 5 (November 2020)](#1-net-5-november-2020)
- [2. .NET 6 (November 2021 - LTS)](#2-net-6-november-2021---lts)
- [3. .NET 7 (November 2022)](#3-net-7-november-2022)
- [4. .NET 8 (November 2023 - LTS)](#4-net-8-november-2023---lts)
- [5. .NET 9 (Expected November 2024)](#5-net-9-expected-november-2024)
- [6. .NET 10 (Expected November 2025 - LTS)](#6-net-10-expected-november-2025---lts)

---

## 1. .NET 5 (November 2020)

**Overview**:
- First release of the unified .NET platform (merging .NET Core and .NET Framework).
- Marked the beginning of the modern .NET (post-Core).

**Key Features**:
- Single SDK and runtime across project types.
- Improved performance and GC enhancements.
- Windows ARM64 support.
- C# 9.0 support with top-level statements, records, and pattern matching improvements.
- System.Text.Json enhancements.

**Advanced Technical Highlights**:
- Introduction of source generators.
- Enhanced RyuJIT performance.
- Cross-platform development improvements.
- Reduced container image sizes.

[More information about .NET 5 here.](https://github.com/CristianSifuentes/.NET5)


---

## 2. .NET 6 (November 2021 - LTS)

**Overview**:
- Long-Term Support (LTS) release.
- First full-fledged unified platform.

**Key Features**:
- Hot reload for improved development cycle.
- Minimal APIs for lightweight web applications.
- Better cloud-native support.
- C# 10 support (global usings, file-scoped namespaces, record structs).

**Advanced Technical Highlights**:
- Significant Blazor performance improvements.
- Profile-guided optimization (PGO).
- Improved startup time and reduced memory usage.
- Native AOT (Ahead-of-Time) compilation improvements.

[More information about .NET 6 here.](https://github.com/CristianSifuentes/.NET6)


---

## 3. .NET 7 (November 2022)

**Overview**:
- Current (non-LTS) release with strong focus on performance.

**Key Features**:
- Continued enhancements to Minimal APIs.
- Performance-focused updates across the base class library.
- C# 11 support (list patterns, raw string literals, required members).

**Advanced Technical Highlights**:
- Native AOT becomes generally available.
- On-stack replacement (OSR) for runtime method replacement.
- Dynamic PGO.
- System.Linq and LINQ improvements with better allocations and speed.

[More information about .NET 7 here.](https://github.com/CristianSifuentes/.NET7)


---

## 4. .NET 8 (November 2023 - LTS)

**Overview**:
- LTS version with major enhancements in cloud, desktop, and mobile support.

**Key Features**:
- Unified MAUI and Blazor Hybrid application model.
- Built-in support for AI/ML workloads.
- ASP.NET Core performance and observability enhancements.
- C# 12 support (primary constructors, alias directives).

**Advanced Technical Highlights**:
- Native AOT support for ASP.NET Core apps.
- Improvements to GC pause time and throughput.
- SIMD and hardware intrinsics extended.
- Enhanced diagnostics with EventPipe and dotnet-monitor.

[More information about .NET 8 here.](https://github.com/CristianSifuentes/.NET8)

---

## 5. .NET 9 (Expected November 2024)

**Overview**:
- Expected to be a current release focused on cloud-native and AI workload enhancements.

**Projected Key Features**:
- Deeper integration with AI tooling (e.g., ONNX, ML.NET).
- Enhanced microservice templates and Dapr integration.
- Expanded MAUI functionality and ecosystem.
- Anticipated C# 13 support.

**Expected Technical Enhancements**:
- Further improvements to Native AOT.
- JIT enhancements for cloud-native scenarios.
- Better startup and memory footprint.
- Distributed tracing and logging enhancements.

[More information about .NET 9 here.](https://github.com/CristianSifuentes/.NET9)


---

## 6. .NET 10 (Expected November 2025 - LTS)

**Overview**:
- Will be a major LTS milestone.
- Expected to fully realize AI-native, distributed, and cloud-native application paradigms.

**Projected Key Features**:
- Full support for WASM with threads and GC.
- Native integration of AI code assistance.
- Support for persistent memory and next-gen hardware.
- C# 14 with deeper language abstraction tools.

**Expected Technical Advancements**:
- Enhanced GPU compute support via DirectML and CUDA bindings.
- Fully modular runtime and SDK.
- Optimized support for serverless architectures.
- Deep integration with confidential computing environments.

[More information about .NET 10 here.](https://github.com/CristianSifuentes/.NET10)


---

> **Note**: .NET 9 and 10 are projected based on official Microsoft planning cycles and community roadmaps. Final features will depend on ongoing development and feedback.

