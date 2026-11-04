// .NET 6 · C# 10: DateOnly, PriorityQueue, LINQ nuevo y record struct
// Ejecuta: dotnet run ejemplos/net06-consolidacion.cs

DateOnly cumple = new(1815, 12, 10);
TimeOnly apertura = new(9, 30);
Console.WriteLine($"{cumple:yyyy-MM-dd} {apertura:HH:mm}");

var cola = new PriorityQueue<string, int>();
cola.Enqueue("baja", 10);
cola.Enqueue("alta", 1);
Console.WriteLine($"Primero: {cola.Dequeue()}");

var numeros = Enumerable.Range(1, 10).ToArray();
Console.WriteLine($"MaxBy: {numeros.MaxBy(x => x % 7)}");
Console.WriteLine($"Lotes: {string.Join(" | ", numeros.Chunk(4).Select(c => string.Join(",", c)))}");
Console.WriteLine($"Últimos: {string.Join(",", numeros.Take(^3..))}");

var total = new Dinero(1500m, "MXN");
Console.WriteLine(total is { Monto: > 1000m } ? $"Pedido grande: {total}" : "Pedido normal");

public readonly record struct Dinero(decimal Monto, string Moneda);
