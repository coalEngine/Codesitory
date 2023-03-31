imgArray1 = new Array(4)
imgArray1[0] = new Image;
imgArray1[0].src = "shirmp.jfif";
imgArray1[1] = new Image;
imgArray1[1].src =  "pork.jpeg";
imgArray1[2] = new Image; 
imgArray1[2].src = "eggrolls.jpg";
imgArray1[3] = new Image; 
imgArray1[3].src = "chiken.jpg"; 

imgArray2 = new Array(4)
imgArray2[0] = new Image;
imgArray2[0].src = "soup.jpg";
imgArray2[1] = new Image;
imgArray2[1].src = "wonton.jpg";
imgArray2[2] = new Image;
imgArray2[2].src = "vegetablesoup.jpg";
imgArray2[3] = new Image;
imgArray2[3].src = "seafoodsoup.jpg";

imgArray3 = new Array(4)
imgArray3[0] = new Image;
imgArray3[0].src = "beefchow.jpg";
imgArray3[1] = new Image;
imgArray3[1].src = "chickenchow.jpg";
imgArray3[2] = new Image;
imgArray3[2].src = "porkchow.jpg";
imgArray3[3] = new Image;
imgArray3[3].src = "shirmpchow.jpg";

imgArray4 = new Array(4)
imgArray4[0] = new Image;
imgArray4[0].src = "shirmp&rice.jpg";
imgArray4[1] = new Image;
imgArray4[1].src = "beef&rice.jfif";
imgArray4[2] = new Image;
imgArray4[2].src = "pork&rice.jpg";
imgArray4[3] = new Image;
imgArray4[3].src = "chicken&rice.jpg";


index = 0; 

function select()
{
	index = Math.floor(Math.random() * 4);
	document.slides.src = imgArray1[index].src;
	document.slides2.src = imgArray2[index].src;
	document.slides3.src = imgArray3[index].src;
	document.slides4.src = imgArray4[index].src;
	setTimeout("select()", 1000);
	return;
} 