myImgArray = new Array(4);
myImgArray[0] = new Image;
myImgArray[0].src = "smash64.jfif";
myImgArray[1] = new Image;
myImgArray[1].src = "smashMelee.jfif";
myImgArray[2] = new Image;
myImgArray[2].src = "smashBrawl.jfif";
myImgArray[3] = new Image;
myImgArray[3].src = "smashUlt.jfif";
index = 0; 

SecondImgArray = new Array(4);
SecondImgArray[0] = new Image; 
SecondImgArray[0].src = "zeldaPast.jfif";
SecondImgArray[1] = new Image; 
SecondImgArray[1].src = "zeldaMinish.jfif";
SecondImgArray[2] = new Image;
SecondImgArray[2].src = "zeldaTime.jfif";
SecondImgArray[3] = new Image;
SecondImgArray[3].src = "zeldaNow.jfif";


function cycle()
{
	document.banner1.src = myImgArray[index].src;
	document.banner2.src = SecondImgArray[index].src;
	index++;
	if(index == 4)
	{
		index = 0; 
	}
	setTimeout("cycle()", 2000);
	return;
} 









