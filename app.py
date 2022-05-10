from flask import Flask, render_template, abort, request
import os
import json
app = Flask(__name__)

with open("MSX.json") as fichero:
    datos=json.load(fichero)


@app.route('/',methods=["GET","POST"])
def inicio():
	return render_template("inicio.html")


@app.route('/juegos', methods=["GET","POST"])
def juegos():

    if request.method == "GET":
        l_categorias=[]
        for juego in datos:
            l_categorias.append(juego["categoria"])
        return render_template('juegos.html', l_categorias=set(l_categorias))

    else:
        nom_juego=request.form.get("nombre")
        categoria=request.form.get("categorias")

        l_nombres=[]
        l_desarrolladores=[]
        l_identificadores=[]
        l_categorias=[]

        for juego in datos:

            l_categorias.append(juego["categoria"])
            
            if nom_juego == "" and str(juego["categoria"]) == categoria:
                l_desarrolladores.append(juego["desarrollador"])
                l_nombres.append(juego["nombre"])
                l_identificadores.append(juego["id"])
            
            elif str(juego["nombre"]).startswith(nom_juego) and str(juego["categoria"]) == categoria:
                l_desarrolladores.append(juego["desarrollador"])
                l_nombres.append(juego["nombre"])
                l_identificadores.append(juego["id"])
        
        return render_template("juegos.html", nom_juego=nom_juego, l_nombres=l_nombres, l_desarrolladores=l_desarrolladores, l_identificadores=l_identificadores, l_categorias=set(l_categorias))


@app.route('/juego/<int:identificador>')
def juegos_detalles(identificador):
    for juegos in datos:
        if juegos["id"] == identificador:
            return render_template('detallejuegos.html', juego=juegos)
        
    return abort(404)

port=os.environ["PORT"]
app.run('0.0.0.0', int(port), debug=False)
