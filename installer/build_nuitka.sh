#!/bin/bash
# Build script para Nuitka
# Alternativa a PyInstaller, produce menos falsos positivos de antivirus
set -e
PROJECT_DIR="$(cd "$(dirname "$0")/.." && pwd)"
BUILD_DIR="$PROJECT_DIR/dist"
echo "🔨 Build Nuitka - Workflow Determinista"
echo "======================================="
cd "$PROJECT_DIR"
pip install nuitka
python -m nuitka --standalone --onefile --enable-plugin=tk-inter \
  --include-data-dir=src/web/templates=templates \
  --include-data-dir=src/web/static=static \
  --output-dir="$BUILD_DIR" \
  --product-name="Workflow Determinista" \
  --file-version="1.0.0" \
  src/main.py
echo "✅ Build Nuitka completado"
