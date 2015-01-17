var App = angular.module('SousChef', []);

App.controller('ContentController', ['$scope','$http',function($scope, $http){
    $scope.submitSearch = function (){
        $http.post('/recipe/get/all',{search:$scope.searchValue}).success(function(data){
            $scope.searchOptions = data;
        })
    }
}])