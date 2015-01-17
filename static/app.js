var App = angular.module('SousChef', []);

App.controller('ContentController', ['$scope', 'Recipes',function($scope, Recipes){

}])

App.factory('Recipes', [function(){
    return{
        query:function(){
            console.log(1)
        }
    }
}])