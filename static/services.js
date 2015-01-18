App.factory('speechAPI', function($http){
    return {
        SpeechRecognition: function(){
          var recognition = new webkitSpeechRecognition();
          recognition.continuous = true;
          recognition.interimResults = false;
          recognition.onstart = function() {console.log('Speech Recognition Commencing')}
          recognition.onresult = function(event) {
              for (var i = event.resultIndex; i < event.results.length; ++i) {
                  if (event.results[i].isFinal) {
                    console.log(event.results[i][0].transcript);
                  }
              }
          }
            recognition.lang = 'en-US';
            recognition.start();
        },
        SpeechSynthesis: function(text){
            var msg = new SpeechSynthesisUtterance();
            msg.text = text;
            msg.lang = 'en-US';
            msg.onend = function(e) {
            console.log('Finished in ' + event.elapsedTime + ' seconds.');
            };
            speechSynthesis.speak(msg);
        }
    
    }
});

App.factory('Request',function($http){
    return{
        searchResults: function(searchTerm) {
            return $http.get('/recipe/get/all/' + searchTerm)
        },
        recipeByID: function(id){
            return $http.get("recipe/"+id)
        },
        pretty:function(data){
            data = data.results;
            return{
                time:data.totalTimeInSeconds,
                rating:data.rating,
                servings:data.numberOfServings,
                ingredients:data.ingredientLines,
                picture:data.images[0].hostedLargeUrl,
                name:data.name,
                flavors:data.flavors,
            }
        }
    }
});