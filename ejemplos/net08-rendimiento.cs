// .NET 8 · C# 12: colecciones, constructores primarios, Frozen, SearchValues, TimeProvider
// Ejecuta: dotnet run ejemplos/net08-rendimiento.cs

using System.Buffers;
using System.Collections.Frozen;

int[] primos = [2, 3, 5, 7];
List<int> mas = [.. primos, 11, 13];
Console.WriteLine(string.Join(",", mas));

FrozenDictionary<string, int> codigos =
    new Dictionary<string, int> { ["MX"] = 52, ["ES"] = 34 }.ToFrozenDictionary();
Console.WriteLine(codigos["MX"]);

SearchValues<char> separadores = SearchValues.Create(",;|");
Console.WriteLine("a,b;c".AsSpan().IndexOfAny(separadores));

var sesion = new Sesion(TimeProvider.System);
Console.WriteLine($"Expirada: {sesion.Expirada}");

public class Sesion(TimeProvider reloj)
{
    private readonly DateTimeOffset _inicio = reloj.GetUtcNow();
    public bool Expirada => reloj.GetUtcNow() - _inicio > TimeSpan.FromMinutes(30);
}
