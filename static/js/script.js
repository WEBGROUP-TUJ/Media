$(".phone_menu").click(function () {
    $(".menu2").slideToggle(800);
    if ($(".main_h1").css("margin-top") == "270px") {
        $(".main_h1").css("margin-top","70px");
        $(".section1").css("height") = "1258px";
    }
    else{
        $(".main_h1").css("margin-top","270px");
        $(".section1").css("height") = "1458px";
    }
})

$(window).on('load', function() {

    $('#js-preloader').addClass('loaded');

});


const updateScrollPercentage = function() { 
    const heightOfWindow = window.innerHeight,
    contentScrolled = window.pageYOffset,
    bodyHeight = document.body.offsetHeight,
    percentage = document.querySelector(".percentage"),
    percentageVal = document.querySelector("#percentage-value")
    if(bodyHeight - contentScrolled <= heightOfWindow) {
        percentageVal.textContent = percentage.style.width = "100%"
    }
    else {
        const total = bodyHeight - heightOfWindow,
        got = contentScrolled,
        percent = parseInt((got/total) * 100)
        percentageVal.textContent = percentage.style.width = percent + "%"
    }
}
window.addEventListener('scroll', updateScrollPercentage)

// const swiper = new Swiper('.swiper-container', {
//   // Optional parameters
//   // cssMode: true,
//   spaceBetween: 100,
//   loop: true,
//   effect: 'fade',
//   speed: 2000,
//   autoplay: {
//       delay: 8000,
//       disableOnInteraction: false,
//   },
//   direction: 'horizontal',

//   // If we need pagination

//   // Navigation arrows
//   navigation: {
//       nextEl: '.swiper-button-next',
//       prevEl: '.swiper-button-prev',
//   },

//   // And if we need scrollbar
//   scrollbar: {
//       el: '.swiper-scrollbar',
//   },
// });


    




// $(".hamburger__button").click(function () {
//   $(this).css("margin-bottom", "100px");
// })