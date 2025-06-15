
import json
import random
import textwrap
import shutil

# -------------- Utilidades --------------

def cargar_preguntas(nombre_archivo: str):
    with open(nombre_archivo, "r", encoding="utf-8") as f:
        return json.load(f)

def ancho_terminal(default: int = 100) -> int:
    """
    Devuelve el ancho actual de la terminal para envolver texto.
    """
    try:
        return shutil.get_terminal_size().columns
    except Exception:
        return default

# -------------- Presentación --------------

def mostrar_explicacion(exp: dict):
    print("\nℹ️  Explicación detallada")
    print(f"   🎯 Concepto clave: {exp.get('concepto', '')}")
    print(f"   ✅ Por qué es correcta: {exp.get('porque_correcta', '')}")

    # Errores de las demás
    print("   ❌ Por qué las otras son erróneas:")
    for letra, razon in exp.get("porque_erroneas", {}).items():
        texto = textwrap.fill(f"{letra}) {razon}",
                              width=ancho_terminal(),
                              subsequent_indent=" " * 6)
        print(f"      {texto}")

    print(f"   🔎 Resumen: {exp.get('resumen', '')}\n")

# -------------- Lógica del examen --------------

def hacer_examen(preguntas):
    aciertos = 0
    falladas = []

    for idx, p in enumerate(preguntas, 1):
        # Título de pregunta
        print(f"\n📖  Pregunta {idx}: {p['pregunta']}")

        # Opciones
        for letra, opcion in p["opciones"].items():
            print(f"   {letra}. {opcion}")

        # Respuesta del usuario
        try:
            respuesta = input("✏️  Tu respuesta: ").strip().lower()
        except UnicodeDecodeError:
            print("⚠️  Error de codificación. Intenta otra vez.")
            respuesta = input("✏️  Tu respuesta (sin caracteres raros): ").strip().lower()

        correcta = p["respuesta"].lower()

        # Evaluación
        if respuesta == correcta:
            print("🎉  ¡Correcto!")
            aciertos += 1
        else:
            print(f"❌  Incorrecto. La respuesta correcta es «{correcta}»")
            falladas.append(p)

        # Explicación siempre
        if "explicacion" in p:
            mostrar_explicacion(p["explicacion"])
        else:
            print("(Sin explicación disponible)")

        print(f"📈  Progreso: {aciertos}/{idx} acertadas")

    return aciertos, falladas

# -------------- Programa principal --------------

def main():
    archivo = "preguntas.json"
    preguntas = cargar_preguntas(archivo)
    total = len(preguntas)

    try:
        num = int(input(f"¿Cuántas preguntas quieres responder? (máx {total}): "))
        if num < 1 or num > total:
            print("🔢 Número fuera de rango. Se usarán todas las preguntas.")
            num = total
    except ValueError:
        print("🔢 Entrada inválida. Se usarán todas las preguntas.")
        num = total

    # Mezclar preguntas
    random.shuffle(preguntas)
    seleccionadas = preguntas[:num]

    print("\n🚀  Comienza el examen interactivo")
    aciertos, falladas = hacer_examen(seleccionadas)

    # Resultados finales
    print("\n🏁  Resultados finales")
    print(f"   🏆  Aciertos: {aciertos}")
    print(f"   ❌  Fallos: {len(falladas)}")
    porcentaje = (aciertos / num) * 100
    nota10 = round(porcentaje / 10, 2)
    print(f"   📊  Nota: {porcentaje:.1f}%  —  {nota10}/10")

    # Repetición de falladas
    if falladas:
        repetir = input("🔁  ¿Repetir solo las falladas? (s/n): ").strip().lower()
        if repetir == "s":
            print("\n🔄  Examen de recuperación:")
            hacer_examen(falladas)

if __name__ == "__main__":
    main()
