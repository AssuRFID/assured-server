	var app = angular.module('assuredWeb', ['ngRoute', 'ngResource', 'assuredWebControllers', 'assuredWebServices'])
	app.config(['$interpolateProvider', function($interpolateProvider) {
	  $interpolateProvider.startSymbol('[[');
	  $interpolateProvider.endSymbol(']]');
	}]);
	app.config(['$routeProvider', function($routeProvider) {
	  $routeProvider.
		when('/tags', {
		  templateUrl: 'static/partials/tag-list.html',
		  controller: 'TagListCtrl'
		}).
		when('/tags/:tagId', {
		  templateUrl: 'static/partials/tag-detail.html',
		  controller: 'TagDetailCtrl'
		}).
		otherwise({
		  redirectTo: '/tags'
		});
	}]);
