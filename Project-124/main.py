import re
from flask import Flask, jsonify, request

# creating object of the flask
app = Flask(__name__)
Contacts = [
    {
        'id': 1,
        'Name': 'pqr',
        'Number': '2388428349',
        'Call Status': True
    },
    {
        'id': 2,
        'Name': 'abc',
        'Number': '1234567890',
        'Call Status': True
    }]


@app.route('/addcontact', methods=['POST'])
def addContact():
    if not request.json:
        return jsonify({
            'status': 'Error',
            'message': 'Please Provide the following data.'
        })
    contact = {
        'id': Contacts[-1]['id'] + 1,
        'Name': request.json['Name'],
        'Number': request.json['Number'],
        'Call Status': False
    }
    Contacts.append(contact)
    return jsonify({
        'status': 'successful',
        'message': 'Data added Successfully'
    })


@app.route('/get-contacts')
def getContacts():
    return jsonify({
        'data': Contacts
    })


if(__name__ == '__main__'):
    app.run(debug=True)
