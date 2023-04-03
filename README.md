# productsistem

Project carried out with the aim of presenting a simple project to register products, customers and sales for an evaluation event.

A local API was developed with the aim of providing a database for accessing and consuming the application. Therefore, it will be necessary to open 2 terminals to run the api and another for the project developed with VUE.js

## Run Api

To run the Api work, you will need to install python and flask ( pip install flask ) and flask cors (pip install flask-cors). Then,
go to the Api folder and run the command:

```
python app.py
```

The api will be running on port: http://localhost:5000
After the api is up and running, open a second terminal to run the project. Go to the principal project folder and follow the next step:

## Project setup

```
npm install
```

### Compiles and hot-reloads for development

```
npm run serve
```

### Compiles and minifies for production

```
npm run build
```

### Run your unit tests

```
npm run test:unit
```

### Lints and fixes files

```
npm run lint
```