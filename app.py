from flask import Flask, render_template
from conexoes import carregar_assuntos  # Importa a função do módulo conexoes.py

app = Flask(__name__, template_folder='./templates')

@app.route("/carregar_assunto")
def carregar_assunto():
    assuntos = carregar_assuntos()
    lista_assuntos = [{"numIdAssunto": row[0], "assunto": row[1]} for row in assuntos]
   
    return render_template("assunto.html", assuntos=lista_assuntos)

if __name__ == "__main__":
    app.run(debug=True)
