imgArray = new Array(4);
imgArray[0] = new Image;
imgArray[0].src = "lions.gif";
imgArray[1] = new Image; 
imgArray[1].src = "tigers.gif";
imgArray[2] = new Image;
imgArray[2].src = "bears.gif";
imgArray[3] = new Image;
imgArray[3].src = "ohmy.gif";
index = 0; 

function cycle()
{

	document.banner.src = imgArray[index].src;
	index++;
	if( index == 4)
	{
		index = 0; 
	}
	setTimeout("cycle()", 2000);
	return;
} 