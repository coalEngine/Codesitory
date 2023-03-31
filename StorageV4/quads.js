alert("Type in values for A, B and C");
function getX()
{
    var a = parseFloat(document.form.a.value);
    var b = parseFloat(document.form.b.value);
    var c = parseFloat(document.form.c.value);
    var x1;
    var x2;
    var discriminant = b * b - 4 * a * c;
        x1 = Math.round(-b - Math.sqrt(discriminant) / 2 * a);
        x2 = Math.round((-b + Math.sqrt(discriminant)) / 2 * a);
    if (discriminant > 0) 
    {
        x1 = (-b + Math.sqrt(discriminant)) / (2 * a);
        x2 = (-b - Math.sqrt(discriminant)) / (2 * a);
    }
    else if (discriminant == 0) 
    {
        x1 = x2 = -b / (2 * a);
    }
    else 
    {
        let realPart = (-b / (2 * a)).toFixed(2);
        let imagPart = (Math.sqrt(-discriminant) / (2 * a)).toFixed(2);
        realPart = x1;
        imagPart = x2;
    }
    document.form.answer.value = x1;
    document.form.answer2.value = x2;
}

 



