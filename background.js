$(function(){
	var lines;
	var rollIcon = chrome.extension.getURL("icon.png");
	jQuery.get(chrome.extension.getURL("ricklist.txt"), function(data) {
		lines = data.split("\n");
		lines = lines.filter(function(value){
				return value.charAt(0) !== "!" && value.charAt(0) !== "["
			       	})
		lines = lines.map(function(url){
		   if(url.indexOf("youtube.com") !== -1){
			return "www.youtube.com/watch?v=" + url.substring(url.indexOf("=")+1);
		   }
		   if(url.indexOf("#body") !== -1){
		   	return url.substring(0,url.indexOf("#body"));
		   }
		   return url
		})
		//alert($.inArray("#", lines))
		$("a").each(function(){
	  	  var href = $(this).attr('href') 
	  	  if(href.indexOf("http") === 0){
			href = href.substring(href.indexOf("//")+2);
	 	   }
	 	   if($.inArray(href,lines) !== -1){
			$(this).before('<img src="'+rollIcon+'" style="width:21px; height:21px">');	
	           } 
		})
	});
})

