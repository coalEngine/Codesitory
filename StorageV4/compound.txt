alert("Enter In Values in values for the Compound Interest Equation")
function comp()
{
    var trueAmoun;
    var p = parseFloat(document.form.p.value);
    var r= parseFloat(document.form.r.value);
    var n = parseFloat(document.form.n.value);
    var t = parseFloat(document.form.t.value);

    var trueRate = r / n;
    var trueTime = n * t;
   
        trueAmoun = Math.round(p * (Math.pow((1 + (trueRate)), (trueTime))));
        

   document.form.Amount.value = trueAmoun;
}