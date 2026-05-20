# .NET Versions Highlights (5 to 11)

## Overview

This document summarizes the evolution of the modern .NET platform from .NET 5 through the .NET 11 preview. It is current as of May 2026 and emphasizes how each release contributed to the unified runtime, developer productivity, cloud-native adoption, and AI-first innovation.

## Support and Release Cadence

- .NET moved to an annual November release cadence starting with .NET 5.
- Even-numbered releases are LTS (long-term support), while odd-numbered releases are STS (standard-term support).
- As of May 2026:
  - .NET 5 reached end-of-life in May 2022.
  - .NET 6 reached end-of-life in November 2024.
  - .NET 7 reached end-of-life in May 2024.
  - .NET 9 reached end-of-life in May 2026.
  - .NET 10 is the current LTS release.
  - .NET 11 is in preview and expected to reach GA in November 2026.

## Table of Contents

- [1. .NET 5 (November 10, 2020)](#1-net-5-november-10-2020)
- [2. .NET 6 (November 8, 2021 - LTS)](#2-net-6-november-8-2021---lts)
- [3. .NET 7 (November 8, 2022)](#3-net-7-november-8-2022)
- [4. .NET 8 (November 14, 2023 - LTS)](#4-net-8-november-14-2023---lts)
- [5. .NET 9 (November 12, 2024)](#5-net-9-november-12-2024)
- [6. .NET 10 (November 11, 2025 - LTS)](#6-net-10-november-11-2025---lts)
- [7. .NET 11 (Preview, GA planned November 2026)](#7-net-11-preview-ga-planned-november-2026)

------------------------------------------------------------------------

## 1. .NET 5 (November 10, 2020)

**Context**
- .NET 5 was the first release after the formal unification of .NET Core and the legacy .NET Framework. It defined the baseline for the modern .NET ecosystem.
- It was intentionally short-lived, with support ending in May 2022, but its influence remains foundational.

**Why it mattered**
- Unified runtime and SDK experience across Windows, Linux, and macOS.
- Established the single-platform vision with a common base class library, tooling, and runtime.
- Made `System.Text.Json` the default serialization library for many workloads.

**Key features**
- C# 9 support: top-level statements, `record` types, `init` accessors, pattern matching enhancements.
- Windows ARM64 support and improved cross-platform runtime stability.
- Performance improvements across RyuJIT, garbage collection, and networking.
- Docker container optimizations with smaller base images.

**Technical highlights**
- Source generators introduced compile-time code generation for serializers, logging, and analyzers.
- Single-file application publishing began to mature.
- `HttpClient` and JSON pipeline improvements enabled faster cloud-native APIs.

**Legacy status**
- .NET 5 remains a milestone release for teams still maintaining older projects, but all new production work should target supported releases such as .NET 10 or .NET 8.

[More information about .NET 5 here.](https://docs.microsoft.com/dotnet/core/dotnet-five)

------------------------------------------------------------------------

## 2. .NET 6 (November 8, 2021 - LTS)

**Context**
- .NET 6 was the first true LTS version of the unified platform and became the mainstream choice for production workloads until November 2024.
- It solidified the .NET developer experience, especially for web, cloud, desktop, and container scenarios.

**Why it mattered**
- Delivered broad ecosystem maturity and stability.
- Brought major productivity improvements for web and API development.
- Became the recommended baseline for modern .NET migrations for several years.

**Key features**
- C# 10 support: global `using` directives, file-scoped namespaces, record structs, improved pattern matching.
- Minimal APIs for fast, lightweight web services.
- Hot reload for faster edit-and-refresh workflows.
- Built-in support for ARM64 and container-friendly builds.

**Technical highlights**
- Blazor performance improvements and WebAssembly enhancements.
- Profile-guided optimization (PGO) for faster startup and throughput.
- Native AOT support on experimental paths, improving startup and memory for console and microservice workloads.
- Enhanced observability with built-in metrics and diagnostics.

**Support note**
- .NET 6 is now out of support, but it remains an important reference point for migration planning and long-term architecture decisions.

[More information about .NET 6 here.](https://docs.microsoft.com/dotnet/core/dotnet-six)

------------------------------------------------------------------------

## 3. .NET 7 (November 8, 2022)

**Context**
- .NET 7 was a performance-focused STS release that pushed the platform forward with innovation rather than broad long-term compatibility.
- Its goal was to advance the runtime, libraries, and native AOT tooling quickly.

**Why it mattered**
- Demonstrated that .NET could rapidly evolve on a yearly cadence.
- Delivered meaningful performance and productivity gains for cloud-native workloads.

**Key features**
- C# 11 support: list patterns, raw string literals, required members, generic math enhancements.
- Continued evolution of Minimal APIs and simplified web application templates.
- Improved JSON source generator coverage and smaller payloads.

**Technical highlights**
- Native AOT support became generally available for more workloads.
- On-stack replacement (OSR) improved live debugging and dynamic runtime updates.
- Dynamic PGO further optimized JIT behavior for production workloads.
- Continued improvements to LINQ and collections to reduce allocations.

**Support note**
- .NET 7 reached end-of-life in May 2024, making .NET 8 and 10 the preferred targets for current deployments.

[More information about .NET 7 here.](https://docs.microsoft.com/dotnet/core/dotnet-seven)

------------------------------------------------------------------------

## 4. .NET 8 (November 14, 2023 - LTS)

**Context**
- .NET 8 is the most recent LTS release with broad support through 2026.
- It accelerated cloud, desktop, and hybrid workloads, while also bringing AI-friendly improvements.

**Why it mattered**
- Marked the first LTS release with production-ready first-class Native AOT support for ASP.NET Core.
- Reinforced .NET as a compelling choice for full-stack and cross-platform development.

**Key features**
- C# 12 support: primary constructors, alias directives, collection expressions, and improved interpolated strings.
- Finalized Blazor and MAUI integration for hybrid mobile/desktop experiences.
- Better observability with native support for EventPipe, dotnet-monitor, and distributed tracing.
- Improved cloud performance with smaller images, faster cold starts, and streamlined container builds.

**Technical highlights**
- Native AOT support for ASP.NET Core and worker services.
- GC improvements for lower pause times and better throughput.
- Extended SIMD and hardware intrinsics for data-intensive workloads.
- More powerful diagnostics and startup tracing.

**Support note**
- .NET 8 remains one of the best supported and most production-ready releases for new applications in 2026.

[More information about .NET 8 here.](https://docs.microsoft.com/dotnet/core/dotnet-eight)

------------------------------------------------------------------------

## 5. .NET 9 (November 12, 2024)

**Context**
- .NET 9 was the latest STS release in 2025 and focused on AI, cloud-native telemetry, and platform evolution.
- It marked the transition from experimental AI support to production-ready AI integration across the stack.

**Why it mattered**
- It expanded .NET's cloud-native capabilities and accelerated the platform's AI story.
- It brought stronger runtime diagnostics, better trimming defaults, and smarter publish pipelines.

**Key features**
- C# 13 support: list patterns, required members improvements, and enhanced lambda syntax.
- Deeper AI integration through built-in connectors and native support for ONNX and ML.NET scenarios.
- Better Dapr and microservice template support.
- Enhanced MAUI and Blazor tooling for modern apps.

**Technical highlights**
- Runtime improvements for cloud-native startup, request handling, and memory usage.
- Enhanced distributed tracing and logging experiences.
- Further refinement of Native AOT and publish trimming.

**Support note**
- .NET 9 reached end-of-life in May 2026, which reinforces the recommendation to use .NET 10 or .NET 8 for production systems.

[More information about .NET 9 here.](https://docs.microsoft.com/dotnet/core/dotnet-nine)

------------------------------------------------------------------------

## 6. .NET 10 (November 11, 2025 - LTS)

**Context**
- .NET 10 is the current LTS release as of May 2026 and represents the most mature, supported foundation for enterprise applications.
- It is positioned for large-scale cloud, serverless, AI-native, and edge workloads.

**Why it mattered**
- It delivered the latest stable set of platform features while preserving the reliability expected from an LTS release.
- It became the recommended target for new production projects in 2026.

**Key features**
- C# 14 support: enhanced pattern matching, collection and tuple improvements, and runtime code generation enhancements.
- Strong WebAssembly support with threaded workloads and improved GC.
- Native integration of AI code assistance and inference primitives.
- First-class support for persistent memory and next-generation hardware acceleration.

**Technical highlights**
- Improved GPU compute support through DirectML and CUDA bindings.
- Modular runtime and SDK structure for smaller footprint deployments.
- Enhanced serverless experience and confidential computing support.
- Better support for distributed systems, service meshes, and hybrid cloud.

**Support note**
- .NET 10 is the recommended production platform in 2026 and will remain supported through 2028.

[More information about .NET 10 here.](https://docs.microsoft.com/dotnet/core/dotnet-ten)

------------------------------------------------------------------------

## 7. .NET 11 (Preview, GA planned November 2026)

**Context**
- .NET 11 is the next STS release and is currently available as preview builds in 2026.
- The release continues the yearly cadence with a focus on AI-first development and even tighter runtime efficiency.

**Why it matters**
- It defines the next wave of innovation for ASP.NET Core, the base class libraries, and the runtime.
- It is the release that will shape migration choices after .NET 10.

**Projected features**
- AI-first framework primitives more deeply integrated into ASP.NET Core and the BCL.
- Smarter native container publishing with even more aggressive trimming, AOT defaults, and smaller footprints.
- Enhanced cloud-native templates with resilience, observability, and runtime diagnostics.
- Anticipated C# 15 support.

**Expected technical advancements**
- Hybrid AOT/JIT adaptive execution for improved startup and steady-state performance.
- Continued GC evolution targeting ultra-low latency microservices.
- Better first-class support for distributed actor models, event-driven systems, and edge scenarios.
- Expanded hardware acceleration support for AI accelerators and ARM advancements.

**Preview note**
- .NET 11 is still under preview and not recommended for most production workloads until after the November 2026 GA release.

[More information about .NET 11 here.](https://docs.microsoft.com/dotnet/core/dotnet-eleven)

------------------------------------------------------------------------

## Practical guidance

- For new production projects in 2026, choose .NET 10 LTS unless you need a preview feature only available in .NET 11.
- For projects already on .NET 8, staying on that LTS release is a strong option through 2026.
- Avoid .NET 5, .NET 6, .NET 7, and .NET 9 for new production deployments because they are no longer supported.
- Use the annual cadence as a planning anchor: even-numbered versions for long-term stability, odd-numbered versions for innovation and faster feature adoption.

> **Note**: .NET follows an annual November release cadence. LTS releases occur every two years (even-numbered versions). .NET 11 is currently in preview as of 2026 and is planned for GA in November 2026.
