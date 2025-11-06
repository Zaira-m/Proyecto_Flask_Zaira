from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Página principal
@app.route("/")
def index():
    return render_template("index.html")

# Ejercicio 1: Promedio de notas y asistencia
@app.route("/ejercicio1", methods=["GET", "POST"])
def ejercicio1():
    resultado = error = None
    valores = {"nota1": "", "nota2": "", "nota3": "", "asistencia": ""}

    if request.method == "POST":
        try:
            # Tomar valores y los guardar para persistir en la vista
            valores["nota1"] = request.form.get("nota1", "").strip()
            valores["nota2"] = request.form.get("nota2", "").strip()
            valores["nota3"] = request.form.get("nota3", "").strip()
            valores["asistencia"] = request.form.get("asistencia", "").strip()

            # Conversión a float
            n1 = float(valores["nota1"])
            n2 = float(valores["nota2"])
            n3 = float(valores["nota3"])
            asistencia = float(valores["asistencia"])

            # Validaciones de rango
            if not all(10 <= n <= 70 for n in (n1, n2, n3)) or not (0 <= asistencia <= 100):
                error = "Error: las notas deben estar entre 10 y 70, y la asistencia entre 0 y 100."
            else:
                promedio = round((n1 + n2 + n3) / 3, 1)
                estado = "Aprobado" if (promedio >= 40 and asistencia >= 75) else "Reprobado"
                resultado = f"Promedio: {promedio} — Estado: {estado}"

        except ValueError:
            error = "Por favor, ingresa solo números válidos en todos los campos."

    return render_template("ejercicio1.html", resultado=resultado, error=error, valores=valores)

# Ejercicio 2: Nombre más largo
@app.route("/ejercicio2", methods=["GET", "POST"])
def ejercicio2():
    resultado = error = None
    valores = {"nombre1": "", "nombre2": "", "nombre3": ""}

    if request.method == "POST":
        valores["nombre1"] = request.form.get("nombre1", "").strip()
        valores["nombre2"] = request.form.get("nombre2", "").strip()
        valores["nombre3"] = request.form.get("nombre3", "").strip()

        if any(v == "" for v in valores.values()):
            error = "Ingresa los tres nombres."
        else:
            nombres = [valores["nombre1"], valores["nombre2"], valores["nombre3"]]
            nombre_mas_largo = max(nombres, key=len)
            resultado = f"El nombre más largo es '{nombre_mas_largo}' con {len(nombre_mas_largo)} caracteres."

    return render_template("ejercicio2.html", resultado=resultado, error=error, valores=valores)

# Página 4 para cumplir rúbrica de "4 páginas"
@app.route("/acerca")
def acerca():
    return render_template("acerca.html")

if __name__ == "__main__":
    app.run(debug=True)
