function calculate(){
    var base = parseFloat(document.form_1.Base.value);
    var exponent = parseFloat(document.form_1.Exponent.value);
    var answer;

        answer = Math.pow(base, exponent);
        document.form_1.Answer.value = answer; 
}