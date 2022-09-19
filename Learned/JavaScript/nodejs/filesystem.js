var http = require('http');
var fs = require('fs'); // acronyme for file system

http.createServer(function (req, res) {
  fs.readFile('demofile1.html', function(err, data) {
    res.writeHead(200, {'Content-Type': 'text/html'});
    res.write(data);
    return res.end();
  });
}).listen(8080);


```
fs.readFile()
fs.appendFile()
fs.open()
fs.writeFile()
fs.unlink()
fs.rename()

ex1)
fs.appendFile('mynewfile1.txt', ' This is my text.', function (err) {
    if (err) throw err;
    console.log('Updated!');
  });
```