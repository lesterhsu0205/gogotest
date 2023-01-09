import json

def test_hello(app, client):
    res = client.get('/')
    assert res.status_code == 200

def test_create_task(client):
    res = client.post('/task', json={
        "name": "買晚餐"
    })
    print(f'test_create_task response: {res}')
    assert res.status_code == 201
    result = res.json['result']
    assert type(result) == dict
    assert result['name'] == '買晚餐'

def test_list_tasks(client):
    res = client.get('/tasks')
    print(f'test_list_tasks response: {res}')
    assert res.status_code == 200
    assert type(res.json) == dict
    assert type(res.json['result']) == list

def test_update_task(client):
    client.post('/task', json={
        "name": "買特餐"
    })
    res = client.put('/task/2', json={
        "name": "買午餐",
        "status": 1
    })
    print(f'test_update_task response: {res}')
    assert res.status_code == 200
    result = res.json['result']
    assert type(result) == dict
    assert result['name'] == '買午餐'

def test_delete_task(client):
    client.post('/task', json={
        "name": "買特餐"
    })
    res = client.delete('/task/2')
    print(f'test_delete_task response: {res}')
    assert res.status_code == 200
    
