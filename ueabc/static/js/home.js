$(window).load(function() {
	$("#slider").nivoSlider({
	    directionNavHide: false,
	    captionOpacity: 1,
	    prevText: "<",
	    nextText: ">",
	    pauseTime:5000
	});
	$(".addForm").hide();
	$(".userList").hide();
});