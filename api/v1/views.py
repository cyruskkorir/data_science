import json
import os
from flask import Flask, request, jsonify, render_template
from flask_pymongo import PyMongo
from dotenv import load_dotenv
import pandas as pd

app = Flask(__name__)

# check and load env variables
load_dotenv()

app.config["MONGO_URI"] = os.getenv('MONGO_URI')
mongodb_client = PyMongo(app)
db = mongodb_client.db

@app.route('/', methods=['GET'])
def index():
    return jsonify({
        'message': 'Welcome to Jacaranda Health api'
    })

@app.route('/save-ticket', methods=['POST'])
def save_ticket():
    df = pd.read_csv('Assignment.csv')
    data_dict = df.to_dict(orient="records")
    db.tickets.insert_many(data_dict)
    return jsonify(message="successfully saved")

# // fetch all records
@app.route('/fetch-ticket', methods=['GET'])
def get_tickets():
    tickets = db.tickets.find()
    result = [ticket for ticket in tickets]
    return jsonify(result)

# // fetch a single record by id
@app.route('/fetch-ticket<int:recordId>', methods=['GET'])
def get_one_ticket(recordId):
    ticket = db.tickets.find_one({'_id': recordId})
    return ticket


@app.route('/update-ticket<int:recordId>', methods=['PUT'])
def update_db(recordId):
    updated_ticket = db.tickets.find_one_and_update(
        {'_id': recordId}, {'$set': 
            [
                {'ticket_id': 'ticket_id'},
                {'intents': 'intents'},
                {'subject', 'subject'},
                {'phone': 'phone'},
                {'incoming_messages': 'incoming_messages'},
                {'outgoing_messages': 'outgoing_messages'}
            ]
        }
    )
    return updated_ticket
    
