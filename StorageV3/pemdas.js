function multiply()
{
	document.form_1.number_3.value = document.form_1.number_1.value * 
		document.form_1.number_2.value;
}

function divide()
{
	var num1 = parseInt(document.form_2.numD_1.value); 
	var num2 = parseInt(document.form_2.numD_2.value);

	document.form_2.numD_3.value = num1 / num2;
}

function add()
{

	var num2 = parseInt(document.form_3.numA_1.value);
	var num1 = parseInt(document.form_3.numA_2.value);

	 document.form_3.numA_3.value = num1 + num2;
}

function subTract()
{
	var num1 = parseInt(document.form_4.numS_1.value);
	var num2 = parseInt(document.form_4.numS_2.value);

	document.form_4.numS_3.value = num1 - num2;
}