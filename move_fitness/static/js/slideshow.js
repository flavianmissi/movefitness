window.addEvent('domready', function() {
    /* settings */
    var showDuration = 3000;
    var container = $('slideshow-container');
    var imgContainers = container.getElements('.img-element');
    var currentIndex = 0;
    var interval;

    /* opacity and fade */
    imgContainers.each(function(img, i) {
        if(i > 0) {
            img.set('opacity',0);
        }
    });

    /* worker */
    var show = function() {
        imgContainers[currentIndex].fade('out');
        imgContainers[currentIndex = currentIndex < imgContainers.length - 1 ? currentIndex+1 : 0].fade('in');
    };

    /* start once the page is finished loading */
    window.addEvent('load',function() {
        interval = show.periodical(showDuration);
    });

    var i;
    for (i in document.images) {
        if (document.images[i].src) {
            var imgSrc = document.images[i].src;
            if (imgSrc.substr(imgSrc.length-4) === '.png' || imgSrc.substr(imgSrc.length-4) === '.PNG') {
                document.images[i].style.filter = "progid:DXImageTransform.Microsoft.AlphaImageLoader(enabled='true',sizingMethod='crop',src='" + imgSrc + "')";
            }
        }
    }

});
