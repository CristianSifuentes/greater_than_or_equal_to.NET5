// .NET 10 · C# 14: extension, field, ?.=, LeftJoin, orden numérico y JSON estricto
// Ejecuta: dotnet run ejemplos/net10-madurez.cs

#:property PublishAot=false

using System.Globalization;
using System.Text.Json;

int[] vacio = [];
Console.WriteLine($"Vacía: {vacio.EstaVacia}");

var u = new Usuario { Nombre = "  Ada  " };
Console.WriteLine($"[{u.Nombre}]");

Usuario? nadie = null;
nadie?.Nombre = "No se asigna";
Console.WriteLine(nadie is null);

var clientes = new[] { (Id: 1, Nombre: "Ada"), (Id: 2, Nombre: "Grace") };
var pedidos = new[] { (ClienteId: 1, Total: 9m) };
foreach (var fila in clientes.LeftJoin(pedidos, c => c.Id, p => p.ClienteId, (c, p) => $"{c.Nombre}: {p.Total}"))
    Console.WriteLine(fila);

var comparador = StringComparer.Create(CultureInfo.InvariantCulture, CompareOptions.NumericOrdering);
string[] nombres = ["archivo10", "archivo2"];
Array.Sort(nombres, comparador);
Console.WriteLine(string.Join(", ", nombres));

try
{
    var opciones = new JsonSerializerOptions(JsonSerializerOptions.Strict);
    JsonSerializer.Deserialize<Punto>("""{"X":1,"X":2}""", opciones);
}
catch (JsonException)
{
    Console.WriteLine("JSON estricto rechazó una propiedad duplicada");
}

public record Punto(int X);

public class Usuario
{
    public string Nombre
    {
        get;
        set => field = value?.Trim() ?? throw new ArgumentNullException(nameof(value));
    } = "";
}

public static class Extensiones
{
    extension<T>(IEnumerable<T> fuente)
    {
        public bool EstaVacia => !fuente.Any();
    }
}
