imgArray = new Array(4);
imgArray[0] = new Image;
imgArray[0].src = "ver1.jfif";
imgArray[1] = new Image;
imgArray[1].src = "ver15.jfif";
imgArray[2] = new Image;
imgArray[2].src = "ver10.jfif";
imgArray[3] = new Image;
imgArray[3].src = "ver17.jpg";

imgArray2 = new Array(4);
imgArray2[0] = new Image;
imgArray2[0].src = "smash64.png"
imgArray2[1] = new Image;
imgArray2[1].src = "melee.jpg"
imgArray2[2] = new Image;
imgArray2[2].src = "smasnWiiU.jpg"
imgArray2[3] = new Image;
imgArray2[3].src = "smashUlt.jpeg"

imgArray3 = new Array(4);
imgArray3[0] = new Image;
imgArray3[0].src = "time.jfif"
imgArray3[1] = new Image;
imgArray3[1].src = "majora.jpg"
imgArray3[2] = new Image;
imgArray3[2].src = "skyward.jpg"
imgArray3[3] = new Image;
imgArray3[3].src = "botw.jpg"
index = 0;




function doPrevious()
{
	if(index > 0)
	{
	    index--;
	    document.slideshow.src = imgArray[index].src;
	}
}



function doNext()
{
	if (index < 9) 
	{
		index++;
		document.slideshow.src = imgArray[index].src;
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

function doPREvious()
{
	if(index > 0)
	{
	    index--;
	    document.slideSHow.src = imgArray3[index].src;
	}
}



function doNEXt()
{
	if (index < 9) 
	{
		index++;
		document.slideSHow.src = imgArray3[index].src;
	}
	return;
} 