import sys
import os
import glob
from markitdown import MarkItDown

md = MarkItDown()

# CASO 1: Individual
if len(sys.argv) > 1:
    pdf_objetivo = sys.argv[1]
    if not os.path.exists(pdf_objetivo):
        print(f"Error: El archivo {pdf_objetivo} no existe.")
        sys.exit(1)
    nombre_salida = os.path.splitext(pdf_objetivo)[0] + ".md"
    print(f"Modo individual: Procesando {pdf_objetivo}...")
    try:
        res = md.convert(pdf_objetivo)
        with open(nombre_salida, "w", encoding="utf-8-sig", errors="replace") as f:
            f.write(res.text_content)
        print(f"Exito! Guardado en: {nombre_salida}")
    except Exception as e:
        print(f"Ocurrio un error: {e}")

# CASO 2: Masivo
else:
    archivos_pdf = glob.glob("*.pdf")
    total_archivos = len(archivos_pdf)
    if total_archivos == 0:
        print("Error: No se encontro ningun archivo .pdf en esta carpeta.")
        sys.exit(1)
    print(f"Modo masivo: Se encontraron {total_archivos} archivos PDF!")
    print("-" * 60)
    for contador, pdf_objetivo in enumerate(archivos_pdf, 1):
        nombre_salida = os.path.splitext(pdf_objetivo)[0] + ".md"
        print(f"[{contador}/{total_archivos}] Convirtiendo: {pdf_objetivo}...")
        try:
            res = md.convert(pdf_objetivo)
            with open(nombre_salida, "w", encoding="utf-8-sig", errors="replace") as f:
                f.write(res.text_content)
            print(f"    Guardado con exito: {nombre_salida}\n")
        except Exception as e:
            print(f"    Error en este archivo: {e}\n")
    print("-" * 60)
    print("Proceso masivo completado con exito!")
