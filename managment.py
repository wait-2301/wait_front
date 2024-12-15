from flask import Flask, jsonify, render_template

app = Flask(__name__)

# Данные для очереди
queue = [
    {"name": "Космухамбетов Ансар", "time": "", "ticket": "B111"},
    {"name": "Ерке Есхан", "time": "00:05", "ticket": ""},
    {"name": "Космухамбетов Ансар", "time": "", "ticket": "B111"},
    {"name": "Ерке Есхан", "time": "00:05", "ticket": ""},
    {"name": "Космухамбетов Ансар", "time": "", "ticket": "B111"},
    {"name": "Ерке Есхан", "time": "00:05", "ticket": ""},
    {"name": "Космухамбетов Ансар", "time": "", "ticket": "B111"},
    {"name": "Ерке Есхан", "time": "00:05", "ticket": ""},
    {"name": "Космухамбетов Ансар", "time": "", "ticket": "B111"},
    {"name": "Ерке Есхан", "time": "00:05", "ticket": ""},
    {"name": "Космухамбетов Ансар", "time": "", "ticket": "B111"},
    {"name": "Ерке Есхан", "time": "00:05", "ticket": ""},
    {"name": "Космухамбетов Ансар", "time": "", "ticket": "B111"},
    {"name": "Ерке Есхан", "time": "00:05", "ticket": ""},
    {"name": "Космухамбетов Ансар", "time": "", "ticket": "B111"},
    {"name": "Ерке Есхан", "time": "00:05", "ticket": ""},
    {"name": "Космухамбетов Ансар", "time": "", "ticket": "B111"},
    {"name": "Ерке Есхан", "time": "00:05", "ticket": ""},
    {"name": "Космухамбетов Ансар", "time": "", "ticket": "B111"},
    {"name": "Ерке Есхан", "time": "00:05", "ticket": ""},
]

@app.route('/')
def index():
    return render_template('managment.html')  # Перенесите ваш HTML в папку templates/index.html

@app.route('/queue', methods=['GET'])
def get_queue():
    return jsonify(queue)

if __name__ == '__main__':
    app.run(debug=True)
