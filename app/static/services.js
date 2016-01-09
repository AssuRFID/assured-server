var assuredWebServices = angular.module('assuredWebServices', ['ngResource']);

assuredWebServices.factory('Tag', function($resource) {
  return $resource('/assured/api/v1.0/tags/:id', null,
				   {
					 'update': { method:'PUT', isArray: false }
				   }
				  )
});
