imgArray = new Array(4);
imgArray[0] = new Image;
imgArray[0].src = "lions2.gif";
imgArray[1] = new Image; 
imgArray[1].src = "tigers2.gif";
imgArray[2] = new Image;
imgArray[2].src = "bears2.gif";
imgArray[3] = new Image;
imgArray[3].src = "ohmy2.gif";
index = 0; 

function select()
{
	index = Math.floor(Math.random() * 4);
	document.banner.src = imgArray[index].src;
	setTimeout("select()", 2000);
	return;
} 