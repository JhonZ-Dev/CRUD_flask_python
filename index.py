from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__)

# Lista de tareas (simulada en memoria)
tasks = []

