from flask import Flask, render_template

app = Flask(__name__)

#Ruta - 1 
@app.route( '/', methods=['GET'] )
def ajedrez():
    return render_template("index.html", num = 8, col = 8, color_1="red", color_2="black")

#Ruta - 2 
@app.route( '/<int:x>/', methods=['GET'] )
def ajedrezConFilas(x):
    return render_template("index.html", num = x, col = x, color_1="red", color_2="black")

#Ruta - 3 
@app.route( '/<int:x>/<int:y>/', methods=['GET'] )
def ajedrezConFilasYColumnas(x,y):
    return render_template("index.html", num = x, col = y, color_1="red", color_2="black")

#Ruta -  
@app.route( '/<int:x>/<int:y>/<string:col_0>/<string:col_1>/', methods=['GET'] )
def ajedrezConFilasYColumnasYColor(x,y,col_0,col_1):
    return render_template("index.html", num = x, col = y, color_1=col_0, color_2=col_1)


#App.run
if __name__ == "__main__":
    app.run(debug=True)