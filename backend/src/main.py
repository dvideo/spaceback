# coding=utf-8

from flask import Flask, jsonify, request, render_template, redirect, url_for
from flask_cors import CORS

# from flask_bootstrap import Bootstrap

from database import Database
from vehicle_registration_service import register_vehicle

app = Flask(__name__)

CORS(app) # Please do not do this in production :)
# Bootstrap(app)


database = Database()


@app.route('/success/add')
def success():
  return render_template('success.html', data=database.list())

# @app.route('/success/del')
# def successDel():
#   return render_template('successDel.html', data=database.list())


@app.route('/vehicles')
def get_vehicles():
  # TODO
  return render_template('addVehicles.html', data=database.list())


@app.route('/vehicles', methods=['POST'])
def create_vehicle():
  # TODO
  carType = str(request.form['carType'])
  name = str(request.form['name'])
  mile = int(request.form['mile'])
  wheel = int(request.form['wheel'])
  door = int(request.form['door'])
  estat = str(request.form['estat'])
  seat = str(request.form['seat'])
  rate = 'High'
  slide1=slide2=slide3=slide4=''
  if carType.lower()=='minivan':
    slide1 = request.form['slide1']
    slide2 = request.form['slide2']
    slide3 = request.form['slide3']
    slide4 = request.form['slide4']
  if(mile<10000):
    rate = 'Low'
  elif(mile>=10000 and mile<100000):
    rate = 'Medium'
  dbAdd = {'carType':carType,
            'name': name,
            'mile': mile,
            'rate':rate,
            'wheel': wheel,
            'estat':estat}
  if(carType.lower()=='minivan'):
    dbAdd.update({'slide1':slide1,
                  'slide2':slide2,
                  'slide3':slide3,
                  'slide4':slide4,
                  'door':door})
  elif(carType.lower()=='motorcycle'):
    dbAdd.update({'seat':seat})
  else:
    dbAdd.update({'door':door})
  # check for duplicates? might not matter since id is unique
  register_vehicle(database.create(dbAdd))
  return redirect(url_for('success'))

@app.route('/vehicles/<id>')
def get_vehicle(id):
  # TODO
  print('here is my id: ',id)
  print(database.find(int(id)))
  return jsonify(database.find(int(id)))

@app.route('/vehicles/<id>', methods=['PATCH'])
def update_vehicle(id):
  # TODO
  print(id)
  # print(request.form)
  # return jsonify(id + "" + request.form)
  return render_template('addVehicles.html', data=database.list())

@app.route('/vehicles/<id>', methods=['DELETE'])
def delete_vehicle(id):
  # TODO
  database.destroy(int(id))
  return jsonify({})
  # return render_template('successDel.html', data=database.list())
