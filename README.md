# What's New in .NET 5

##  Table of Contents
- [Overview of .NET 5](#overview-of-net-5)
- [Key Improvements in .NET 5](#key-improvements-in-net-5)
- [Performance Enhancements](#performance-enhancements)
- [New Features](#new-features)
  - [C# 9 Enhancements](#c-9-enhancements)
  - [Source Generators](#source-generators)
  - [F# 5 Enhancements](#f-5-enhancements)
  - [System.Text.Json Improvements](#systemtextjson-improvements)
- [Runtime Enhancements](#runtime-enhancements)
- [Cross-Platform Compatibility](#cross-platform-compatibility)
- [Visual Basic Support](#visual-basic-support)
- [Migration & Compatibility](#migration--compatibility)
- [Conclusion](#conclusion)

---

## Overview of .NET 5
.NET 5 is the next major release of .NET Core following 3.1. The name was changed to **.NET 5 instead of .NET Core 4** for two reasons:
1. Version numbers 4.x were skipped to **avoid confusion with .NET Framework 4.x**.
2. The term **"Core" was dropped** to emphasize that this is the **main implementation of .NET going forward**.

### 🏗 Platform Consolidation
- .NET 5 **unifies** .NET development by replacing .NET Core but **does not replace** .NET Framework.
- ASP.NET Core 5.0 and Entity Framework Core 5.0 **retain "Core"** in their names to avoid confusion with older versions.

---

## Key Improvements in .NET 5
.NET 5 includes **several performance improvements, new features, and enhancements** in runtime, libraries, and programming languages.

### **Performance Enhancements**
- **Garbage Collection (GC) optimizations**.
- Improved **System.Text.Json** performance.
- Enhanced **System.Text.RegularExpressions**.
- **Async `ValueTask` pooling** for reduced memory allocation.
- **Container size optimizations** for better cloud deployments.

---

## New Features
### C# 9 Enhancements
.NET 5 is paired with **C# 9**, introducing several powerful features:

- **Records**: Reference types with value-based equality.
- **Relational pattern matching**: Extends pattern matching with relational operators.
- **Top-level statements**: Allows C# programs without a `Main` method.
- **Function pointers**: Enables interop with native code.

Example of **Top-Level Statements**:
```csharp
System.Console.Write("Hello world!");
```

### Source Generators
.NET 5 introduces **Source Generators**, allowing **code to be generated at compile time**.
- Can inspect existing code and **generate new files** dynamically.
- Improves **compile-time optimizations**.

For more details, see: [Introducing C# Source Generators](https://devblogs.microsoft.com/dotnet/introducing-c-source-generators/).

### F# 5 Enhancements
F# is the functional programming language for .NET. With .NET 5, **F# 5 introduces interpolated strings**, similar to C#.

**Example of String Interpolation**:
```fsharp
let name = "David"
let age = 36
let message = $"{name} is {age} years old."
```

### System.Text.Json Improvements
- **Preserve references** to handle circular dependencies.
- **Serialization extension methods** for `HttpClient`.
- **Support for immutable types and C# 9 records**.
- **Custom converters can handle null values**.
- **Allow writing numbers in quotes** for better compatibility.

---

## Runtime Enhancements
- **Single-File Applications**: Package everything into **one executable**.
- **App Trimming**: Reduces app size by removing unused code.
- **Windows Arm64 Support**: Native support for **Arm64 processors**.

---

## Cross-Platform Compatibility
.NET 5 is fully **cross-platform** and replaces .NET Core. However, it **doesn’t replace .NET Framework**.

| **Technology**      | **Recommended Alternative** |
|---------------------|---------------------------|
| **Web Forms**       | ASP.NET Core Blazor/Razor Pages |
| **Windows Workflow (WF)** | Elsa Workflows |
| **Windows Communication Foundation (WCF)** | gRPC or CoreWCF |

For **.NET 5 apps**, use `net5.0` as the **Target Framework Moniker (TFM)**.

---

##  Visual Basic Support
.NET 5 does **not** introduce new language features for **Visual Basic**, but **extends project support** for:
- Console Apps
- Class Libraries
- WPF Applications
- Windows Forms (WinForms)
- Unit Test Projects (MSTest, NUnit, xUnit)

---

##  Migration & Compatibility
.NET 5 is the **main implementation** going forward, but **.NET Framework 4.x is still supported**.

###  Technologies NOT Ported from .NET Framework
- **Web Forms**
- **Windows Workflow (WF)**
- **Windows Communication Foundation (WCF)** (but CoreWCF is an alternative).

###  Code Sharing
- **For .NET 5 apps** → Use `net5.0`.
- **For compatibility with .NET Framework** → Use `netstandard2.0`.

For more details, see [.NET Standard](https://docs.microsoft.com/en-us/dotnet/standard/net-standard?tabs=net-standard-1-0).

---

##  Conclusion
.NET 5 is a **major step forward** in **unifying .NET** and improving **performance, cross-platform support, and runtime efficiency**. However, **it does not replace .NET Framework**, and some older technologies require alternative solutions.

**Key Takeaways**:
✅ Faster runtime with **performance optimizations**.  
✅ **C# 9, F# 5, and Visual Basic improvements**.  
✅ **Better JSON serialization** with `System.Text.Json`.  
✅ **Single-file applications and App Trimming**.  
✅ **Improved compatibility for cross-platform apps**.

---

###  **Useful Links**
- 🔗 [.NET 5 Download](https://dotnet.microsoft.com/en-us/download/dotnet/5.0)
- 🔗 [C# 9 Features](https://docs.microsoft.com/en-us/dotnet/csharp/whats-new/csharp-9)
- 🔗 [F# 5 Features](https://docs.microsoft.com/en-us/dotnet/fsharp/whats-new/fsharp-5)
- 🔗 [System.Text.Json Updates](https://docs.microsoft.com/en-us/dotnet/standard/serialization/system-text-json-overview)
