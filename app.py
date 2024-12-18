from flask import Flask, request, jsonify
from flask_cors import CORS  
import os

app = Flask(__name__)
CORS(app)  # Add this line to enable CORS for all routes

@app.route('/echo', methods=['GET'])
def echo():
    # Extract the 'text' parameter from the query string
    text = request.args.get('text', default="No text provided")
    
    # Print the text to the console
    print(f"Received text: {text}")
    
    # Return the same text back to the user
    return jsonify({"response": text})

if __name__ == '__main__':
    # Use the PORT environment variable assigned by Heroku
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
