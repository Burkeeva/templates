from flask import Flask, jsonify, render_template
import pandas as pd

app = Flask(__name__)

def get_data():
    # Чтение данных из Excel и преобразование в JSON
    df = pd.read_excel('data.xlsx')
    return df.to_dict(orient='records')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/data')
def data():
    data = get_data()
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
