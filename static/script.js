$(document).ready(function(){	
	
	$(function () {
    //  Accordion Panels
    $(".sortable-accordion div").show();
    $('.sortable-accordion div').slideToggle('slow');
    $(".sortable-accordion h3").click(function () {
        $(this).next(".inner").slideToggle().siblings(".inner:visible").slideUp();
        $(this).toggleClass("current");
        $(this).siblings("h3").removeClass("current");
    });
});
  
$( ".sortable" ).sortable({   
	placeholder: "ui-sortable-placeholder"   
}).find("li").append("<span class='options'></span>");  

$('#submenu a').click(function(){return false;})

$('.options').click(function(){
	var childpos = $(this).offset();  
  var  parentpos = $(this).parent().offset();
  
  var posLeft = childpos.left - parentpos.left;

	$('#submenu').css({'top':(childpos.top - 10)+"px", 'left': (posLeft+420)+"px"}).fadeIn(200);
	$('#submenu').mouseleave(function(){$(this).fadeOut(200);});
});

$('#toggleMenu .list').click(function(){
	$('#sidebar-menu li span').animate({'opacity':1, 'margin-left':'0px'});
	$('#sidebar-menu').toggleClass('animate');
	$('#toggleMenu .list').fadeOut();
	$('#toggleMenu .thumbs').fadeIn();

});

$('#toggleMenu .thumbs').click(function(){
	$('#sidebar-menu li span').css({'opacity': 0, 'margin-left': "10px"});
	$('#sidebar-menu').toggleClass('animate');	
	$('#toggleMenu .thumbs').fadeOut();
	$('#toggleMenu .list').fadeIn();	
	
});

$("#sidebar-menu li").click(function(){
	$("#sidebar-menu li").not(this).removeClass("selected");
	$(this).toggleClass("selected");
});

$('#drop-select').click(function(){
	$('#dropdown-list').toggleClass('animate');
});

$('#dropdown-list li').click(function(){$('#dropdown-list').removeClass('animate');});

});