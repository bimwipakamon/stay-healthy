// <!-- Call opacity on hover images from carousel-->

$(document).ready(function () {
    $("img.imgOpa").hover(function () {
        $(this).stop().animate({ opacity: "0.6" }, 'slow');
    },
        function () {
            $(this).stop().animate({ opacity: "1.0" }, 'slow');
        });
});