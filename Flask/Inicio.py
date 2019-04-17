from flask import Flask,jsonify,render_template
app=Flask(__name__)

@app.route("/json")
def conJason():
	return jsonify({"saludo":"hola mundo"})
	
@app.route("/",methods=["GET"])
def index():
	items=[{'nombre':'carlos','edad':'36'},{'nombre':'Cote','edad':'32'}]
	return render_template("index.html",name="Ejemplo",items=items)

if __name__=='__main__':
	app.run(debug=True)