var express = require('express');

var app = express();

app.get("/search", function (req, res) {
    const { spawn } = require('child_process');
    console.log("starting file");
    const pyProg = spawn('python', ['./../main.py']);
    console.log("started");
    pyProg.stdout.on('data', function(data) {
        console.log(data.toString());
        res.write(data);
        res.end('end');
    });

});

var server = app.listen(8081, function () {
    var host = server.address().host;
    var port = server.address().port;
    console.log("Server is running on %s %s", host, port);
})