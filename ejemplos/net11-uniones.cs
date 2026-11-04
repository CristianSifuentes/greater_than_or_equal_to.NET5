// .NET 11 · C# 15: union, closed, with(...), indexadores de extensión y saltos etiquetados
// Requiere el SDK de .NET 11. Validado con 11.0.100-rc.3.26522.148.
// Ejecuta: dotnet run ejemplos/net11-uniones.cs

#:property PublishAot=false

using System.Diagnostics;
using System.IO.Compression;
using System.Numerics;
using System.Text;
using System.Text.Json;

Console.WriteLine(Describir(new Exito("listo")));
Console.WriteLine(Describir(new Fallo(404)));
Console.WriteLine(JsonSerializer.Serialize<Resultado>(new Exito("hola")));

Console.WriteLine(Puerta(new Abierta(40)));

string[] valores = ["uno", "dos"];
List<string> lista = [with(capacity: 32), .. valores];
HashSet<string> conjunto = [with(StringComparer.OrdinalIgnoreCase), "Hola", "HOLA"];
Console.WriteLine($"Capacidad {lista.Capacity}, únicos {conjunto.Count}");

IEnumerable<int> numeros = Enumerable.Range(1, 10);
Console.WriteLine(numeros[2]);

int[][] malla = [[1, 2], [3, 4]];
int encontrado = 0;
fila: foreach (var r in malla)
{
    foreach (var c in r)
    {
        if (c == 2) continue fila;
        if (c == 3) { encontrado = c; break fila; }
    }
}
Console.WriteLine(encontrado);

Console.WriteLine(Decimal64.Parse("0.1") + Decimal64.Parse("0.2"));
Console.WriteLine(0.1 + 0.2);

var izquierda = new[] { (1, "a"), (2, "b") };
var derecha = new[] { (2, "x"), (3, "y") };
foreach (var (a, b) in izquierda.FullJoin(derecha, p => p.Item1, q => q.Item1))
    Console.WriteLine($"{a} | {b}");

using var memoria = new MemoryStream();
using (var z = new ZstandardStream(memoria, CompressionMode.Compress, leaveOpen: true))
    z.Write(Encoding.UTF8.GetBytes(new string('a', 10_000)));
Console.WriteLine($"10000 bytes en {memoria.Length} con Zstandard");

Console.WriteLine(Process.RunAndCaptureText("dotnet", ["--version"]).StandardOutput.Trim());

static string Describir(Resultado r) => r switch
{
    Exito(var m) => m,
    Fallo(var c) => $"error {c}",
};

static string Puerta(Estado e) => e switch
{
    Cerrada => "cerrada",
    Abierta(var p) => $"{p}% abierta",
};

public record Exito(string Mensaje);
public record Fallo(int Codigo);
public union Resultado(Exito, Fallo);

public closed record class Estado;
public record class Cerrada : Estado;
public record class Abierta(float Porcentaje) : Estado;

public static class Secuencias
{
    extension(IEnumerable<int> s)
    {
        public int this[int i] => s.ElementAt(i);
    }
}
