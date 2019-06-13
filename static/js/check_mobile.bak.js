(function() {
	var GLOBLE_PARAMS = (function () {
		var args = new Object();
		var query = location.search.substring(1);
	 
		var pairs = query.split("&"); // Break at ampersand
		for(var i = 0; i < pairs.length; i++) {
			var pos = pairs[i].indexOf('=');
			if (pos == -1) continue;
			var argname = pairs[i].substring(0,pos);
			var value = pairs[i].substring(pos+1);
			value = decodeURIComponent(value);
			args[argname] = value;
		}
		return args;
	})();
    var u = navigator.userAgent;
    var isMobile = false;
    if(u.indexOf("Android") > -1) {
        isMobile = true;
    } else if(u.indexOf("iPhone") > -1) {
        isMobile = true;
    } else if(u.indexOf("MicroMessenger") > -1) {
        isMobile = true;
    }
    if(GLOBLE_PARAMS["pc"]){
        isMobile = false;
    }
    window.IF_MOBILE_BROSWER_JUMP_TO = function (url) {
        if(url && isMobile) {
            location.href = url;
        }
    }
})();