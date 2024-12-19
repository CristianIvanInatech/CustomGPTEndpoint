from flask import Flask, request, jsonify
from flask_cors import CORS  
import os

app = Flask(__name__)
CORS(app)  

@app.route('/echo', methods=['GET'])
def echo():
    
    text = request.args.get('text', default="No text provided")
    
    
    try:
        with open('medical_details.txt', 'a', encoding='utf-8') as file:
            file.write(text + '\n')
    except Exception as e:
        print(f"Error writing to file: {e}")
        return jsonify({"error": "Could not save data"}), 500
    

    return jsonify({"response": "Datele au fost verificate"})

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
