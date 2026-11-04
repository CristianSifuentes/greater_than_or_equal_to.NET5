using System.Text.Json.Serialization;
var b = WebApplication.CreateSlimBuilder(args);
b.Logging.ClearProviders();
b.Services.ConfigureHttpJsonOptions(o => o.SerializerOptions.TypeInfoResolverChain.Insert(0, Ctx.Default));
var app = b.Build();
app.MapGet("/", () => new Saludo("hola", 2026));
app.Run();
public record Saludo(string Texto, int Anio);
[JsonSerializable(typeof(Saludo))] public partial class Ctx : JsonSerializerContext { }
