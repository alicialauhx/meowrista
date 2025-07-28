$(document).ready(function(){
    $('.menu-btn').click(function(){
        $('.sidebar').addClass('active');
        $('.menu-btn').css("visibility", "hidden");
    });
    $('.close-btn').click(function(){
        $('.sidebar').removeClass('active');
        $('.menu-btn').css("visibility", "visible");
    }); 
    $('.sub-btn').click(function(){
        $('.sub-menu').not($(this).next('.sub-menu')).slideUp();
        $('.sub-btn .dropdown').not($(this).find('.dropdown')).removeClass('rotate');

        $(this).next('.sub-menu').slideToggle();
        $(this).find('.dropdown').toggleClass('rotate');
    });
})

$(document).click(function(event) {
    if (!$(event.target).closest('.sidebar, .menu-btn').length) {
        $('.sidebar').removeClass('active');
        $('.menu-btn').css("visibility", "visible");
    }
});