import re
import shutil
from pathlib import Path

CARPETA_ORIGEN = Path.home() / "Downloads"
CARPETA_DESTINO = Path.home() / "Documents" / "Examens Accés Grau Superior Catalunya"

CARPETAS = {
    "angles": "01 Anglès",
    "ingles": "01 Anglès",
    "english": "01 Anglès",
    "matematiques": "02 Matemàtiques",
    "matematicas": "02 Matemàtiques",
    "matematica": "02 Matemàtiques",
    "mates": "02 Matemàtiques",
    "catala": "03 Llengua catalana",
    "catalan": "03 Llengua catalana",
    "castella": "04 Llengua castellana",
    "castellano": "04 Llengua castellana",
    "geografia": "05 Geografia",
    "historia": "05 Geografia",
    "psicologia": "06 Psicologia i sociologia",
    "sociologia": "06 Psicologia i sociologia",
}

def normalizar(texto):
    texto = texto.lower()
    reemplazos = {
        "á": "a", "à": "a", "é": "e", "è": "e", "í": "i",
        "ó": "o", "ò": "o", "ú": "u", "ü": "u", "ç": "c", "ñ": "n"
    }
    for original, nuevo in reemplazos.items():
        texto = texto.replace(original, nuevo)
    return texto

def destino_para(nombre_archivo):
    # Separa el nombre en palabras completas: "matematiques-triangles_2023" -> {"matematiques", "triangles", "2023"}
    palabras = set(re.split(r"[^a-z0-9]+", normalizar(Path(nombre_archivo).stem)))

    # Psicologia/sociologia primero, para no confundirla con otras materias
    if palabras & {"psicologia", "sociologia"}:
        return CARPETAS["psicologia"]

    for clave, carpeta in CARPETAS.items():
        if clave in palabras:
            return carpeta

    return None

def organizar():
    CARPETA_DESTINO.mkdir(parents=True, exist_ok=True)

    for carpeta in CARPETAS.values():
        (CARPETA_DESTINO / carpeta).mkdir(exist_ok=True)

    movidos = 0
    no_identificados = []

    for archivo in CARPETA_ORIGEN.iterdir():
        if not archivo.is_file():
            continue

        if archivo.suffix.lower() not in [".pdf", ".doc", ".docx"]:
            continue

        carpeta = destino_para(archivo.name)

        if carpeta is None:
            no_identificados.append(archivo.name)
            continue

        destino = CARPETA_DESTINO / carpeta / archivo.name

        # Si ya existe, añade un número al final
        contador = 1
        while destino.exists():
            destino = CARPETA_DESTINO / carpeta / f"{archivo.stem}_{contador}{archivo.suffix}"
            contador += 1

        shutil.move(str(archivo), str(destino))
        movidos += 1
        print(f"Movido: {archivo.name} -> {carpeta}")

    print(f"\nTotal de archivos movidos: {movidos}")

    if no_identificados:
        print("\nArchivos que no se han podido identificar:")
        for nombre in no_identificados:
            print(f"- {nombre}")

if __name__ == "__main__":
    organizar()
