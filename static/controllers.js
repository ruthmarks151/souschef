App.controller('SearchController', ['$scope', '$http','Request', function($scope, $http, Request) {
    $scope.submitSearch = function() {
        Request.searchResults($scope.searchValue).success(function(data) {
            $scope.searchOptions = data;
        })
    }
}])

App.controller('RecipeController',['$scope', 'speechAPI','Request','$routeParams', function($scope, speechAPI, Request, $routeParams){
    speechAPI.SpeechRecognition();
    Request.recipeByID($routeParams.recipeid).success(function(data){
        $scope.recipe = Request.pretty(data);
    })
    
    
}])