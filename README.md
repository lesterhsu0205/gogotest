# GOGOLOOK test application

## Project structure

```
.
├── README.md
├── app
│   ├── Dockerfile
│   ├── app.py
│   ├── model
│   │   ├── record.py
│   │   └── result.py
│   └── requirements.txt
├── compose.yaml
├── gogolook_test.postman_collection.json
├── tests
│   ├── conftest.py
│   └── test_api.py
└── venv
```

## Deploy with docker compose

```bash
$ docker compose up --build --force-recreate -d
```

## Expected result

Listing containers must show one container running and the port mapping as below:

```bash
$ docker compose ps
NAME                COMMAND             SERVICE             STATUS              PORTS
gogotest-web-1      "python3 app.py"    web                 running             0.0.0.0:8000->8000/tcp
```

After the application starts, navigate to `http://localhost:8000` in your web browser or run:

```bash
$ curl localhost:8000
Hello World!
```

Stop and remove the containers

```bash
$ docker compose down
```

## Unit Test
```bash
$ cd gogotest
$ python3 -m venv venv
$ . venv/bin/activate
$ pip3 install pytest
$ pytest
```
