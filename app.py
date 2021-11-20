from flask import Flask, request, render_template, redirect

app = Flask(__name__)

@app.get("/")
def index():
    # Render the index.html template and return it 
    return render_template("index.html")

@app.get("/search")
def search():
    args = request.args.get("q")
    return redirect(f"https://google.com/search?q={args}")

if __name__ == "__main__":
    app.run()