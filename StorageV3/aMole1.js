imgArray = new Array(4);
imgArray[0] = new Image;
imgArray[0].src = "Hole1.png";
imgArray[1] = new Image; 
imgArray[1].src = "Hole2.png";
imgArray[2] = new Image;
imgArray[2].src = "Hole3.png";
imgArray[3] = new Image;
imgArray[3].src = "Mole.png";

index = 0; 
indexTwo = 0;
indexThree = 0; 
indexFour = 0; 
indexFive = 0; 
indexSixth = 0; 
indexSeven = 0; 
indexEight = 0;
indexNine = 0;
var score = 0;

function select()
{
	index = Math.floor(Math.random() * 4);
	indexTwo = Math.floor(Math.random() * 4);;
	indexThree = Math.floor(Math.random() * 4);
	indexFour = Math.floor(Math.random() * 4);
	indexFive = Math.floor(Math.random() * 4);
	indexSixth = Math.floor(Math.random() * 4);
	indexSeven = Math.floor(Math.random() * 4);
	indexEight = Math.floor(Math.random() * 4);
	indexNine = Math.floor(Math.random() * 4);

	document.random_1.src = imgArray[index].src;
	document.random_2.src = imgArray[indexTwo].src;
	document.random_3.src = imgArray[indexThree].src;
	document.random_4.src = imgArray[indexFour].src;
	document.random_5.src = imgArray[indexFive].src;
	document.random_6.src = imgArray[indexSixth].src;
	document.random_7.src = imgArray[indexSeven].src;
	document.random_8.src = imgArray[indexEight].src;
	document.random_9.src = imgArray[indexNine].src;

	setTimeout("select()", 2000);
	return;
} 

