$(document).ready(function() {
    window.NUM_CHARS = 140;
    $("#grumb_chars_left").html(window.NUM_CHARS);

    // Toggle the little white arrow triangle on the settings menu.
    // Uses custom events triggered by toggling/removing a class to hookon to
    // existing bootstrap javascript code.
    // Took way to long to implement for one stupid little triangle.
    $("#settings-dropdown").bind('cssClassToggled', function(){
        $("#settings-menu-arrow").css("display","block");
    });
    $("#settings-dropdown").bind('cssClassRemoved', function(){
        $("#settings-menu-arrow").css("display","none");
    });
    $(".dislikes-others").popover({'html':true});

    // Periodically check for new grumbs.
    var tid = setInterval(checkNewFollowerGrumbs, 10000);
});

// Comments form submission.
$('.grumbs-list').on('submit', '.post-comment', function() {
    $.ajax({
        data: $(this).serialize(),
        type: $(this).attr("method"),
        url: $(this).attr("action"),
        success: function(response) {
            comment_html = response.html;
            grumb_id = response.grumb_id;
            $("#grumb_" + grumb_id + " .comments-list li").last().prev().after(comment_html);
            $("#grumb_" + grumb_id + " .comments-list :text").val("");
        }
    });
    return false;
});

// dislike comment.
$('.grumbs-list').on('submit', '.dislike-form-comment', function() {
    $.ajax({
        data: $(this).serialize(),
        type: $(this).attr("method"),
        url: $(this).attr("action"),
        success: function(response) {
            num_dislikes = response[0].fields.dislikes.length
            $(".comment_" + response[0].pk + " .num_dislikes").html(num_dislikes);
            // Change "dislike" option to "undislike" or vice versa
            if (this.url.search("undislike") >= 0) {
                $(".comment_" + response[0].pk + " .dislike-link").val("Dislike");
                $(".comment_" + response[0].pk + " .dislike-form-comment").attr("action","/grumblr/dislike_comment/");
            }
            else {
                $(".comment_" + response[0].pk + " .dislike-link").val("Undislike");
                $(".comment_" + response[0].pk + " .dislike-form-comment").attr("action","/grumblr/undislike_comment/");
            }
        }
    });
    return false;
});

// dislike grumb.
$('.grumbs-list').on('submit', '.dislike-form-grumb', function() {
    $.ajax({ // create an AJAX call...
        data: $(this).serialize(), // get the form data
        type: $(this).attr("method"), // GET or POST
        url: $(this).attr("action"), // the file to call
        success: function(response) { // on success..

            // Format dislike names and popover data.
            // Making this dynamic is a pain in the ass.
            dislike_str = ""
            num_dislikes = response[0].fields.dislikes.length
            if (num_dislikes == 0) {
                dislike_str = "Nobody dislikes this."
            }
            else if (num_dislikes == 1) {
                var name = "<a href='/grumblr/profile/" + response[1].fields.username + "/'>" + response[1].fields.first_name + "</a>";
                dislike_str = name + " dislikes this."
            }
            else if (num_dislikes == 2) {
                var name1 = "<a href='/grumblr/profile/" + response[1].fields.username + "/'>" + response[1].fields.first_name + "</a>";
                var name2 = "<a href='/grumblr/profile/" + response[2].fields.username + "/'>" + response[2].fields.first_name + "</a>";
                dislike_str = name1 + " and " + name2  + " dislike this."
            }
            else if (num_dislikes == 3) {
                var name1 = "<a href='/grumblr/profile/" + response[1].fields.username + "/'>" + response[1].fields.first_name + "</a>";
                var name2 = "<a href='/grumblr/profile/" + response[2].fields.username + "/'>" + response[2].fields.first_name + "</a>";
                var name3 = "<a href='/grumblr/profile/" + response[3].fields.username + "/'>" + response[3].fields.first_name + "</a>";
                dislike_str = name1 + ", " + name2 + " and " + name3  + " dislike this."
            }
            else if (num_dislikes == 4) {
                var name1 = "<a href='/grumblr/profile/" + response[1].fields.username + "/'>" + response[1].fields.first_name + "</a>";
                var name2 = "<a href='/grumblr/profile/" + response[2].fields.username + "/'>" + response[2].fields.first_name + "</a>";
                var name3 = "<a href='/grumblr/profile/" + response[3].fields.username + "/'>" + response[3].fields.first_name + "</a>";
                dislike_str = name1 + ", " + name2 + ", " + name3  + " and " +
                    "<a href='#' class='dislikes-others' data-toggle='popover' data-content='" +
                    '<a href="/grumblr/profile/' + response[4].fields.username + '/">' + response[4].fields.first_name + "</a>" +
                    "'>1 other</a>" +
                    " dislike this.";
            }
            else if (num_dislikes > 4) {
                var name1 = "<a href='/grumblr/profile/" + response[1].fields.username + "/'>" + response[1].fields.first_name + "</a>";
                var name2 = "<a href='/grumblr/profile/" + response[2].fields.username + "/'>" + response[2].fields.first_name + "</a>";
                var name3 = "<a href='/grumblr/profile/" + response[3].fields.username + "/'>" + response[3].fields.first_name + "</a>";
                var names = "";
                for (var i = 4; i <= num_dislikes; i++) {
                    names += '<a href="/grumblr/profile/' + response[i].fields.username + '/">' + response[i].fields.first_name + "</a>" + "<br>";
                }
                console.log(names);
                dislike_str = name1 + ", " + name2 + ", " + name3  + " and " +
                    "<a href='#' class='dislikes-others' data-toggle='popover' data-content='" + names +
                    "'>" + (num_dislikes - 3) + " others</a>" +
                    " dislike this.";
            }
            var text = "&nbsp;" + dislike_str;
            $(".grumb_" + response[0].pk + " .grumb-stats .num_dislikes").html(text);
            // Change "dislike" option to "undislike" or vice versa
            if (this.url.search("undislike") >= 0) {
                $(".grumb_" + response[0].pk + " .dislike-form-grumb .dislike-link").val("Dislike");
                $(".grumb_" + response[0].pk + " .dislike-form-grumb").attr("action","/grumblr/dislike_grumb/");
            }
            else {
                $(".grumb_" + response[0].pk + " .dislike-form-grumb .dislike-link").val("Undislike");
                $(".grumb_" + response[0].pk + " .dislike-form-grumb").attr("action","/grumblr/undislike_grumb/");
            }
            // Initialize popover.
            $(".grumb_" + response[0].pk + " .grumb-stats .dislikes-others").popover({'html':true});
        }
    });
    return false;
});

