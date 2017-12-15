// scraper.js
'use strict';

var Nightmare = require('nightmare');
new Nightmare()
// input the captera page to scraape
  .goto('https://www.capterra.com/p/165410/WooCommerce/')
  .wait(150)
  .screenshot('./debug/1_screen_load.png')
  .html('./data/captera.html', 'HTMLComplete')
  .run(function(err, nightmare) {
    if (err) {
      console.log(err);
    }
    process.exit()
  });