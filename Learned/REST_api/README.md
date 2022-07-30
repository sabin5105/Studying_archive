# RESTfull API test

## json server open
```console
$ mkdir json-server-exam && cd json-server-exam
$ npm init -y
$ npm install json-server --save-dev
```

## Create DB file (which is .json)

## Let json server watch DB
```console
$ json-server --watch db.json --port 5000
```

## above code is bit bothering
* edit script of "package.json"
```js
{
  "name": "json-server-exam",
  "version": "1.0.0",
  "scripts": {
    "start": "json-server --watch db.json"
  },
  "devDependencies": {
    "json-server": "^0.15.0"
  }
}
```

## start npm
```console
$ npm start
```

## Interaction with postman or something else
<img width="600" alt="Screen Shot 2022-07-30 at 9 39 05 PM" src="https://user-images.githubusercontent.com/50198431/181915602-af4f8b6e-0e0f-40d4-8d41-536b0a0a7b23.png">
<img width="600" alt="Screen Shot 2022-07-30 at 10 02 15 PM" src="https://user-images.githubusercontent.com/50198431/181915612-a02195fb-e421-4733-9caa-65a65360949d.png">
<img width="183" alt="Screen Shot 2022-07-30 at 9 45 30 PM" src="https://user-images.githubusercontent.com/50198431/181915613-392cb6eb-5803-4c7c-b4b9-0a64a1b21062.png">
<img width="183" alt="Screen Shot 2022-07-30 at 9 46 40 PM" src="https://user-images.githubusercontent.com/50198431/181915617-ea190eed-df21-49e6-81ef-cd727ff296fe.png">

