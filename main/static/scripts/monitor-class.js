// Create custom events for class changes.
// Use to add on to bootstrap javascript without modifying bootstrap.js code.
// Credits: http://stackoverflow.com/questions/1950038/jquery-fire-event-if-css-class-changed
(function(){
    var originalToggleClassMethod = jQuery.fn.toggleClass;
    jQuery.fn.toggleClass = function(){
        var result = originalToggleClassMethod.apply( this, arguments );
        jQuery(this).trigger('cssClassToggled');
        return result;
    }
})();

(function(){
    var originalRemoveClassMethod = jQuery.fn.removeClass;
    jQuery.fn.removeClass = function(){
        var result = originalRemoveClassMethod.apply( this, arguments );
        jQuery(this).trigger('cssClassRemoved');
        return result;
    }
})();

