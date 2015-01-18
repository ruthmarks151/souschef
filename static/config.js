App.config(['$routeProvider',
  function($routeProvider) {
    $routeProvider.
      when('/', {
        templateUrl: 'templates/search.html',
        controller: 'SearchController'
      }).
      when('/recipe/:recipeid', {
        templateUrl: 'templates/recipe.html',
        controller: 'RecipeController'
      }).
      otherwise({
        redirectTo: '/'
      });
  }]);