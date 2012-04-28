window.addEvent('domready', function() {
    (function(d, s, id) {
        var js, fjs = d.getElementsByTagName(s)[0];
        if (d.getElementById(id)) return;
        js = d.createElement(s); js.id = id;
        js.src = "//connect.facebook.net/pt_BR/all.js#xfbml=1";
        fjs.parentNode.insertBefore(js, fjs);
    }(document, 'script', 'facebook-jssdk'));
});

new TWTR.Widget({
  version: 2,
  type: 'profile',
  rpp: 4,
  interval: 30000,
  width: 250,
  height: 300,
  id: 'tweets',
  subject: 'Siga-nos no twitter',
  theme: {
      shell: {
          background: '#8ec1da',
          color: '#ffffff'
      },
      tweets: {
          background: '#ffffff',
          color: '#444444',
          links: '#1985b5'
      }
  },
  features: {
      scrollbar: false,
      loop: true,
      live: true,
      behavior: 'default'
  }
}).render().setUser('MoveFitnessRJ').start();
