# Cómo generar el ejecutable .EXE para el programa de Presupuesto de Obra (GUI)

## Requisitos:
- Python 3 instalado en Windows
- pip instalado
- PyInstaller (puede instalarse con pip)

## Pasos:

1. Abrir la terminal de Windows (CMD)
2. Instalar PyInstaller:
   pip install pyinstaller

3. Navegar a la carpeta donde está `main_gui.py`:
   cd C:\ruta\a\tu\carpeta\presupuesto_obra

4. Ejecutar el siguiente comando para generar el .exe:
   pyinstaller --onefile --windowed main_gui.py

   - `--onefile`: genera un solo archivo ejecutable
   - `--windowed`: evita que se abra una consola negra

5. El archivo ejecutable estará en la carpeta `dist\` como:
   dist\main_gui.exe

Este archivo funcionará en cualquier computador con Windows, sin necesidad de instalar Python.
