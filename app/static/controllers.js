var assuredWebControllers = angular.module('assuredWebControllers', [])

assuredWebControllers.controller('TagListCtrl', function($scope, Tag) {
  json = Tag.query()
  $scope.tags = json
});

assuredWebControllers.controller('TagDetailCtrl', function($scope, $routeParams, Tag) {
  $scope.tagId = $routeParams.tagId;

  $scope.tag = Tag.get({id: $routeParams.tagId}, function(tag) {
	/*console.log(tag);*/
  });
  
});
