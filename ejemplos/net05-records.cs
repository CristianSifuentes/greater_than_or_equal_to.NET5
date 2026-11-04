// .NET 5 · C# 9: records, with, top-level statements y patrones relacionales
// Ejecuta: dotnet run ejemplos/net05-records.cs

var original = new Persona("Ada", "Lovelace");
var casada = original with { Apellido = "King" };

Console.WriteLine(original);
Console.WriteLine(casada);
Console.WriteLine($"Igualdad por valor: {original == new Persona("Ada", "Lovelace")}");

foreach (var edad in new[] { -1, 12, 36, 80 })
    Console.WriteLine($"{edad}: {Etapa(edad)}");

static string Etapa(int edad) => edad switch
{
    < 0 => "inválida",
    < 18 => "menor",
    >= 18 and < 65 => "adulta",
    _ => "mayor",
};

public record Persona(string Nombre, string Apellido);
