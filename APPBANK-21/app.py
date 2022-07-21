# importing needed libraries
import pyotp
from flask import *
from flask_bootstrap import Bootstrap

# configuring flask application
app = Flask(__name__)
app.config["SECRET_KEY"] = "APP_SECRET_KEY"
Bootstrap(app)

# Validação de Lógica Passo 3
auth = "tokenvalidado"


# homepage route
@app.route("/")
def index():
    return "LAB BANK 21 - agencia_conta: A001CC001 / password: password / TOKEN : 980002"



# login page route
@app.route("/dados/")
def dados():
    return render_template("dados.html")

@app.route("/saldo/")
def saldo():
    return render_template("saldo.html")

@app.route("/senhatransacional/")
def senhatransacional():
    return render_template("senhatransacional.html")

@app.route("/transfer/")
def transfer():
    try:
       validapasso3=request.args['auth']
    except:
       return redirect(url_for("dados"))
    if validapasso3 == auth:
        return render_template("transfer.html")
    else:
        return redirect(url_for("dados"))
       
# Fase 1
@app.route("/dados/", methods=["POST"])
def dados_form():
    # demo creds
    creds = {"username": "A001CC001", "password": "password"}

    # getting form data
    username = request.form.get("username")
    password = request.form.get("password")

    # authenticating submitted creds with demo creds
    # redirecting users to 2FA page when creds are valid
    if username == creds["username"] and password == creds["password"]:
        return redirect(url_for("saldo"))
    else:
        # inform users if creds are invalid
        flash("Agencia e Conta ou Senha Errada", "Falha de Acesso")
        return redirect(url_for("dados"))

#Fase2
@app.route("/saldo/", methods=["POST"])
def saldo_form():
    # demo creds
    creds = {"username": "3", "password": "1"}

    # getting form data
    username = request.form.get("username")

    # authenticating submitted creds with demo creds
    # redirecting users to 2FA page when creds are valid
    if username == creds["username"] :
        return redirect(url_for("senhatransacional"))
    else:
        flash("Encerrando o processo", "dados")
        return redirect(url_for("dados"))

#Fase3
@app.route("/senhatransacional/", methods=["POST"])
def senhatransacional_form():
    # demo creds
    creds = {"username": "980002", "password": "1"}

    # Validação do Token
    username = request.form.get("username")

    if username == creds["username"] :
        #Erro de Lógica
        #return redirect(url_for("transfer"))
        #Correção
        return redirect(url_for("transfer", auth="tokenvalidado"))
    else:
        flash("Token Invalido, Processo reincializado", "dados")
        return redirect(url_for("dados"))

# running flask server
if __name__ == "__main__":
    app.run(debug=True)
