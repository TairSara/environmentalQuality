const questions = [
    {
        index: 1,
        "question": "מרבית הפסולת בחופים היא:",
        "options": ["פלסטיק", "סיגריות", "בקבוקי זכוכית", "מזון"],
        "correctAnswer": "פלסטיק"
    },
    {
        index: 2,
        "question": "מהם יתרונותיו של תהליך המחזור?",
        "options": ["חוסך בחומרי גלם", "מצמצם את עלויות הייצור", "מפחית שימוש באנרגיה", "כל התשובות נכונות"],
        "correctAnswer": "כל התשובות נכונות"
    },
    {
        index: 3,
        "question": "מדוע לוקח לפלסטיק הרבה זמן להתפרק?",
        "options": ["כיוון שמדובר בחומרים שאינם קיימים בטבע", "כיוון שתהליך הייצור שלו לוקח זמן רב", "כיוון שהוא מצריך תנאי חום גבוהים במיוחד", "לפלסטיק לא לוקח זמן רב להתפרק"],
        "correctAnswer": "כיוון שמדובר בחומרים שאינם קיימים בטבע"
    },
    {
        index: 4,
        "question": "פסולת פלסטית בים(כגון חוטים, חבלים, שקים ושקיות) היא הגורם השני בגודלו לפגיעה ב-:",
        "options": ["צבי ים", "כלבי ים", "דגים", "ליוויתנים"],
        "correctAnswer": "צבי ים"
    },
    {
        index: 5,
        "question": "מה אנחנו יכולים לעשות על מנת למחזר?",
        "options": ["להשתמש בשקיות בד", "להפריד פסולת ולשים בפח המתאים", "לצמצם צריכת מוצרים מפלסטיק", "כל התשובות נכונות"],
        "correctAnswer": "כל התשובות נכונות"
    },
    {
        index: 6,
        "question": "מהו תהליך הטמעת הפסולת?",
        "options": ["פעולה בה מטמינים פסולת בבטן האדמה", "פעולה בה מחביאים פסולת מתחת לפחי אשפה", "תהליך בו מטמינים את הפסולת ושורפים אותה", "אף תשובה אינה נכונה"],
        "correctAnswer": "פעולה בה מטמינים פסולת בבטן האדמה"
    },
    {
        index: 7,
        "question": "איזה מחאה מובילה גרטה טונברג?",
        "options": ["בעד טבעונות", "נגד שימוש בכלי דייג שונים", "בעד שריפת אשפה והטמעה", "נגד הזנחת משבר האקלים"],
        "correctAnswer": "נגד הזנחת משבר האקלים"
    },
    {
        index: 8,
        "question": "העיר הזוהמת ביותר בעולם הינה:",
        "options": ["בייג'ינג", "תל אביב", "גורוגראם", "לונדון"],
        "correctAnswer": "גורוגראם"
    },
    {
        index: 9,
        "question": "כמה בקבוקי פלסטיק דרושים על מנת לייצר חולצה?",
        "options": ["77", "5", "1", "12"],
        "correctAnswer": "5"
    },
     {
        index: 10,
        "question": "מהו תהליך המיחזור?",
        "options": ["תהליך בו מפרקים פסולת ומחזירים אותה למצב של חומר גלם, אשר ישמש לייצור מוצרים חדשים", "שינוע של פסולת עירונית אל מתקן מרכזי, ושריפתה בכבשן גבוה בטמפרטורה גבוהה", "פעולה בה מסלקים פסולת, ממיינים אותה ומטמיעים אותה בבטן האדמה", "כל התשובות נכונות"],
        "correctAnswer": "תהליך בו מפרקים פסולת ומחזירים אותה למצב של חומר גלם, אשר ישמש לייצור מוצרים חדשים"
    },
    {
        index: 11,
        "question": "מה משליכים לפח הכתום?",
        "options": ["אריזות פסולת", "בקבוקי פלסטיק", "בגדים", "כל התשובות נכונות"],
        "correctAnswer": "אריזות פסולת"
    },
    {
        index: 12,
        "question": "מהי התכלות?",
        "options": ["תהליך בו החומר ממוחזר", "תהליך שבו החומר מתפרק", "תהליך שבו החומר נשרף", "תהליך שבו החומר נטמן"],
        "correctAnswer": "תהליך שבו החומר מתפרק"
    },
    {
        index: 13,
        "question": "כיצד ניתן להתמודד עם משבר האקלים?",
        "options": ["להעדיף שימוש בתחבורה ציבורית והליכה", "צמצום שימוש בכלים חד פעמיים", "צריכה מופחתת של מוצרים", "כל התשובות נכונות"],
        "correctAnswer": "כל התשובות נכונות"
    },
    {
        index: 14,
        "question": "כוכב הלכת שלנו הוא:",
        "options": ["נוגה", "חמה", "כדור הארץ", "צדק"],
        "correctAnswer": "כדור הארץ"
    },
    {
        index: 15,
        "question": "מהי אנרגיה סולרית?",
        "options": ["אנרגיה המופקת מקרני השמש", "אנרגיה המופקת מאור הירח", "אנרגיה המופקת מרוח", "אנרגיה המופקת ממים"],
        "correctAnswer": "אנרגיה המופקת מקרני השמש"
    },
    {
        index: 16,
        "question": "לאיזה פח נזרוק קרטון חלב ריק?",
        "options": ["פח כתום", "פח ירוק", "פח סגול", "פח חום"],
        "correctAnswer": "פח כתום"
    },
    {
        index: 17,
        "question": "לאיזה פח נזרוק שקית ריקה של במבה?",
        "options": ["פח ירוק", "פח כתום", "פח כחול", "פח סגול"],
        "correctAnswer": "פח כתום"
    },
      {
        index: 18,
        "question": "לאיזה פח נזרוק את קופסת הקורנפלקס?",
        "options": ["פח חום", "פח סגול", "פח כחול", "פח ירוק"],
        "correctAnswer": "פח כחול"
    },
    {
        index: 19,
        "question": "לאיזה פח נזרוק שאריות מהכריך?",
        "options": ["פח חום", "פח ירוק", "פח כתום", "פח אפור"],
        "correctAnswer": "פח חום"
    },
    {
        index:20,
        "question": "אבא קרא את העיתון ועכשיו החליט לזרוק אותו, לאיזה פח נזרוק?",
        "options": ["פח כתום", "פח אפור", "פח כחום", "פח סגול"],
        "correctAnswer": "פח כחול"
    },
    {
        index:21,
        "question": "החולצה של מאיה ישנה מאוד והיא החליטה לזרוק אותה, לאיזה פח נזרוק?",
        "options": ["פח ירוק", "פח כתום", "פח סגול", "פח כחום"],
        "correctAnswer": "פח ירוק"
    },
    {
        index:22,
        "question": "דני סיים לאכול את התפוח, לאיזה פח יזרוק את האשפה?",
        "options": ["פח חום", "פח סגול", "פח כתום", "פח אפור"],
        "correctAnswer": "פח חום"
    },
    {
        index:23,
        "question": "אתמול בשיעור טבע בבית ספר 'שיבולים' שאלה המורה את התלמידים מדוע חשוב למחזר?\nמה לדעתכם ענתה המורה?",
        "options": ["כדי שיהיו פחים צבעוניים שיקשטו את השכונה", "שכל ילד יוכל לבחור את הצבע האהוב עליו ולזרוק בהתאם", "כדי לחסוך בחומרי גלם ולהפחית את כמות הפסולת והזיהום", "משום שזבל שמפיץ ריח רע נאסף לעיתים קרובות יותר"],
        "correctAnswer": "כדי לחסוך בחומרי גלם ולהפחית את כמות הפסולת והזיהום"
    },
    {
        index:24,
        "question": "דני שיחק עם אחיו כדורגל בבית ושבר את האגרטל, דני מיהר לנקות את שברי הזכוכית .\nלאיזה פח נזרוק שברי זכוכית?",
        "options": ["פח ירוק", "פח סגול", "פח חום", "פח כתום"],
        "correctAnswer": "פח סגול"
    },
    {
        index:25,
        "question": "היכן אני אזרוק את מכלי  הצבע הריקים?",
        "options": ["פח סגול", "פח אפור", "פח חום", "פח ירוק"],
        "correctAnswer": "פח אפור"
    },
    {
        index:26,
        "question": "דור העלה שאלה בפני נועה וגיא האם נדרש לנקות את האריזה טרם זריקתה לפח הכתום,נועה טענה כי זה פח ושאנחנו לא מנקים אשפה לפני שזורקים ואילו גיא טען כי חשיבות לזיקת אריזה ללא אשפה?\nנועה טענה כי זה פח ושאנחנו לא מנקים אשפה לפני שזורקים ואילו גיא הסכים עמה והוסיף כי אפשר לשלוף את המזרק הפלסטיקי בקלות ולזרוק את הנייר הפלסטיק מבלי לנקות אותו. מי משניהם צודק ולמה?",
        "options": ["גם נועה וגם דור צודקים כל אחד יעשה כרצונו עם באריזה והמזון שבתוכו", "גם נועה וגם דור טועים ולא זורקים אריזות לפח הכתום זורקים רק שאריות אורגניות", "דור צודק לפח הכתום יש להשליך רק אריזות ריקות ללא שאריות מזון ואילו את שאריות המזון לפח אחר מתאים", "נועה צודקת אשפה מקומה בפח ולא צריך לנקות אותה"],
        "correctAnswer": "דור צודק לפח הכתום יש להשליך רק אריזות ריקות ללא שאריות מזון ואילו את שאריות המזון לפח אחר מתאים"
    },
    {
        index:27,
        "question": "האם אני רשאי לזרוק את פסולת הפחים בבית שלי שלי לפח הסגול?",
        "options": ["לא!", "כן", "לא אם הפח ריק ברובו", "כן, רק אם הפח מלא"],
        "correctAnswer": "לא!"
    },
    {
        index:28,
        "question": "לאן מועברות האריזות הנזרקות בפח הכתום?",
        "options": ["לגני החלדים ליצירת צעצועים לבית הבובות", "בישראל יש 3 תחנות מיון שמטפלות באריזות הפחים הכתומים ושם מתבצעת הפרדה לסוגי החומרים השונים שמגיעים למפעלי מיחזור בארץ וחלקם מעבר לים", "מוטמעים בבטן האדמה", "למפעל שאריזותיו בצבע עתום כמו הפח"],
        "correctAnswer": "בישראל יש 3 תחנות מיון שמטפלות באריזות הפחים הכתומים ושם מתבצעת הפרדה לסוגי החומרים השונים שמגיעים למפעלי מיחזור בארץ וחלקם מעבר לים"
    },
    {
        index:29,
        "question": "מתי מפנים את הפחים הכתומים?",
        "options": ["אחת לחודש", "אחת לשבועיים", "כל יום", " אחת לשבוע"],
        "correctAnswer": "אחת לשבועיים"
    },
    {
        index:30,
        "question": "אספתי בקבוקים למחזר במחזורית לאיסוף בקבוקי פלסטיק.אילו בקבוקים אוכל לשים שם?",
        "options": ["בקבוק שתייה של חצי ליטר עם פקק", "בקבוק שתייה של ליטל וחצי עם פקק", "בקבוק שתייה של ליטר עם פקק", " כל בקבוק פלסטיק"],
        "correctAnswer": "בקבוק שתייה של ליטל וחצי עם פקק"
    },
    {
        index:31,
        "question": "אני רוצה לזרוק את הכיסא עץ הישן שלי, באיזה פח אזרוק אותו?",
        "options": ["פח כתום", "פח סגול", "פח ירוק", "פח אפור"],
        "correctAnswer": "פח ירוק"
    },
    {
        index:32,
        "question": "לאחר שסיימתי להכין את העוגה נדרשתי לזרוק את אריזת הביצים לפח. לאיזה פח אזרוק?",
        "options": ["פח אפור", "פח כחול", "פח כתום", "מתקן לאיסוף קרטונים"],
        "correctAnswer": "פח כחול"
    },
    {
        index:33,
        "question": "בסוף היום הולדת יוסי הלך לזרוק את כל קרטוני הפיצה הריקים בפח, אך לא ידע באיזה פח לזרוק. איזה פח מתאים?",
        "options": ["מתקן לאיסוף קרטונים", "פח כחול", "פח סגול", "פח ירוק"],
        "correctAnswer": "פח כחול"
    },
    {
        index:34,
        "question": "שלילך סיימה לבשל עם בקבוק השמן זית נדרשה לזרוק אותו לפח, איזה פח מתאים?",
        "options": ["פח אפור", "פח סגול", "פח ירוק", "פח טורקיז"],
        "correctAnswer": "פח סגול"
    },
      {
        index:35,
        "question": "הלוחמים בשטח אכלו קופסאות שימורים ובסוף הארוחה נדרשו על ידי המפקד לזרוק את הקופסאות לפח המתאים, מהו הפח המתאים?",
        "options": ["פח ירוק", "פח כתום", "פח סגול", "פח כחול"],
        "correctAnswer": "פח כתום"
    }
  ];

