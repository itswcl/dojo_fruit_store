from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = "zzz"

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/checkout', methods=['POST'])
def checkout():
    session["strawberry"] = int(request.form["strawberry"])
    session["raspberry"] = int(request.form["raspberry"])
    session["apple"] = int(request.form["apple"])
    session["first_name"] = request.form["first_name"]
    session["last_name"] = request.form["last_name"]
    session["student_id"] = request.form["student_id"]

    print(f"Charging {session['first_name']} for {session['strawberry']+session['raspberry']+session['apple']}")
    return redirect("/checkout") # redirect the path

@app.route('/checkout')
def receipt():

    return render_template('checkout.html', # render file
        strawberry=session["strawberry"],
        raspberry=session["raspberry"],
        apple=session["apple"],
        first_name=session["first_name"],
        last_name=session["last_name"],
        student_id=session["student_id"]
    )

@app.route('/fruits')
def fruits():
    return render_template("fruits.html")

if __name__=="__main__":
    app.run(debug=True)