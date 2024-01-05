from flask import Flask

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return "Welcome Home Buddy"

@app.route('/items/<int:item_id>', methods=['GET'])
def get_items(item_id):
    res = {"itemId":item_id, "description":"This is the item description "}
    return res

@app.route("/additems", methods=['POST'])
def add_items():
    return "Items added"

if __name__ == "__main__":
    app.run(debug=True)

