using System.Text.Json;
using System.Text.RegularExpressions;
using BenchmarkDotNet.Attributes;
using BenchmarkDotNet.Running;

BenchmarkSwitcher.FromAssembly(typeof(Lab).Assembly).Run(args);

public record Pedido(int Id, string Cliente, decimal Total, DateTime Fecha, string[] Etiquetas);

[MemoryDiagnoser]
public class Lab
{
    int[] _arr = default!;
    IEnumerable<int> _seq = default!;
    List<Pedido> _pedidos = default!;
    string _json = default!;
    Dictionary<string,int> _dict = default!;
    string[] _keys = default!;
    string _texto = default!;
    static readonly Regex _rx = new(@"\b[a-z]+@[a-z]+\.com\b", RegexOptions.Compiled);

    [GlobalSetup]
    public void Setup()
    {
        _arr = Enumerable.Range(0, 1024).ToArray();
        _seq = _arr;
        _pedidos = Enumerable.Range(0, 100).Select(i => new Pedido(i, "cliente-" + i, i * 1.5m, new DateTime(2026, 11, 4), ["a", "b", "c"])).ToList();
        _json = JsonSerializer.Serialize(_pedidos);
        _keys = Enumerable.Range(0, 1000).Select(i => "clave-" + i).ToArray();
        _dict = _keys.ToDictionary(k => k, k => k.Length);
        _texto = string.Concat(Enumerable.Repeat("lorem ipsum dolor sit amet ana@correo.com consectetur ", 200));
    }

    [Benchmark] public int ForeachIEnumerable() { int s = 0; foreach (var x in _seq) s += x; return s; }
    [Benchmark] public int LinqWhereSelectSum() => _arr.Where(x => (x & 1) == 0).Select(x => x * 2).Sum();
    [Benchmark] public string JsonSerializar() => JsonSerializer.Serialize(_pedidos);
    [Benchmark] public List<Pedido>? JsonDeserializar() => JsonSerializer.Deserialize<List<Pedido>>(_json);
    [Benchmark] public int DictionaryLookup() { int s = 0; foreach (var k in _keys) s += _dict[k]; return s; }
    [Benchmark] public int RegexContar() => _rx.Count(_texto);
    [Benchmark] public string[] StringSplit() => _texto.Split(' ');
    [Benchmark] public async Task<int> AsyncCadena() { int s = 0; for (int i = 0; i < 1000; i++) s += await Uno(i); return s; }
    static async Task<int> Uno(int i) { await Task.Yield(); return i; }
    [Benchmark] public int ExcepcionLanzarCapturar() { try { throw new InvalidOperationException(); } catch (InvalidOperationException) { return 1; } }
}
