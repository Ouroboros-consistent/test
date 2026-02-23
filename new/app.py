from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    binary_result = None
    
    if request.method == "POST":
        decimal_number = request.form["decimal"]
        
        if decimal_number.isdigit():
            binary_result = bin(int(decimal_number))[2:]
        else:
            binary_result = "Input harus berupa angka positif"

    return render_template("index.html", result=binary_result)

if __name__ == "__main__":
    app.run(debug=True)