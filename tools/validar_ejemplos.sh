#!/usr/bin/env bash
# Compila y ejecuta cada ejemplo con el SDK disponible. Requiere .NET 11 para net11-uniones.cs.
set -u
cd "$(dirname "$0")/.."
fallos=0
for archivo in ejemplos/net*.cs; do
  if salida=$(dotnet run "$archivo" 2>&1); then
    printf '✅ %s\n' "$archivo"
  else
    printf '❌ %s\n%s\n' "$archivo" "$salida"
    fallos=$((fallos + 1))
  fi
done
exit "$fallos"
