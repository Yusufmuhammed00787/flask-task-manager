
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

tasks = []

@app.route("/")
def home():
    return render_template("index.html", tasks=tasks)

@app.route("/add", methods=["POST"])
def add_task():
    task = request.form.get("task", "").strip()

    if task:
        tasks.append({"name": task, "done": False})

    return redirect(url_for("home"))

@app.route("/complete/<int:task_id>", methods=["POST"])
def complete_task(task_id):
    if 0 <= task_id < len(tasks):
        tasks[task_id]["done"] = True

    return redirect(url_for("home"))

if __name__ == "__main__":
    app.run(debug=True, port=5000)
