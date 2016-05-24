var system = require('system');
var webPage = require('webpage');
var page = webPage.create();
var args = system.args;
var ms = args[args.length-1];

page.viewportSize = { width: 1920, height: 1080 };
page.open(args[1], function start(status) {
  window.setTimeout(function() {
    var args = system.args;
    console.log(args[args.length-2])
    if (args.length < 3) {
	console.log("No image-url supplied.");
	phantom.exit();
	};
    var fname = args[2];
    console.log(fname + "[ "+args[args.length-2]+"ms delay]")
    page.render(fname, {format: 'jpeg', quality: '100'});
    phantom.exit();
  }, ms);
});
