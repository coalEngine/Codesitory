imgArray = new Array(4);
imgArray[0] = new Image;
imgArray[0].src = "lions1.gif";
imgArray[1] = new Image;
imgArray[1].src = "tigers1.gif";
imgArray[2] = new Image;
imgArray[2].src = "bears.gif";
imgArray[3] = new Image;
imgArray[3].src = "ohmy.gif";
index = 0; 

function doPrevious()
{
	if(index > 0)
	{
	    index--; 
	    document.slideshow.src = imgArray[index].src;
	}
	return;
}

function doNext() 
{
	if (index < 3) 
	{
		index++;
		document.slideshow.src = imgArray[index].src;
	}
	return;
} 
