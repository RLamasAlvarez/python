from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        numero_local = request.form["numero_local"]
        nombre_local = request.form["nombre_local"]
        unidad_negocio = request.form["unidad_negocio"]
        mensaje = f"Número de Local: {numero_local}\nNombre del Local: {nombre_local}\nUnidad de Negocio: {unidad_negocio}"
        return render_template("ejemplo.html", mensaje=mensaje)
    return render_template("ejemplo.html")

if __name__ == "__main__":
    app.run(debug=True)
