const http = require('http');
const https = require('https');
const fs = require('fs');

const DEBUG = true;

const WEBSITE = 'www.surviv.io';

let server = http.createServer((req, res) => {
    if (DEBUG)
        console.log("REQ: " + req.url);

    switch(req.method){
        case 'GET':
            switch (req.url) {
                case '/js/app.8c9b4367.js':
                    console.log("JAVA SCRIPT");
                    fs.createReadStream('app.js').pipe(res);
                    break;
                default:
                    var headers = req.headers;
                    headers.host = 'surviv.io';
                    headers.referer = "https://surviv.io/";
                    headers['accept-encoding'] = "";
                    makeHttpsRequest(WEBSITE, req.url, headers, (data) => {
                        res.write(data);
                        res.end();
                    });
                    break;
            }
            break;
        case 'POST':
            let buffers = [];

            req.on('data', (data)=>{
                buffers.push(data);
            });

            req.on('end', () => {
                var headers = req.headers;
                headers.host = 'surviv.io';
                headers.referer = "https://surviv.io/";
                headers['accept-encoding'] = "";

                makePOSTRequest(WEBSITE, req.url, headers, Buffer.concat(buffers).toString('utf8'), (data, headers)=>{
                    res.writeHead(200, headers);
                    res.write(data);
                    res.end();
                });
            });

            break;
    }

});

server.listen(1111, () => {
    console.log("Listening on 1111");
});

function makeHttpsRequest(host, path, headers = {}, cb) {
    let req = https.request({
        hostname: host,
        path: path,
        headers: headers
    }, (res) => {
        let buffers = [];

        res.on('data', (data) => {
            buffers.push(data);
        });

        res.on('end', () => {
            cb(Buffer.concat(buffers));
        });
    });

    req.end();
}

function makePOSTRequest(host, path, headers = {}, body = {}, cb) {
    let req = https.request({
        hostname: host,
        path: path,
        method: "POST",
        headers: headers
    }, (res) => {
        let buffers = [];

        res.on('data', (data) => {
            buffers.push(data);
        });

        res.on('end', () => {
            cb(Buffer.concat(buffers), res.headers);
        });
    });

    req.end(body);
}