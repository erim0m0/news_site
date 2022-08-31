let menuOfSupportClass = document.getElementById("menu-of-support").classList;
var headerIconId = document.getElementById("header-icon-i").classList;

$(window).load(function () {
    // Animate loader off-screen
    $(".se-pre-con").fadeOut(300);
});

$(document).ready(function () {
    $('.support').hover(function () {
        $('.left-header > section').slideToggle(100);
    });

    $('#instant-prices').hover(function () {
        $('.menu-of-instant-prices').slideToggle(400);
    })

    $('#instant-news').hover(function () {
        $('.menu-of-instant-news').slideToggle(400);
    });

    $('#logo').hover(function () {
        $('.zoom-img-of-arka').toggle(500);
    });

    $('#header-icon').click(function () {
        $('#header').slideToggle(400);
        if (headerIconId.contains('fa-angle-double-up')) {
            $('#header-icon i').addClass('fa-angle-double-down')
            $('#header-icon i').removeClass('fa-angle-double-up')
        } else {
            $('#header-icon i').addClass('fa-angle-double-up')
            $('#header-icon i').removeClass('fa-angle-double-down')
        }
    });
});

function scrollTopHeader() {
    document.getElementById('header').scrollIntoView({behavior: "smooth"});
}


