$(document).ready(function() {

        // JQuery code to be added in here.
	// $("#about-btn").click( function(event){
		// alert("You clicked the JQuery button");
	// });
	
	// $("button").hover( function(){
		// $(this).css('background-color', 'red');
	// },
	// function(){
		// $(this).css('background-color', 'blue');
	// });
	
	$("#about-btn").addClass("btn btn-primary");
	
	$("#about-btn").click( function(event){
		msgstr = $("#msg").html()
		msgstr = msgstr + "o"
		$("#msg").html(msgstr)
	});
	
});