var React = require('react')
var App = require('./app')
require('expose?$!expose?jQuery!jquery');


ReactDOM.render(<App url='/api/restaurants/'/>, document.getElementById('container'))
