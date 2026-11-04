// .NET 9 · C# 13: params Span, Lock, Task.WhenEach, CountBy, Guid v7, Base64Url
// Ejecuta: dotnet run ejemplos/net09-adaptacion.cs

using System.Buffers.Text;

Console.WriteLine(Sumar(1, 2, 3));

var candado = new Lock();
lock (candado)
{
    Console.WriteLine("Sección crítica con System.Threading.Lock");
}

var tareas = Enumerable.Range(1, 3).Select(async i =>
{
    await Task.Delay(50 * (4 - i));
    return i;
});
await foreach (var t in Task.WhenEach(tareas))
    Console.WriteLine($"Terminó: {await t}");

foreach (var (letra, veces) in new[] { "a", "b", "a" }.CountBy(x => x))
    Console.WriteLine($"{letra}: {veces}");

Console.WriteLine(Guid.CreateVersion7().ToString()[14]);   // Versión 7
Console.WriteLine(Base64Url.EncodeToString([1, 2, 3, 250]));

static int Sumar(params ReadOnlySpan<int> numeros)
{
    int total = 0;
    foreach (var n in numeros) total += n;
    return total;
}
