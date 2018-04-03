$(document).ready(main);

function main(){
	api.getQuotes(gotAllQuotes);
}

function gotAllQuotes(data){
	render.allQuotes(data)
	for(var i=0; i<data.length; i++){
		$("#"+data[i]).click(function(){
			api.getQuote(this.id, gotQuote);
		});
	}
}

function gotQuote(quote){
	render.quote(quote);
	$("#quote").show();
	$("#closeBtn").click(function() {
		$("#quote").hide();
	});
	$("#submitBtn").click(function() {
		var characterNames = [];
		var userAnswers = getUserAnswer(quote.characters.length);
		for(var i=0; i<quote.characters.length; i++) {
			api.getCharacter(quote.quoteID, quote.characters[i], userAnswers, characterNames, checkAnswer);
		}	
	});	
}

function getUserAnswer(numberOfTextBoxes) {
	var userAnswers = [];
	for(var i=0; i<numberOfTextBoxes; i++) {
		userAnswers.push($("#inputBox"+i).val());
	}
	return userAnswers;
}

function clearUserAnswers(userAnswers) {
	for(var i=0; i<userAnswers.length; i++) {
		$("#inputBox"+i).val('');
	}
}

function checkAnswer(userAnswers, characterNames) {
	var result = true;
	for(var i=0; i<userAnswers.length; i++) {
		if(characterNames[i].name.toUpperCase().includes(userAnswers[i].toUpperCase())) {
		}
		else {
			result = false;
		}
	}
	render.displayResult(result);
	
	$("#tryAgainBtn").click(function() {
		clearUserAnswers(userAnswers);
	});
}