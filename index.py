from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__)

# Lista de tareas (simulada en memoria)
tasks = []

@app.route('/')
def index():
    return render_template('index.html', tasks=tasks)

