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
