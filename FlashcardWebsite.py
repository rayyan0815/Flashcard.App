from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Store cards in memory (resets when you restart)
cards = []

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/add_card', methods=['POST'])
def add_card():
    data = request.json

    question = data.get(question)
    answer = data.get(answer)
    if question and answer:
        cards.append({"question": question, "answer": answer})

        return jsonify({"success": True, "total": len (cards)})
    return jsonify({"success": False})

@app.route('/remove_card', methods=['Post'])
def remove_card():

    data = request.json
    index = data.get('index')
    if 0 <= index < len(cards):
        removed = cards.pop(index)
        return jsonify({"success": True, "removed": removed})
    return jsonify({"success": False})

if __name__ == '__main__':
    app.run(debug=True)
