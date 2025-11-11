from flask import Flask, render_template, request
from pymongo import MongoClient
import os

app = Flask(__name__)

# Load credentials from environment variables
MONGO_USER = os.getenv("MONGO_USER", "admin")
MONGO_PASS = os.getenv("MONGO_PASS", "admin1234")
MONGO_HOST = os.getenv("MONGO_HOST", "mongo_new")
MONGO_PORT = os.getenv("MONGO_PORT", "27017")

uri = f"mongodb://{MONGO_USER}:{MONGO_PASS}@{MONGO_HOST}:{MONGO_PORT}"
client = MongoClient(uri)

db = client.user_db          # Database
user_db_collection = db.user_data  # Collection

def fill_form(username, description):
    user_data = {'name': username, 'desc': description}
    result = user_db_collection.insert_one(user_data)
    print(f'Task inserted with id: {result.inserted_id}')

def read_data():
    res = user_db_collection.find()
    print('This is the data present:')
    for docs in res:
        print(f'{docs["name"]}: {docs["desc"]}')

@app.route('/')
def home():
    return render_template('login.html')

@app.route("/submit", methods=['POST'])
def submit():
    username = request.form.get('username')
    password = request.form.get('password')
    description = request.form.get('description')

    fill_form(username, description)
    read_data()

    valid_user = {
        'Kaustav': '812004',
        'Gaurav': '2580',
        'Vishesh': '6392'
    }

    if username in valid_user and password == valid_user[username]:
        return render_template('Welcome.html', name=username)
    else:
        return render_template('login.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
