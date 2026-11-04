# Laboratorio

Código de las mediciones publicadas en [docs/24-laboratorio.md](../docs/24-laboratorio.md).

```bash
# Microbenchmarks: un runtime por vez, en proceso
cd laboratorio/micro
for t in net8.0 net9.0 net10.0 net11.0; do
  dotnet build -c Release -f $t
  dotnet bin/Release/$t/micro.dll --filter '*' --inProcess --warmupCount 8 --iterationCount 20 --exporters json
done

# Native AOT y JIT
python3 laboratorio/medir_aot.py osx-arm64
```

Necesitas el SDK de .NET 11 y los runtimes 8, 9 y 10.
