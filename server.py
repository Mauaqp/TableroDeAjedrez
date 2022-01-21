from flask import Flask, render_template

app = Flask(__name__)

#Ruta - 1 
@app.route( '/', methods=['GET'] )
def ajedrez():
    return render_template("index.html", num = 8, color_0="red", color_1="black")

#App.run
if __name__ == "__main__":
    app.run(debug=True)