var webpage = require("webpage");
var system = require('system');

if (system.args.length === 1) {
	console.log('Usage: screenpage.js <some URL> <file name>');
	phantom.exit();
}

urladdr = system.args[1];
filename = system.args[2];

function main(url,file) {
    	var page = webpage.create();
    	page.settings.userAgent = 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:39.0) Gecko/20100101 Firefox/39.0';
	page.settings.resourceTimeout = 30000;
	page.viewportSize = { width: 1024, height: 768 };

    	page.open(url, function(status) {
        if (status != "success") {
            	console.log('ERROR');
        }else{
		page.render(file);
        	page.close();
	}
	phantom.exit();
    });
}


main(urladdr,filename);
