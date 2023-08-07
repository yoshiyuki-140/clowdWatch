
from flask import Flask,jsonify
from flask_cors import CORS
from apps import PeopleNumberChecker

app = Flask(__name__)
CORS(app)

@app.route('/')
def main():
    # ここに画像処理と分岐をする
    # 状態判定Flask

    # status == 2 -> busy
    # status == 1 -> soso
    # status == 0 -> empty
    filePath = "C:/Users/moyas/Documents/programsForMe/apps/clowdWatch/html/index.html"
    with open(filePath,encoding='UTF-8') as f:
        return f.read()
    
@app.route('/api/current_people_count',methods=['GET'])
def current_people_count():
    count = PeopleNumberChecker.get_current_people()
    return jsonify({'count':count})

if __name__ == "__main__":
    app.run(debug=True)