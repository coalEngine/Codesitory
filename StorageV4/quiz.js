function Grade(){
    grade = 0;
    if (document.Quiz.Q1[1].checked)
    {
        alert("Question 1 Is Correct!")
        grade = grade + 1;
    }
    else
    {
        alert("Question 1 is Wrong!")
    }

    if (document.Quiz.Q2[0].checked)
    {
        alert("Question 2 Is Correct!")
        grade = grade + 1;
    }
    else
    {
        alert("Question 2 is Wrong!")
    }

    if (document.Quiz.Q3[0].checked)
    {
        alert("Question 3 Is Correct!")
        grade = grade + 1;
    }
    else
    {
        alert("Question 3 is Wrong!")
    }

    if (document.Quiz.Q4[0].checked)
    {
        alert("Question 4 Is Correct!")
        grade = grade + 1;
    }
    else{
        alert("Question 4 is Wrong!")
    }

    if (document.Quiz.Q5[0].checked)
    {
        alert("Question 5 Is Correct!")
        grade = grade + 1;
    }
    else{
        alert("Question 5 is Wrong!")
    }
}