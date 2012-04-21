window.addEvent('domready', function() {
    var imgs = $$(".thumb.column img");
    var origClass = "two columns";
    imgs.addEvent("mouseover", function(e) {
        e.target.className += " active";
    });
    imgs.addEvent("mouseout", function(e) {
        e.target.className = origClass;
    });
});
