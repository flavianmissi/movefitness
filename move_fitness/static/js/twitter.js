var TwitterGitter = new Class({

    Implements: [Options,Events],

    options: {
        count: 2,
        sinceID: 1,
        link: true,
        onRequest: $empty,
        onComplete: $empty
    },

    initialize: function(username, options) {
        //set options
        this.setOptions(options);
        this.info = {};
        this.username = username;
    },

    //get it!
    retrieve: function() {
        console.log("oi");
        that = this;
        new Request.JSONP({
            url: 'http://twitter.com/statuses/user_timeline/' + that.username + '.json',
            data: {
                count: that.options.count,
                since_id: that.options.sinceID
            },
            onRequest: this.fireEvent('request'),
            onComplete: function(data) {
                //linkify?
                if(that.options.link) {
                    data.each(function(tweet) { tweet.text = that.linkify(tweet.text); }, that);
                }
                //complete!
                //this.fireEvent('complete', [data, data[0].user]);
                this.fireEvent('complete', [data, "foooooo"]);
            }.bind(this)
        }).send();
        return this;
    },

    //format
    linkify: function(text) {
        //courtesy of Jeremy Parrish (rrish.org)
        return text.replace(/(https?:\/\/\S+)/gi,'<a href="$1">$1</a>').replace(/(^|\s)@(\w+)/g,'$1<a href="http://twitter.com/$2">@$2</a>').replace(/(^|\s)#(\w+)/g,'$1#<a href="http://search.twitter.com/search?q=%23$2">$2</a>');
    }
});