// Toggle visibility of dislike buttons.
$('.grumbs-list').on('mouseenter', '.grumb', function() {
        $(this).find(".grumb-button").css("visibility","visible");
});
$('.grumbs-list').on('mouseleave', '.grumb', function() {
        $(this).find(".grumb-button").css("visibility","hidden");
});

$(".modal-btn, .modal-link").on("click", function() {
    // Center the modal window.
    var id = "#" + $(this).attr("id") + "_modal_window"
    var modalHeight = $(id).height();
    var windowHeight = $(window).height();
    var marginHeight = (windowHeight - modalHeight)/2;
    $(id).css("margin-top", marginHeight + "px");

    // Loads initial values into the edit area.
    if ($(this).attr("id") == "edit_contacts") {
        $("#edit-contacts-table input").each(function() {
            var id = "#contact-" + $(this).attr("name")
            var orig_value = $(id).html();
            $(this).attr("value", orig_value);
        });
    }
    // Loads initial values into the edit area.
    else if ($(this).attr("id") == "edit_aboutme") {
        orig_text = $("#aboutme-text").html();
        $("#edit-aboutme-text").val(orig_text);
    }
    // Loads initial values into the edit area.
    else if ($(this).attr("id") == "edit_links") {
        var orig_text = "";
        $("#links-text a").each(function() {
            orig_text += ($(this).text() + "\n");
        });
        $("#edit-links-text").val(orig_text.trimRight());
    }
});

$("#profile-navbar li").on("click", function() {
    // Change the active tab to the new one.
    $("#profile-navbar li").removeClass("active");
    $(this).addClass("active");

    // Show the page.
    var name = $(this).attr("name");
    var pageName = "#page-" + name;
    $(".page").addClass("hidden");
    $(pageName).removeClass("hidden");
});

// Update number of characters left.
$("#grumb_input_text").on("keyup", function(event) {
    var chars_left = window.NUM_CHARS - this.value.length
    $("#grumb_chars_left").html(chars_left);
});

// Prevent further entering of text if num chars left < 0
$("#grumb_input_text").on("keydown", function(event) {
    var chars_left = window.NUM_CHARS - this.value.length
    key = event.keyCode
    var is_char_keypress = key >= 65 && key <= 90 && event.ctrlKey == false
    if (chars_left <= 0 && is_char_keypress) {
        event.preventDefault();
    }
});

function updateContacts() {
    // Rewrite this to send to server.
    $(".edit-contact-text").each(function() {
        var id = "#contact-" + $(this).attr("name")
        var new_value = $(this).attr("value");
        $(id).html(new_value);
    });
    $('#edit_contacts_modal').modal('hide');
}

function updateAboutme() {
    // Rewrite this to send to server.
    var lines = $("#edit-aboutme-text").val().split("\n");
    var html_text = "";
    for (var i = 0; i < lines.length; i++) {
        html_text += ("<div>" + lines[i] + "</div>");
    }
    $("#aboutme-text").html(html_text);
    $('#edit_aboutme_modal').modal('hide');

}

function updateLinks() {
    // Rewrite this to send to server.
    var lines = $("#edit-links-text").val().split("\n");
    var html_text = "";
    for (var i = 0; i < lines.length; i++) {
        if (lines[i] != "") {
            html_text += "<div><a href='" + lines[i] + "'>" + lines[i] + "</a></div>";
        }
    }
    $("#links-text").html(html_text);
    $('#edit_links_modal').modal('hide');

}


function checkNewFollowerGrumbs() {
    // Get the id of the first grumb in the list.
    var first_grumb_id = $("#followers-grumbs-list li").first().attr("id").slice("6");
    $.ajax({
        data: {first_grumb_id: first_grumb_id},
        type: "GET",
        url: "/grumblr/update_follower_grumbs",
        success: function(response) {
            $("#followers-grumbs-list").prepend(response.html);
        }
    });
}


$('body').on('click.collapse-next.data-api', '[data-toggle=collapse-next]', function (e) {
  var $target = $(this).parent().next()
  $target.data('collapse') ? $target.collapse('toggle') : $target.collapse()
})
