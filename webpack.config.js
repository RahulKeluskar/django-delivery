var path = require('path')
var webpack = require('webpack')
var BundleTracker = require('webpack-bundle-tracker')

module.exports = {
	context: __dirname,
	
	entry: './assets/js/index',
	
	output: {
		path: path.resolve('./assets/bundles/'),
		filename: '[name]-[hash].js',
	},
	
	plugins: [
		new BundleTracker({filename: './webpack-stats.json'}),
	],
	
	module: {
		loaders: [
		  { test: /\.jsx?$/,
		  	exclude: /node_modules/,
		  	loader: 'babel-loader',
		  	query: {
		  		presets: ['react']
		  	}
		  },
          {
            test: /[\/\\]node_modules[\/\\]some-module[\/\\]index\.js$/,
            loader: "imports?this=>window"
          },
          {
            test: /[\/\\]node_modules[\/\\]some-module[\/\\]index\.js$/,
            loader: "imports?define=>false"
          }
		]
	},
	
	plugins: [
		new webpack.ProvidePlugin({
			$: 'jquery',
			jQuery: 'jquery'
		})
	],
	
	resolve: {
		modulesDirectories: ['node_modules', 'bower_components'],
		extensions: ['', '.js', '.jsx'],
		alias: {
			jquery: 'jquery/dist/jquery.js'
		}
	}
}
