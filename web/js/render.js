var render = {

	allQuotes: function(data){
		for(var i=0; i<data.length; i++){
			var renderedQuote = "<div id="+data[i]+" class='quote'>"+(i+1)+"</div>";
			$("#quotesContainer").append(renderedQuote)
		}
	},

	quote: function(data){
		$("#quote").html("");
		$("#quote").append('<div class="quoteText">'+data['text']+'</div>');
		var people = data['characters'].sort()
		var renderedQuote = "<div class='quoteAnswers'>"
		for(var i=0;i<people.length; i++){
			renderedQuote += '<div class="quoteAnswer"><div class="quoteLabel">'+people[i]+'</div>';
			renderedQuote += '<input type="text" placeholder="Enter Value Here" id="inputBox'+i+'" class="quoteInput"/></div>';
		}
		renderedQuote += '<button id="closeBtn">X</button>';
		renderedQuote += '<button id="submitBtn">SUBMIT</button>';
		renderedQuote += "</div>"
		$("#quote").append(renderedQuote);
	},

	displayResult: function(result) {
		if(!result) {
			$(".correctAnswer").hide();
			var incorrectAnswer = "<div class='incorrectAnswer'>"
			incorrectAnswer += '<div id="failureText">INCORRECT ANSWER</div>';
			incorrectAnswer += '<button id="tryAgainBtn">Try Again</button>';
			incorrectAnswer += "</div>"
			$(".quoteAnswers").append(incorrectAnswer);
			$(".incorrectAnswer").show();
		}
		else {
			$(".incorrectAnswer").hide();
			var correctAnswer = "<div class='correctAnswer'>"
			correctAnswer += '<div id="successText">CORRECT ANSWER!!!</div>';
			$(".quoteAnswers").append(correctAnswer);
			$(".correctAnswer").show();
		}
	}
}