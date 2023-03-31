imgArray = new Array(10);
imgArray[0] = new Image;
imgArray[0].src = "euclid.png";
imgArray[1] = new Image;
imgArray[1].src = "pythag.png";
imgArray[2] = new Image;
imgArray[2].src = "leonardo.png";
imgArray[3] = new Image;
imgArray[3].src = "rene.png";
imgArray[4] = new Image
imgArray[4].src = "pierre.png"; 
imgArray[5] = new Image;
imgArray[5].src = "blaise.png";
imgArray[6] = new Image;
imgArray[6].src = "newton.png"; 
imgArray[7] = new Image;
imgArray[7].src = "leibniz.png"; 
imgArray[8] = new Image;
imgArray[8].src = "leonhard.png"; 
imgArray[9] = new Image;
imgArray[9].src = "karl.png"; 

imgArray2 = new Array(4);
imgArray2[0] = new Image;
imgArray2[0].src = "smash64.png"
imgArray2[1] = new Image;
imgArray2[1].src = "smash64.png"
imgArray2[2] = new Image;
imgArray2[2].src = "smash64.png"
imgArray2[3] = new Image;
imgArray2[3].src = "smash64.png"
index = 0;





function doPrevious()
{
	if(index > 0)
	{
	    index--;
	    document.slideshow.src = imgArray[index].src;
	    document.slideShow.src = imgArray2[index].src;
	}
}



function doNext()
{
	if (index < 9) 
	{
		index++;
		document.slideshow.src = imgArray[index].src;
		document.slideShow.src = imgArray2[index].src;
	}
	return;
} 

function doPRevious()
{
	if(index > 0)
	{
	    index--;
	    document.slideShow.src = imgArray2[index].src;
	}
}



function doNExt()
{
	if (index < 9) 
	{
		index++;
		document.slideShow.src = imgArray2[index].src;
	}
	return;
} 