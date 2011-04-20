$(document).ready(function(){
    var slideWidth = $(".slider-block").width();
    var slides = $('.slide');
    var numberOfSlides = slides.length;

    // Wrap all .slides with #slideInner div
    slides
        .wrapAll('<div id="slideInner"></div>')
        .css({ 'float' : 'left', 'width' : slideWidth });

    var block = $('#slideInner')
        .css('width', slideWidth * numberOfSlides);

    function nextSlide() {
        block.animate({
            'marginLeft' : -slideWidth
        }, function(){
            block.find('.slide:first').detach().appendTo(block);
            block.css({marginLeft: 0})
            setTimeout(nextSlide, 5000);
        });
    };
    setTimeout(nextSlide, 5000);
});
