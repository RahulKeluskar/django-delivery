var React = require('react')

module.exports = React.createClass({
	loadRestaurantsFromServer: function() {
		$.ajax({
			url: this.props.url,
			datatype: 'json',
			cache: false, 
			success: function(data) {
				this.setState({data:data})
			}.bind(this)
		})
	},
	getInitialState: function() {
		return {data: []};
	},
	componentDidMount: function() {
		this.loadRestaurantsFromServer();
	},
	render: function() {
		return ( 
			<div>
			<h1>Oh shit, React works!</h1>
			<p>{this.state.data}</p>
			</div>
		)
	}
})
