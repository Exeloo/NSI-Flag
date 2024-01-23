
function createQuiz() {
    
    var title = document.createElement('div');
    title.className = 'titleQuiz';

    var text = document.createElement('div');
    text.className = 'textQuiz';

    var questions = document.createElement('div');
    questions.className = 'questionsQuiz';
    questions.id = 'questionsQuiz';

    for (i = 1; i < 6; i++) {
        
        questions.appendChild(createQuestion(i));
    }



    var submit = document.createElement('div');
    submit.className = 'submit';
    submit.id = 'submit'
    submit.innerHTML = '<div class="submitButton">Valider votre réponse</div>';
    submit.onclick = (event) => {
        getAnswer()
    }

    var content = document.getElementById('content');
    if (document.getElementById('questionsQuiz')) {content.removeChild(document.getElementById('questionsQuiz'));}
    if (document.getElementById('score')) {content.removeChild(document.getElementById('score'));}
    content.removeChild(document.getElementById('startQuiz'));
    content.appendChild(title);
    content.appendChild(text);
    content.appendChild(questions);
    content.appendChild(submit);
    
    

}




function createQuestion(i) {
    q = document.createElement('div');
    q.className = 'questionQuiz';
    q.id = 'question' + i;

    var leftPart = document.createElement('div');
    leftPart.className = 'leftQuiz';
    
    var border = document.createElement('div');
    border.className = 'borderImgQuiz'

    var imgLeft = document.createElement('img');
    imgLeft.className = 'flagImgQuiz';

    var rightPart = document.createElement('div');
    rightPart.className = 'rightQuiz';
    
    var formRight = document.createElement('form');
    formRight.className = 'formRightQuiz';
    formRight.id = i;
    axios.get("http://localhost:8000/Flags").then((reponse) => {
        var nb = reponse.data.length
        var nba = getRandom(nb)
        var nbb = getRandom(nb)
        var nbc = getRandom(nb)
        var nbd = getRandom(nb)

        while (nba === nbb) {
            nbb = getRandom(nb)
        }
        while (nba === nbc || nbb === nbc) {
            nbc = getRandom(nb)
        }
        while (nba === nbd || nbb === nbd || nbc === nbd) {
            nbd = getRandom(nb)
        }
        var a = reponse.data[nba].replaceAll('_', ' ');
        var b = reponse.data[nbb].replaceAll('_', ' ');
        var c = reponse.data[nbc].replaceAll('_', ' ');
        var d = reponse.data[nbd].replaceAll('_', ' ');
        var l = new Array(a, b, c, d);

        var rep = getRandom(4);

        for (flag of l) {
            var input = document.createElement('input');
            input.type = 'radio';
            input.name = 'quiz';
            input.id = l.indexOf(flag);
            input.value = l.indexOf(flag);
            input.onclick = (event) => {
                clickRadio(event.currentTarget);
            };

            var label = document.createElement('label');
            label.innerHTML = flag;
            label.className = 'radiocontainer';
            label.id = 'label' + l.indexOf(flag) +  formRight.id;

            var span = document.createElement('span');
            span.className = 'checkmark'


            label.appendChild(input);
            label.appendChild(span);

            formRight.appendChild(label);
            
        }
        flag = l[rep].replaceAll(' ', '_');
        imgLeft.src = 'http://localhost:8000/' + flag;
        imgLeft.id = flag;
        
    });
    border.appendChild(imgLeft)
    leftPart.appendChild(border);
    rightPart.appendChild(formRight);

    q.appendChild(leftPart);
    q.appendChild(rightPart);

    return q;
}


function getRandom(max) {
    return Math.floor(Math.random() * Math.floor(max));
}

function clickRadio(element) {
    var n, i, x;
    n = element.id;
    m = element.parentElement.parentElement.id
    for (i = 0; i < 5; i++) {
        x = document.getElementById("label" + i + m);
        if (x) {
            x.className = x.className.replace(" checkedlabel", "");
            x.lastChild.innerHTML = ''
        }
    }
    document.getElementById("label" + n + m).className += " checkedlabel";
}

function getAnswer() {
    var quiz = document.getElementById('questionsQuiz');
    var points = 0;
    for (q of quiz.getElementsByClassName('questionQuiz')) {
        var flag = q.firstChild.firstChild.firstChild.id;
        var checked = "";
        for (prop of q.lastChild.firstChild.children) {
            if (prop.className.endsWith(' checkedlabel')) {
                checked = prop.innerText

            }
        }
        if (flag === checked) {points += 1}
        
    }
    var score = document.createElement('div');
    score.className = 'score'
    score.id = 'score'
    score.innerText = 'Vous avez un score de ' + points + '/5'

    var start = document.createElement('div');
    start.className = 'startQuiz'
    start.id = 'startQuiz'
    start.onclick = (event) => {
        createQuiz()
    }

    var startButton = document.createElement('div');
    startButton.className = 'startButton'
    startButton.innerText = 'Relancer le Quiz'

    start.appendChild(startButton);

    document.getElementById('content').removeChild(document.getElementById('submit'));
    document.getElementById('content').appendChild(score)
    document.getElementById('content').appendChild(start)
}