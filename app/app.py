import json
import jsonpickle
from flask import Flask, Response, request, abort
from model.result import Result
from model.record import Record

app = Flask(__name__)

records = []
record_idx = 1

@app.route('/')
def hello():
    return 'Hello World!'

@app.route('/tasks', methods=['GET'])
def list_tasks():
    return gen_response(200, Result(records))

@app.route('/task', methods=['POST'])
def create_task():

    data = request.json

    if type(data) is not str:
        global record_idx
        record_idx = record_idx + 1
        new_record = Record(record_idx, data.get('name'), 0)
        records.append(new_record)
        return gen_response(201, Result(new_record))
    else:
        abort(400, description="Fail to decode attritube: 'name'")


@app.route('/task/<int:id>', methods=['PUT'])
def update_task(id):

    record = find_record(id)

    if record is not None:
        data = request.json
        record.name = data.get('name')
        record.status = data.get('status')
        return gen_response(200, Result(record))
    else:
        abort(404, description=f'Resource not found by id: {id}')


@app.route('/task/<int:id>', methods=['DELETE'])
def delete_task(id):

    record = find_record(id)

    if record is not None:
        result = record
        records.remove(record)
        return gen_response(200, None)
    else:
        abort(404, description=f'Resource not found by id: {id}')


@app.errorhandler(400)
def bad_request(error):
    return gen_response(400, Result(error.description))


@app.errorhandler(404)
def resource_not_found(error):
    return gen_response(404, Result(error.description))


@app.errorhandler(Exception)
def handle_exception(error):
    return Response(error.args, status=500, mimetype='application/json')


def gen_response(status_code, result):
    if result is None:
        return Response(status=status_code, mimetype='application/json')
    return Response(jsonpickle.encode(result, unpicklable=False), status=status_code, mimetype='application/json')


def find_record(id):
    return next((record for record in records if record.id == id), None)


if __name__ == '__main__':
    records.clear()
    records.append(Record(record_idx, '買早餐', 0))
    app.run(host='0.0.0.0', port=8000, debug=True)
