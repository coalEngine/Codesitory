function calculate(){ var radicand = parseFloat(document.form.radiCand.value); var answer;

    answer = Math.sqrt(radicand);
    document.form.answer.value = answer;

}