from tasks import get_stock_price
from flask import jsonify, request
from flask.app import Flask

app = Flask(__name__)

@app.route("/stock_price", methods=["POST"])
def get_stock():
    data = request.get_json()
    stock_name = data.get('stock_name')

    if not stock_name:
        return jsonify({"error": "Nome da ação necessaria"})

    get_stock_price.delay(stock_name)

    return jsonify({"message": "Requisição processada com sucesso!"})

if __name__ == "__main__":
    app.run(debug=True)
