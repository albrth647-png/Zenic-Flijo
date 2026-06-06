#!/bin/bash
# Build script para PyInstaller
# Convierte el proyecto Python en un solo ejecutable
set -e
PROJECT_DIR="$(cd "$(dirname "$0")/.." && pwd)"
BUILD_DIR="$PROJECT_DIR/dist"
echo "🔨 Build PyInstaller - Workflow Determinista"
echo "============================================"
cd "$PROJECT_DIR"
pip install pyinstaller
pyinstaller --onefile --windowed --name "WorkflowDeterminista_v1.0" \
  --add-data "src/web/templates:templates" \
  --add-data "src/web/static:static" \
  # --icon installer/icon.ico  # Descomenta si tienes un icono .ico
  src/main.py
echo "✅ Build completado: $BUILD_DIR/WorkflowDeterminista_v1.0.exe"
