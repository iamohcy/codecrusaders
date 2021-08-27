$(document).ready(function() {

    // // Choose a random background image.
    // // Source: http://www.markinns.com/articles/full/simple_two_line_image_randomiser_script_with_jquery
    // var images = ["sunny.jpg", "spots2.jpg", "cat.jpg", "cat2.jpg", "building.jpg", "cat3.jpg", "train.jpg"];
    // $("body").css({"background-image": "url(" + STATIC_URL + "css/bg/" + images[Math.floor(Math.random() * images.length)] + ")"});

    // Dynamically set height of signin-row
    var height = $(window).height();
    $("#parent-div").css("margin-top",(height*3/5));


    // $('#register-div').transition({ x: '-1000px' }, 0);
    $("#register-link").on("click", function() {
        $('#signin-div').addClass("animated slideOutRight");
        $('#register-div').removeClass("hidden");
        $('#register-div').removeClass("animated slideOutRight");
        $('#register-div').addClass("animated slideInLeft");
        setTimeout(function() {$('#signin-div').addClass("hidden");},700)
    });

    $("#signin-link").on("click", function() {
        $('#register-div').addClass("animated slideOutRight");
        $('#signin-div').removeClass("hidden");
        $('#signin-div').removeClass("animated slideOutRight");
        $('#signin-div').addClass("animated slideInLeft");
        setTimeout(function() {$('#register-div').addClass("hidden");}, 700)

    });

});




// $(".dropdown-toggle").dropdown();


// $("#month-dropdown li").on("click", function() {
//     var day_text = $("#dob_month").html();
//     var month_text = $(this).find("a").html();
//     var year_text = $("#dob_year").html();
//     var dob_text = day_text + " " + month_text + " " + year_text

//     $("#dob_month").html(month_text)
//     $("#dropdown_title_month").html(month_text);
//     $("#dob").val(dob_text);
// });
// $("#day-dropdown li").on("click", function() {
//     var day_text = $(this).find("a").html();
//     var month_text = $("#dob_day").html();
//     var year_text = $("#dob_year").html();
//     var dob_text = day_text + " " + month_text + " " + year_text

//     $("#dob_day").html(day_text)
//     $("#dropdown_title_day").html(day_text);
//     $("#dob").val(dob_text);
// });
// $("#year-dropdown li").on("click", function() {
//     var day_text = $("#dob_month").html();
//     var month_text = $("#dob_day").html();
//     var year_text = $(this).find("a").html();
//     var dob_text = day_text + " " + month_text + " " + year_text

//     $("#dob_year").html(year_text)
//     $("#dropdown_title_year").html(year_text);
//     $("#dob").val(dob_text);
// });
