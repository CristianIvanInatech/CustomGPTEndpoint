from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/echo', methods=['GET'])
def echo():
    # Extract the 'text' parameter from the query string
    text = request.args.get('text', default="No text provided")
    
    # Print the text to the console
    print(f"Received text: {text}")
    
    # Return the same text back to the user
    return jsonify({"response": text})

if __name__ == '__main__':
    # Run the app on localhost:5000
    app.run(host='0.0.0.0', port=5000, debug=True)
