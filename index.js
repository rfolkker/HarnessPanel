/* npm Modules */
const express = require("express");
const app = express();
const request = require('request');
const http = require('http');
const path = require("path");
const bodyParser = require("body-parser");
const fs = require('fs');
const httpServer = http.Server(app);
module.exports = run
	
function run(){
	var port = 3200;
	var hostname = "localhost"

	/* Start the server */
	httpServer.listen(port);

	/* Middlewares */
	app.use(bodyParser.json());
	app.use(bodyParser.urlencoded({ limit: '50mb',extended: true }));
	app.use(express.static(path.join(__dirname, "../css")));

	app.get("/", (req,res,next) =>{
		res.status(200).send("Hello world");
	});
	
	app.get("/exportDOM", (req,res,next) =>{
		var csInterface = new CSInterface();
		const exportDOMAction = (res, result) => {
			res.status(200).send(result);
		};
		
		const embeddedCall = (fn, ...fixedArgs) => {
			return function (...remainingArgs) {
				return fn.apply(this, fixedArgs.concat(remainingArgs));
			};
		};

		const callbackDOM = embeddedCall(exportDOMAction, res);
		csInterface.evalScript("exportDOM()", callbackDOM);
	});
}