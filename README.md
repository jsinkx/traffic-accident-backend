<div align="center">

# Traffic accident backend ML app

Create traffic accident forecast wia weather conditions in Moscow at north

</div>

---

## Documentation

[Simple markdown documentation](./documentation.md)

## Stack

-  Flask
-  joblib

## Configuration

An example of the config is in `.env.example`, but to use it you need to use `.env`

The integration of the config from env into python variables is in `./shared/config.py `

Before using it, it is necessary to load the `.pkl` of trained models in `./models` and register them in `./models.json`.

You can get models in the [traffic-accident-ml](https://github.com/jsinkx/traffic-accident-ml) repository or download from [Google Drive](https://drive.google.com/drive/folders/1tYOwK5FFDQ4p6IUQ2HQIEzmWDxz7muh3?usp=sharing)

## Production mode

### By docker

Way without create `.env`

```sh
docker build -t traffic-accident-backend-ml --build-arg SERVER_HOST=<SERVER_HOST> --build-arg SERVER_PORT=<SERVER_PORT> --build-arg IS_PROD=<IS_PROD> .
```

<strong> Warning: don't forget to create `.env` and add pkl models </strong>

```sh
docker build -t traffic-accident-backend-ml .
```

Run build container

```sh
docker run --name traffic-accident-backend-ml --restart=always -d -p 5000:5000 traffic-accident-backend-ml
```

## Dev mode & installation

1. [`> Python 3.10`](https://www.python.org/)
2. Install all libs from [`requirements.txt`](./requirements.txt)

Install all dependencies

```sh
cd traffic-accident-backend-ml
pip install --no-cache-dir -r requirements.txt
```

Run `python3 -m flask run --host=0.0.0.0`
