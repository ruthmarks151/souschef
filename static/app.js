var App = angular.module('SousChef', ['ngRoute']);

App.config(['$routeProvider',
  function($routeProvider) {
    $routeProvider.
      when('/', {
        templateUrl: 'templates/search.html',
        controller: 'ContentController'
      }).
      when('/recipe/:recipeid', {
        templateUrl: 'templates/recipe.html',
        controller: 'RecipeController'
      }).
      otherwise({
        redirectTo: '/'
      });
  }]);

App.controller('ContentController', ['$scope', '$http', function($scope, $http) {
    $scope.submitSearch = function() {
        $http.get('/recipe/get/all/' + $scope.searchValue).success(function(data) {
            $scope.searchOptions = data;
        })
    }
    $scope.hitserver = function(id) {
        var url = "/recipe/" + id
        $http.get(url).success(function(data) {
            console.log(data)
        })
    }

}])

App.controller('RecipeController',['$scope', '$routeParams','$http',function($scope, $routeParams, $http){


          var recognition = new webkitSpeechRecognition();
          recognition.continuous = true;
          recognition.interimResults = false;
          recognition.onstart = function() {console.log('Speech Recognition Commencing')}
          recognition.onresult = function(event) {
              for (var i = event.resultIndex; i < event.results.length; ++i) {
                  if (event.results[i].isFinal) {
                    $.ajax({
                        url: 'https://api.wit.ai/message',
                        data: {
                            'q': event.results[i][0].transcript,
                            'access_token': 'SMRYKLMQBVUVUFDAPTPTXLY6H2ZM4DQU'
                        },
                        dataType: 'jsonp',
                        method: 'GET',
                        success: function(response) {
                            console.log("User: ", response._text);
                            var sueMispellings = ["Sue", "Su", "Soup"]
                            if (response.outcomes[0].confidence > 0.3) {
                                $.ajax({
                                    url: '/functions',
                                    data: {
                                        'intent': response.outcomes[0].intent,
                                        'entities': response.outcomes[0].entities,
                                        '_text': response.outcomes[0]._text
                                    },
                                    dataType: 'jsonp',
                                    method: 'GET',
                                    beforeSend: function(x){
                                      var delayPhrases =["Umm.",
                                      "Let me check.",
                                      "One second!",
                                      "Just a sec.",
                                      "Hold on.",
                                      "Gimme a minute",
                                      "Well, you see...",
                                      "Now, let me see.",
                                      "Just a moment.",
                                      "Just a second.",
                                      "Hang on a moment.",
                                      "How shall I put it?",
                                      "What's the word for it..",
                                      "Now, let me think...",
                                      "Let me get this right...",
                                      "It's on the tip of my tongue..",
                                      "Now that's an interesting question..."]

                                      var phrase =  delayPhrases[Math.floor(Math.random() * delayPhrases.length)];

                                      var msg = new SpeechSynthesisUtterance();
                                      msg.rate = 1; // 0.1 to 10
                                      msg.pitch = 2; //0 to 2
                                      msg.text = phrase;
                                      msg.lang = 'en-US';

                                      speechSynthesis.speak(msg);

                                    },
                                    complete: function(response) {
                                        if response.responseText[0] != '<'{
                                        console.log("Sue: ", response.responseText);
                                        var msg = new SpeechSynthesisUtterance();
                                        msg.rate = 1; // 0.1 to 10
                                        msg.pitch = 2; //0 to 2
                                        msg.text = response.responseText;
                                        msg.lang = 'en-US';

                                        speechSynthesis.speak(msg);
                                      } else {
                                        var milliseconds = parseInt(str.slice(1,-1))
                                        setTimeout(function(){
                                          console.log("Sue: ", "Your timer is done!");
                                          var msg = new SpeechSynthesisUtterance();
                                          msg.rate = 1; // 0.1 to 10
                                          msg.pitch = 2; //0 to 2
                                          msg.text = "Your timer is done!"
                                          msg.lang = 'en-US';
                                        },milliseconds)
                                      }


                                    }
                                });
                            }else if (response.outcomes[0].confidence > 0.1){
                              console.log("Sue: ", "What was that?");
                              var msg = new SpeechSynthesisUtterance();
                              msg.rate = 1; // 0.1 to 10
                              msg.pitch = 2; //0 to 2
                              msg.text = "What was that?";
                              msg.lang = 'en-US';

                              speechSynthesis.speak(msg);
                            }
                        }
                    });

                  }
              }
          }
            recognition.lang = 'en-US';
            recognition.start();




}])
