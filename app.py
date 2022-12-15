from flask import Flask, render_template, request, jsonify
from pymongo import MongoClient
import certifi
ca = certifi.where()

client = MongoClient("mongodb://sparta:sparta@ac-wqtlhrl-shard-00-00.7frjr12.mongodb.net:27017,ac-wqtlhrl-shard-00-01.7frjr12.mongodb.net:27017,ac-wqtlhrl-shard-00-02.7frjr12.mongodb.net:27017/?ssl=true&replicaSet=atlas-hiv7s7-shard-0&authSource=admin&retryWrites=true&w=majority", tlsCAFile=ca)

db = client.dbSparta
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route("/homework", methods=["POST"])
def homework_post():
    name_receive = request.form['name_give']
    comment_receive = request.form['comment_give']
    doc = {
        'name':name_receive,
        'comment':comment_receive
    }
    db.pesanfans.insert_one(doc)
    return jsonify({'msg':'pesan tersimpan!'})

@app.route("/homework", methods=["GET"])
def homework_get():
    massage_list = list(db.pesanfans.find({},{'_id':False}))
    return jsonify({'massages':massage_list})

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)