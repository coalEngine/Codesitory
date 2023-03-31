imgs = new Array(13);
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
imgs[5] = new Image;
imgs[5].src = "Hole1.png";
imgs[6] = new Image; 
imgs[6].src = "Hole2.png";
imgs[7] = new Image;
imgs[7].src = "Hole3.png";
imgs[8] = new Image;
imgs[8].src = "greenMole.png";
imgs[9] = new Image;
imgs[9].src = "Hole1.png";
imgs[10] = new Image; 
imgs[10].src = "Hole2.png";
imgs[11] = new Image;
imgs[11].src = "Hole3.png";
imgs[12] = new Image;
imgs[12].src = "redMole.png";

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
var finalScore = 0;


time = 61

function select()
{
	index = Math.floor(Math.random() * 13);
	index2 = Math.floor(Math.random() * 13);
	index3 = Math.floor(Math.random() * 13);
	index4 = Math.floor(Math.random() * 13);
	index5 = Math.floor(Math.random() * 13);
	index6 = Math.floor(Math.random() * 13);
	index7 = Math.floor(Math.random() * 13);
	index8 = Math.floor(Math.random() * 13);
	index9 = Math.floor(Math.random() * 13);
	 document.random_1.src = imgs[index].src;
	 document.random_2.src = imgs[index2].src;
	 document.random_3.src = imgs[index3].src;
	 document.random_4.src = imgs[index4].src;
	 document.random_5.src = imgs[index5].src;
	 document.random_6.src = imgs[index6].src;
	 document.random_7.src = imgs[index7].src;
	 document.random_8.src = imgs[index8].src;
	 document.random_9.src = imgs[index9].src;
	time = time - 1;
	if(time <= 0)
	{
		time = 0;
		Stop();
	}
	document.form_1.game_time.value = time;
	setTimeout("select()", 1000);
	return;
} 
function Stop()
{
        index = 1;
        document.random_1.src = imgs[index].src;

        index2 = 1;
        document.random_2.src = imgs[index2].src;

        index3 = 1;
        document.random_3.src = imgs[index3].src;

        index4 = 1;
        document.random_4.src = imgs[index4].src;

        index5= 1;
        document.random_5.src = imgs[index5].src;

        index6 = 1;
        document.random_6.src = imgs[index6].src;

        index7 = 1;
        document.random_7.src = imgs[index7].src;

        index8 = 1;
        document.random_8.src = imgs[index8].src;

        index9 = 1;
        document.random_9.src = imgs[index9].src;
        return;
}



function hit_or_miss()
{
	if(index == 0 || index == 4)
	{
		score = score + 1;
		document.form_1.game_score.value = score;
		index = 1;
		document.random_1.src = imgs[index].src;
		return;
	}
	if(index != 0 && index != 4 && index != 8 && index != 12)
	{
		score = score - 1

		if (time <= 0)
		{
			score = score + 1;
		}
		if(score <= 0)
		{
			score = 0;
		}	
		document.form_1.game_score.value = score;
		return;
	}
	if(index == 8)
	{
		score = score + 5; 
		document.form_1.game_score.value = score;
		index = 1;
		document.random_1.src = imgs[index].src;
		return;	
	}
	if(index == 12)
	{
		score = score - 5;
		if(score <= 0)
		{
			score = 0;
		}	
		document.form_1.game_score.value = score;
		index = 1;
		document.random_1.src = imgs[index].src;
		return;	
	}	
}
function hit_or_miss2()
{
	if(index2 == 0 || index2 == 4)
	{
		score = score + 1;
		document.form_1.game_score.value = score;
		index2 = 1;
		document.random_2.src = imgs[index2].src;
		return;
	}
	if(index2 != 0 && index2 != 4 && index2 != 8 && index2 != 12)
	{
		score = score - 1

		if (time <= 0)
		{
			score = score + 1;
		}

		if(score <= 0)
		{
			score = 0;
		}	
		document.form_1.game_score.value = score;
		return;
	}
	if(index2 == 8)
	{
		score = score + 5; 
		document.form_1.game_score.value = score;
		index2 = 1;
		document.random_2.src = imgs[index2].src;
		return;	
	}
	if(index2 == 12)
	{
		score = score - 5;
		if(score <= 0)
		{	
			score = 0;
		}	
		document.form_1.game_score.value = score;
		index2 = 1;
		document.random_2.src = imgs[index2].src;
		return;	
	}	
}
function hit_or_miss3()
{
	if(index3 == 0 || index3 == 4)
	{
		score = score + 1;
		document.form_1.game_score.value = score;
		index3 = 1;
		document.random_3.src = imgs[index3].src;
		return;
	}
	if(index3 != 0 && index3 != 4 && index3 != 8 && index3 != 12)
	{
		score = score - 1

		if (time <= 0)
		{
			score = score + 1;
		}
		if(score <= 0)
		{
			score = 0;
		}	
		document.form_1.game_score.value = score;
		return;
	}
	if(index3 == 8)
	{
		score = score + 5; 
		document.form_1.game_score.value = score;
		index3 = 1;
		document.random_3.src = imgs[index3].src;
		return;	
	}
	if(index3 == 12)
	{
		score = score - 5;
		if(score <= 0)
		{
			score = 0;
		}	
		document.form_1.game_score.value = score;
		index3 = 1;
		document.random_3.src = imgs[index3].src;
		return;	
	}		
}

