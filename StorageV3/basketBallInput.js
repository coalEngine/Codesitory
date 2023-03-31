var bounces = prompt("How many times do you want it to bounce?", " ") ; 
var speed =prompt("Enter the amount of milliseconds you want the program to run?", " ");

imgArray = new Array(7);
imgArray[0] = new Image;
imgArray[0].src = "basketball1.gif";
imgArray[1] = new Image;
imgArray[1].src = "basketball2.gif";
imgArray[2] = new Image;
imgArray[2].src = "basketball3.gif";
imgArray[3] = new Image;
imgArray[3].src = "basketball4.gif";
imgArray[4] = new Image;
imgArray[4].src = "basketball5.gif";
imgArray[5] = new Image;
imgArray[5].src = "basketball6.gif";
imgArray[6] = new Image;
imgArray[6].src = "basketball7.gif";

index = 0;
counter = 0;

counter2 = 0;

function bounce()
{
	document.banner.src = imgArray[index].src;
	if(counter2 < bounces)
	{	
		setTimeout("bounce()", speed);
	}
	counter++;
	if (counter < 7)
	{
		index++;
	}
	if (counter >= 7)
	{
		index--;
	}
	if (counter == 12)
	{
		index = 0;
		counter = 0;
		counter2++;
	}
}
