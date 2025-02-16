from flask import Flask, render_template, request, flash, redirect, url_for

app = Flask(__name__)

app.secret_key = "secretKey"

tasks = []

@app.route("/")
def home():
    return render_template("index.html", tasks = tasks)

@app.route("/add", methods = ["POST"])
def add_task():
    task = request.form.get("task")
    due_date = request.form.get('due_date')
    if task and due_date:
        tasks.append({'task': task, 'completed': False, 'due_date': due_date})
        flash('Task added successfully', 'success')
    return redirect(url_for("home"))

@app.route("/delete/<int:task_id>")
def delete_task(task_id):
    if task_id < len(tasks):
        tasks.pop(task_id)
        flash("task deleted successfully", "danger")

    return redirect(url_for("home"))

@app.route("/complete/<int:task_id>")
def complete_task(task_id):
    if task_id<len(tasks):
        tasks[task_id]["completed"] = True
        flash("task completed successfully", "success")
    return redirect(url_for("home"))

@app.route("/delete_all")
def delete_alltasks():
    tasks.clear()
    flash("tasks deleted successfully", "danger")
    return redirect(url_for("home"))




if __name__ == "__main__":
    app.run(debug = True)


