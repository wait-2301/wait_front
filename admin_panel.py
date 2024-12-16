from flask import Flask, jsonify, render_template

app = Flask(__name__)

# Статичный список менеджеров
managers = [
    {"name": "Кумисбек Ариана", "table": "СТОЛ 1", "status": "Доступен"},
    {"name": "Казанбасова Амина", "table": "СТОЛ 2", "status": "Доступен"},
    {"name": "Таукен Аспандияр", "table": "СТОЛ 3", "status": "В процессе"},
    {"name": "Агабай Аида", "table": "СТОЛ 4", "status": "Не доступен"},
    {"name": "Сейпыш Алан", "table": "СТОЛ 5", "status": "Доступен"},
]

@app.route('/')
def index():
    return render_template('admin_panel.html')

@app.route('/managers')
def get_managers():
    return jsonify(managers)

if __name__ == '__main__':
    app.run(debug=True)
