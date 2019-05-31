from flask import Flask, render_template, request, jsonify
from google.appengine.ext import ndb
import logging
import json


log = logging.getLogger(__name__)
app = Flask(__name__)
app.config['DEBUG'] = True


class Details(ndb.Model):
    first_name = ndb.StringProperty()
    last_name = ndb.StringProperty()
    age = ndb.IntegerProperty()
    phone = ndb.StringProperty()


@app.route('/')
def get_name():
    return render_template('index.html')


@app.route('/add')
def enter_details():
    return render_template('form.html')


@app.route('/get_details', methods=['POST', 'GET'])
def querykey():
    f_name = request.form.get('fname')
    l_name = request.form.get('lname')
    age = int(request.form.get('age'))
    ph = request.form.get('ph')
    detail = Details(first_name=f_name, last_name=l_name, age=age, phone=ph)
    detail.put()
    return render_template('index.html')


@app.route('/display', methods=['GET'])
def display_result():
    list_of_details = Details.query().fetch()
    details = [
        {
          'age': detail.age,
          'first_name': detail.first_name,
          'last_name': detail.last_name,
          'phone': detail.phone,
          'id': detail.key.id()
        }
        for detail in list_of_details
    ]

    # Can also write return statement as
    # return jsonify({
    #    'success': True,
    #    'details': details
    # })

    return json.dumps({
       'success': True,
       'details': details
    }), 200, {'Content-Type': 'application/json'}


@app.route('/result', methods=['POST'])
def filter_result():

    age = str()
    age1 = age.split(',')
    val1 = int(age1[0])
    val2 = int(age1[1])

    details_list = Details.query(ndb.AND(Details.age >= val1,
                                         Details.age < val2))

    return details_list













