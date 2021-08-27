$(document).ready(function() {

    // Choose a random background image.
    // Source: http://www.markinns.com/articles/full/simple_two_line_image_randomiser_script_with_jquery
    var images = ["sunny.jpg", "spots2.jpg", "cat.jpg", "cat2.jpg", "building.jpg", "cat3.jpg", "train.jpg"];
    $("body").css({"background-image": "url(" + STATIC_URL + "css/bg/" + images[Math.floor(Math.random() * images.length)] + ")"});

    var height = $("#signup-col").height();
    $("#message").height(height-50);
});

$(".dropdown-toggle").dropdown();


$("#month-dropdown li").on("click", function() {
    var day_text = $("#dob_month").html();
    var month_text = $(this).find("a").html();
    var year_text = $("#dob_year").html();
    var dob_text = day_text + " " + month_text + " " + year_text

    $("#dob_month").html(month_text)
    $("#dropdown_title_month").html(month_text);
    $("#dob").val(dob_text);
});
$("#day-dropdown li").on("click", function() {
    var day_text = $(this).find("a").html();
    var month_text = $("#dob_day").html();
    var year_text = $("#dob_year").html();
    var dob_text = day_text + " " + month_text + " " + year_text

    $("#dob_day").html(day_text)
    $("#dropdown_title_day").html(day_text);
    $("#dob").val(dob_text);
});
$("#year-dropdown li").on("click", function() {
    var day_text = $("#dob_month").html();
    var month_text = $("#dob_day").html();
    var year_text = $(this).find("a").html();
    var dob_text = day_text + " " + month_text + " " + year_text

    $("#dob_year").html(year_text)
    $("#dropdown_title_year").html(year_text);
    $("#dob").val(dob_text);
});
