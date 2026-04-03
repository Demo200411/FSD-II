from flask import Flask, request, jsonify

app = Flask(__name__)

orders = {
    101: {"status": "Pending"},
    102: {"status": "Shipped"},
    103: {"status": "Delivered"}
}

@app.route('/orders/<int:order_id>', methods=['PUT'])
def update_order_status(order_id):
    if order_id not in orders:
        return jsonify({"error": "Order not found"}), 404

    data = request.get_json()
    new_status = data.get("status")

    if not new_status:
        return jsonify({"error": "Status required"}), 400

    orders[order_id]["status"] = new_status

    return jsonify({
        "order_id": order_id,
        "new_status": new_status
    })

if __name__ == '__main__':
    app.run(port=5002, debug=True)