function hit_or_miss4()
{
	if(index4 == 0 || index4 == 4)
	{
		score = score + 1;
		document.form_1.game_score.value = score;
		index4 = 1;
		document.random_4.src = imgs[index4].src;
		return;
	}
	if(index4 != 0 && index4 != 4 && index4 != 8 && index4 != 12)
	{
		score = score - 1

		if (time <= 0)
		{
			score = score + 1;
		}
		if(score <= 0)
		{
			score = 0;
		}	
		document.form_1.game_score.value = score;
		return;
	}
	if(index4 == 8)
	{
		score = score + 5; 
		document.form_1.game_score.value = score;
		index4 = 1;
		document.random_4.src = imgs[index4].src;
		return;	
	}
	if(index4 == 12)
	{
		score = score - 5;
		if(score <= 0)
		{
			score = 0;
		}	
		document.form_1.game_score.value = score;
		index4 = 1;
		document.random_4.src = imgs[index4].src;
		return;	
	}			
}
function hit_or_miss5()
{
	if(index5 == 0 || index5 == 4)
	{
		score = score + 1;
		document.form_1.game_score.value = score;
		index5 = 1;
		document.random_5.src = imgs[index5].src;
		return;
	}
	if(index5 != 0 && index5 != 4 && index5 != 8 && index5 != 12)
	{
		score = score - 1

		if (time <= 0)
		{
			score = score + 1;
		}
		if(score <= 0)
		{
			score = 0;
		}	
		document.form_1.game_score.value = score;
		return;
	}
	if(index5 == 8)
	{
		score = score + 5; 
		document.form_1.game_score.value = score;
		index5 = 1;
		document.random_5.src = imgs[index5].src;
		return;	
	}
	if(index5 == 12)
	{
		score = score - 5;
		if(score <= 0)
		{
			score = 0;
		}	 
		document.form_1.game_score.value = score;
		index5 = 1;
		document.random_5.src = imgs[index5].src;
		return;	
	}	
}
function hit_or_miss6()
{
	if(index6 == 0 || index6 == 4)
	{
		score = score + 1;
		document.form_1.game_score.value = score;
		index6 = 1;
		document.random_6.src = imgs[index6].src;
		return;
	}
	if(index6 != 0 && index6 != 4 && index6 != 8 && index6 != 12)
	{
		score = score - 1

		if (time <= 0)
		{
			score = score + 1;
		}
		if(score <= 0)
		{
			score = 0;
		}	
		document.form_1.game_score.value = score;
		return;
	}
	if(index6 == 8)
	{
		score = score + 5; 
		document.form_1.game_score.value = score;
		index6 = 1;
		document.random_6.src = imgs[index6].src;
		return;	
	}
	if(index6 == 12)
	{
		score = score - 5;
		if(score <= 0)
		{
			score = 0;
		}	
		document.form_1.game_score.value = score;
		index6 = 1;
		document.random_6.src = imgs[index6].src;
		return;	
	}	
}
function hit_or_miss7()
{
	if(index7 == 0 || index7 == 4)
	{
		score = score + 1;
		document.form_1.game_score.value = score;
		index7 = 1;
		document.random_7.src = imgs[index7].src;
		return;
	}
	if(index7 != 0 && index7 != 4 && index7 != 8 && index7 != 12)
	{
		score = score - 1

		if (time <= 0)
		{
			score = score + 1;
		}
		if(score <= 0)
		{
			score = 0;
		}	
		document.form_1.game_score.value = score;
		return;
	}
	if(index7 == 8)
	{
		score = score + 5; 
		document.form_1.game_score.value = score;
		index7 = 1;
		document.random_7.src = imgs[index7].src;
		return;	
	}
	if(index7 == 12)
	{
		score = score - 5 
		if(score <= 0)
		{
			score = 0;
		}	
		document.form_1.game_score.value = score;
		index7 = 1;
		document.random_7.src = imgs[index7].src;
		return;	
	}
	
}
function hit_or_miss8()
{
	if(index8 == 0 || index8 == 4)
	{
		score = score + 1;
		document.form_1.game_score.value = score;
		index8 = 1;
		document.random_8.src = imgs[index8].src;
		return;
	}
	if(index8 != 0 && index8 != 4 && index8 != 8 && index8 != 12)
	{
		score = score - 1

		if (time <= 0)
		{
			score = score + 1;
		}
		if(score <= 0)
		{
			score = 0;
		}	
		document.form_1.game_score.value = score;
		return;
	}
	if(index8 == 8)
	{
		score = score + 5; 
		document.form_1.game_score.value = score;
		index8 = 1;
		document.random_8.src = imgs[index8].src;
		return;	
	}
	if(index8 == 12)
	{
		score = score - 5;
		if(score <= 0)
		{
			score = 0;
		}	
		document.form_1.game_score.value = score;
		index8 = 1;
		document.random_8.src = imgs[index8].src;
		return;	
	}	
}
function hit_or_miss9()
{
	if(index9 == 0 || index9 == 4)
	{
		score = score + 1;
		document.form_1.game_score.value = score;
		index9 = 1;
		document.random_9.src = imgs[index9].src;
		return;
	}
	if(index9 != 0 && index9 != 4 && index9 != 8 && index9 != 12)
	{
		score = score - 1

		if (time <= 0)
		{
			score = score + 1;
		}
		
		if(score <= 0)
		{
			score = 0;
		}	
		document.form_1.game_score.value = score;
		return;
	}
	if(index9 == 8)
	{
		score = score + 5; 
		document.form_1.game_score.value = score;
		index9 = 1;
		document.random_9.src = imgs[index9].src;
		return;	
	}
	if(index9 == 12)
	{
		score = score - 5;
		if(score <= 0)
		{
			score = 0;
		}	
		document.form_1.game_score.value = score;
		index9 = 1;
		document.random_9.src = imgs[index9].src;
		return;	
	}	
}