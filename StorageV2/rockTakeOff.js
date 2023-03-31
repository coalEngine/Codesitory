imgArray = new Array(18);
imgArray[0] = new Image;
imgArray[0].src = "rocketTakeoff.jpg"; 
imgArray[1] = new Image;
imgArray[1].src = "rockettakeOff2.jpg";
imgArray[2] = new Image;
imgArray[2].src = "rockettakeOff3.jpg";
imgArray[3] = new Image;
imgArray[3].src = "rockettakeOff4.jpg";
imgArray[4] = new Image;
imgArray[4].src = "rockettakeOff5.jpg";
imgArray[5] = new Image;
imgArray[5].src = "rockettakeOff6.jpg";
imgArray[6] = new Image;
imgArray[6].src = "rockettakeOff7.jpg";
imgArray[7] = new Image;
imgArray[7].src = "rockettakeOff8.jpg";
imgArray[8] = new Image;
imgArray[8].src = "rockettakeOff9.jpg";
imgArray[9] = new Image;
imgArray[9].src = "rockettakeOff10.jpg";
imgArray[10] = new Image;
imgArray[10].src = "rockettakeOff11.jpg";
imgArray[11] = new Image;
imgArray[11].src = "rockettakeOff12.jpg";
imgArray[12] = new Image;
imgArray[12].src = "rockettakeOff13.jpg";
imgArray[13] = new Image;
imgArray[13].src = "rockettakeOff14.jpg";
imgArray[14] = new Image;
imgArray[14].src = "rockettakeOff15.jpg";
imgArray[15] = new Image;
imgArray[15].src = "rockettakeOff16.jpg";
imgArray[16] = new Image;
imgArray[16].src = "rockettakeOff17.jpg";
imgArray[17] = new Image;
imgArray[17].src = "rockettakeOff18.jpg";
index = 0;

function cycle()
{
	document.banner.src = imgArray[index].src;
	index++;
	if(index == 18)
	{
	   	index = 0;
	}
	setTimeout("cycle()", 1000);
	return;
} 