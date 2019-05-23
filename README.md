# Tellus

# Backend

Backend is maintained in the `api` folder. The following commands must be ran in the `api` folder.

## Installation

To run the backend using the Dockerfile run the command:

```
docker build -t tellus_pg .
docker run --rm -P --name tellus_dev tellus_pg
```

To install the Python enviroment:

```
pipenv install
```

## Running the server

To run the api run the command:

```
pipenv shell # Activates the pip enviroment
python server.py
```

# Frontend

## Installation

## Running the server

To run the Frontend run the following command in the `tellus_frontend` folder:

```
yarn run dev
```
