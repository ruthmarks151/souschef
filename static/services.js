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
                                        console.log("Sue: ", response.responseText);
                                        var msg = new SpeechSynthesisUtterance();
                                        msg.text = response.responseText;
                                        msg.lang = 'en-US';
                                        msg.onend = function(e) {
                                          console.log('Finished in ' + event.elapsedTime + ' seconds.');
                                        };
                                        speechSynthesis.speak(msg);
                                    }
                                });
                            }else if (response.outcomes[0].confidence > 0.1){
                              console.log("Sue: ", "What was that?");
                              var msg1 = new SpeechSynthesisUtterance();
                              msg1.text = "What was that?";
                              msg1.lang = 'en-US';

                              speechSynthesis.speak(msg1);
                            }
                        }
                    });

                  }
              }
          }
            recognition.lang = 'en-US';
            recognition.start();
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
        }
    }
});