// Finding the HTML element with the unique identifier "questions" and assigning it to the questionsElement variable.
const questionsElement = document.getElementById('questions');
// Finding the HTML element with the unique identifier "results" and assigning it to the resultsElement variable.
const resultsElement = document.getElementById('results');

let currentQuestionIndex = 0;
let correctAnswers = 0;
let totalScore = 0;
const totalQuestions = Math.min(questions.length, 10);
// Shuffle questions array
function shuffleQuestions() {
    for (let i = questions.length - 1; i > 0; i--) {
        const j = Math.floor(Math.random() * (i + 1));
        const temp = questions[i];
        questions[i] = questions[j];
        questions[j] = temp;
    }
}

// Display next question
function displayNextQuestion() {
    if (currentQuestionIndex < totalQuestions) {
        const q = questions[currentQuestionIndex];
        const div = document.createElement('div');
        div.innerHTML = `<p>${currentQuestionIndex + 1}. ${q.question}</p>`;
        q.options.forEach(option => {
            const button = document.createElement('button');
            button.classList.add('answer');
            button.textContent = option;
            button.onclick = () => checkAnswer(option, q.correctAnswer);
            div.appendChild(button);
        });
        questionsElement.innerHTML = '';
        questionsElement.appendChild(div);
    } else {
        displayResults();
    }
}

// Check if answer is correct
function checkAnswer(selectedAnswer, correctAnswer) {
    const selectedButton = event.target;
    if (selectedAnswer === correctAnswer) {
        correctAnswers++; // Add 1 to the correctAnswers
        totalScore += 10; // Add 10 points for correct answer
        selectedButton.classList.add('correct');
    } else {
        selectedButton.classList.add('incorrect');
        // Find the correct answer button and mark it
        const correctButton = Array.from(selectedButton.parentNode.children).find(button => button.textContent === correctAnswer);
        correctButton.classList.add('correct-answer');
    }
    disableButtons();
    currentQuestionIndex++;
    setTimeout(() => {
        displayNextQuestion();
    }, 1500); // Change question after 1.5 seconds
}

// Disable buttons after an answer is selected
function disableButtons() {
    const buttons = document.querySelectorAll('.answer');
    buttons.forEach(button => {
        button.disabled = true;
    });
}

// Display results
function displayResults() {
    resultsElement.innerHTML = `<p>תשובות נכונות: ${correctAnswers} מתוך ${totalQuestions}</p>`;
    resultsElement.innerHTML += `<p>ניקוד סופי: ${totalScore}</p>`;
}

shuffleQuestions();
displayNextQuestion();