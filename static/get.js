         
        function getBotResponse(){
            var rawText = $("#textInput").val();
            var userHtml = '<p class = "userText"><span>' + rawText + '</span></p>';
            $("#textInput").val("");
            $("#chatbox").append(userHtml);
            document.getElementById('userInput').scrollIntoView({block:'start',behaviour:'smooth'});
            $.get("/get", {msg:rawText }).done(function(data) {
            var botHtml = '<p class ="botText"><span>' + data + '</span></p>';
            $("#chatbox").append(botHtml);

            document.getElementById('userInput').scrollIntoView({block : 'start',behaviour:'smooth'});
            document.getElementById("chatbox").scrollBy(0, 2000);

            });
        }

        $("#textInput").keypress(function(e) {
        if(e.which == 13) {
        getBotResponse();
        document.getElementById("chatbox").scrollBy(0, 2000);
        }
        });
        $("#buttonInput").click(function() {
        getBotResponse();
        })