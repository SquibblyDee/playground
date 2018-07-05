from flask import Flask, render_template

app = Flask(__name__)

# number=0 is being used as our default return
@app.route('/play')
def play():
    return render_template("play.html", number=0)

@app.route('/play/<number>')
def playPlusNum(number):
    intNumber = int(number)
    return render_template("play.html", number=intNumber)

@app.route('/play/<number>/<color>')
def playPlusNumPlusCol(number, color):
    intNumber = int(number)
    strColor = str(color)
    return render_template("play.html", number=intNumber, blockColor=strColor)

if __name__ =="__main__":
    app.run(debug=True)
