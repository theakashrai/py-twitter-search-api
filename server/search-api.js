var express = require('express');

var app = express();

let runPy = new Promise(function(success, nosuccess) {

    const { spawn } = require('child_process');
    const pyprog = spawn('python', ['./../main.py']);

    pyprog.stdout.on('data', function(data) {
        success(data);
    });

    pyprog.stderr.on('data', (data) => {
        nosuccess(data);
    });
});


app.get("/search", function (req, res) {
    res.write('welcome\n');
    runPy.then(function(fromRunpy) {
        console.log(fromRunpy.toString());
        res.end(fromRunpy);
    }).catch(err => {
        console.error(err);
      })
      .then(ok => {
        console.log(ok.message)
      });
});

var server = app.listen(8081, function () {
    var host = server.address().host;
    var port = server.address().port;
    console.log("Server is running on %s %s", host, port);
})