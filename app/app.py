from flask import Flask
app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return "DevSecOps Pipeline - Running! 🚀"

@app.route('/health', methods=['GET'])
def health():
    return "OK", 200

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)
