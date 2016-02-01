var React = require('react')
var App = require('./app')
var ReactDOM = require('react-dom')

require('expose?$!expose?jQuery!jquery');


ReactDOM.render(<App url='/api/restaurants/' pollInterval={10000}/>, document.getElementById('container'))
