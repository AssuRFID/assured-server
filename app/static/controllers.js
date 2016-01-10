var assuredWebControllers = angular.module('assuredWebControllers', [])

assuredWebControllers.controller('TagListCtrl', function($scope, Tag) {
  json = Tag.query();
  $scope.tags = json;
  $scope.onEdit = function(index) {
	$scope.editedTag = angular.extend({}, $scope.tags[index]);
	$scope.editedTagIndex = index;
	$scope.editedTagId = $scope.tags[index].id;
  }

  $scope.saveEdit = function() {
	Tag.update({ id: $scope.editedTag.id }, $scope.editedTag);
	$scope.tags[$scope.editedTagIndex] = $scope.editedTag;
  }

  $scope.deleteTag = function() {
	Tag.delete({ id: $scope.editedTagId });
	$scope.tags.splice($scope.editedTagIndex, 1);
  }
  
});

assuredWebControllers.controller('TagDetailCtrl', function($scope, $routeParams, Tag) {
  $scope.tagId = $routeParams.tagId;

  $scope.tag = Tag.get({id: $routeParams.tagId}, function(tag) {
	/*console.log(tag);*/
  });
  
});
