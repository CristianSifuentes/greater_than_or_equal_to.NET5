// .NET 7 · C# 11: matemática genérica, list patterns, raw strings y GeneratedRegex
// Ejecuta: dotnet run ejemplos/net07-matematica-generica.cs

using System.Numerics;
using System.Text.RegularExpressions;

Console.WriteLine(Sumar<int>(new[] { 1, 2, 3 }));
Console.WriteLine(Sumar<decimal>(new[] { 1.5m, 2.5m }));
Console.WriteLine(Sumar<double>(new[] { 0.5, 0.25 }));

int[] datos = { 1, 2, 3, 4 };
if (datos is [1, .. var medio, 4])
    Console.WriteLine($"Elementos intermedios: {medio.Length}");

var json = """
    { "nombre": "Ada", "lenguaje": "C#" }
    """;
Console.WriteLine(json);

Console.WriteLine(Patrones.Correo().Count("ana@correo.com y luis@empresa.mx"));

static T Sumar<T>(ReadOnlySpan<T> valores) where T : INumber<T>
{
    T total = T.Zero;
    foreach (var v in valores) total += v;
    return total;
}

public static partial class Patrones
{
    [GeneratedRegex(@"\b[\w.]+@[\w.]+\.\w+\b", RegexOptions.IgnoreCase)]
    public static partial Regex Correo();
}
