imgs = new Array(5);
imgs[0] = new Image;
imgs[0].src = "Mole.png";
imgs[1] = new Image;
imgs[1].src = "Hole1.png";
imgs[2] = new Image; 
imgs[2].src = "Hole2.png";
imgs[3] = new Image;
imgs[3].src = "Hole3.png";
imgs[4] = new Image;
imgs[4].src = "Mole.png";

index = 0; 
index2 = 0;
index3 = 0; 
index4 = 0; 
index5 = 0; 
index6 = 0;
index7 = 0;
index8 = 0;
index9 = 0;

var score = 0;

function select()
{
	index = Math.floor(Math.random() * 5);
	index2 = Math.floor(Math.random() * 5);
	index3 = Math.floor(Math.random() * 5);
	index4 = Math.floor(Math.random() * 5);
	index5 = Math.floor(Math.random() * 5);
	index6 = Math.floor(Math.random() * 5);
	index7 = Math.floor(Math.random() * 5);
	index8 = Math.floor(Math.random() * 5);
	index9 = Math.floor(Math.random() * 5);
	 document.random_1.src = imgs[index].src;
	 document.random_2.src = imgs[index2].src;
	 document.random_3.src = imgs[index3].src;
	 document.random_4.src = imgs[index4].src;
	 document.random_5.src = imgs[index5].src;
	 document.random_6.src = imgs[index6].src;
	 document.random_7.src = imgs[index7].src;
	 document.random_8.src = imgs[index8].src;
	 document.random_9.src = imgs[index9].src;
	setTimeout("select()", 2000);
	return;
} 


function hit_or_miss()
{
	if(index == 0 || index == 4)
	{
		score++;
		document.form_1.game_score.value = score;
		return;
	}
	if(index != 0 && index != 4)
	{
		score--;
		document.form_1.game_score.value = score;
		return;
	}
		
}

function hit_or_miss2()
{
	if(index2 == 0 || index2 == 4)
	{
		score++;
		document.form_1.game_score.value = score;
		return;
	}
	if(index2 != 0 && index2 != 4)
	{
		score--;
		document.form_1.game_score.value = score;
		return;
	}
		
}

function hit_or_miss3()
{
	if(index3 == 0 || index3 == 4)
	{
		score++;
		document.form_1.game_score.value = score;
		return;
	}
	if(index3 != 0 && index3 != 4)
	{
		score--;
		document.form_1.game_score.value = score;
		return;
	}
}

function hit_or_miss4()
{
	if(index4 == 0 || index4 == 4)
	{
		score++;
		document.form_1.game_score.value = score;
		return;
	}
	if(index4 != 0 && index4 != 4)
	{
		score--;
		document.form_1.game_score.value = score;
		return;
	}
		
}
function hit_or_miss5()
{
	if(index5 == 0 || index5 == 4)
	{
		score++;
		document.form_1.game_score.value = score;
		return;
	}
	if(index5 != 0 && index5 != 4)
	{
		score--;
		document.form_1.game_score.value = score;
		return;
	}
		
}
function hit_or_miss6()
{
	if(index6 == 0 || index6 == 4)
	{
		score++;
		document.form_1.game_score.value = score;
		return;
	}
	if(index6 != 0 && index6 != 4)
	{
		score--;
		document.form_1.game_score.value = score;
		return;
	}
		
}
function hit_or_miss7()
{
	if(index7 == 0 || index7 == 4)
	{
		score++;
		document.form_1.game_score.value = score;
		return;
	}
	if(index7 != 0 && index7 != 4)
	{
		score--;
		document.form_1.game_score.value = score;
		return;
	}
		
}
function hit_or_miss8()
{
	if(index8 == 0 || index8 == 4)
	{
		score++;
		document.form_1.game_score.value = score;
		return;
	}
	if(index8 != 0 && index8 != 4)
	{
		score--;
		document.form_1.game_score.value = score;
		return;
	}
		
}
function hit_or_miss9()
{
	if(index9 == 0 || index9 == 4)
	{
		score++;
		document.form_1.game_score.value = score;
		return;
	}
	if(index9 != 0 && index9 != 4)
	{
		score--;
		document.form_1.game_score.value = score;
		return;
	}
		
}