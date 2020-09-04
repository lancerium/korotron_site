

if( /Android|webOS|iPhone|iPad|iPod|BlackBerry|IEMobile|Opera Mini/i.test(navigator.userAgent) ) {
    document.getElementById("header-phone").innerHTML = '<a href="tel:+7920717686" style="color: aliceblue; font-size: 15px;">+7 (920) 771-76-86</a>';
} else	{
    document.getElementById("header-phone").innerHTML = '<span style="color: #f0f8ff; font-size: 15px;">+7 (920) 771-76-86</span> ';
}

$(document).ready(function () {
            var offset = 250;
            var duration = 500;

            $(window).scroll(function () {
                if($(this).scrollTop() > offset){
                    $('.goTop').fadeIn(duration);
                }else {
                    $('.goTop').fadeOut(duration);
                }
            });
        })