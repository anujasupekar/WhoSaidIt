var api = {
	getQuotes: function(callback){
		$.get("/quotes").then(function(data){
			data = JSON.parse(data);
			callback(data);
		});
	},

	getQuote: function(_id, callback){
		$.get("/quotes/"+_id).then(function(data){
			data = JSON.parse(data);
			callback(data);
		});
	},

	getCharacter: function(_id, _personKey, userAnswers, characterNames, callback){
		$.get("/quotes/"+_id+"/"+_personKey).then(function(data){
			data = JSON.parse(data);
			characterNames.push(data);
			if(characterNames.length === userAnswers.length)
				callback(userAnswers, characterNames);
		});
	}
}