imgArray = new Array(4);
imgArray[0] = new Image;
imgArray[0].src = "pokemonSS1.png";
imgArray[1] = new Image;
imgArray[1].src = "pokemonSS2.png";
imgArray[2] = new Image;
imgArray[2].src = "pokemonSS1.2.png";
imgArray[3] = new Image;
imgArray[3].src = "pokemonSS3.png";

imgArray2 = new Array(4);
imgArray2[0] = new Image;
imgArray2[0].src = "minecraftSS1.png";
imgArray2[1] = new Image;
imgArray2[1].src = "minecraftSS2.png";
imgArray2[2] = new Image;
imgArray2[2].src = "minecraftSS3.png";
imgArray2[3] = new Image;
imgArray2[3].src = "minecraftSS4.png";


imgArray3 = new Array(4);
imgArray3[0] = new Image;
imgArray3[0].src = "tictac1.png";
imgArray3[1] = new Image;
imgArray3[1].src = "tictac2.png";
imgArray3[2] = new Image;
imgArray3[2].src = "tictac3.png";
imgArray3[3] = new Image;
imgArray3[3].src = "tictac4.png";


index = 0;

function cycle()
{
	document.banner1.src = imgArray[index].src;
	document.banner2.src = imgArray2[index].src;
	document.banner3.src = imgArray3[index].src;
	index++;
	if( index == 4)
	{
		index = 0; 
	}
	setTimeout("cycle()", 400);
	return;
} 

