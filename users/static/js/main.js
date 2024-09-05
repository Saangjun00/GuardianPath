/*
    Designed by: SELECTO
    Original image: https://dribbble.com/shots/5311359-Diprella-Login
*/

let switchCtn = document.querySelector("#switch-cnt");
let switchC1 = document.querySelector("#switch-c1");
let switchC2 = document.querySelector("#switch-c2");
let switchCircle = document.querySelectorAll(".switch__circle");
let switchBtn = document.querySelectorAll(".switch-btn");
let aContainer = document.querySelector("#a-container");
let bContainer = document.querySelector("#b-container");
let allButtons = document.querySelectorAll(".submit");

let getButtons = (e) => {

}

let changeForm = (e) => {

    switchCtn.classList.add("is-gx");
    setTimeout(function () {
        switchCtn.classList.remove("is-gx");
    }, 1500)

    switchCtn.classList.toggle("is-txr");
    switchCircle[0].classList.toggle("is-txr");
    switchCircle[1].classList.toggle("is-txr");

    switchC1.classList.toggle("is-hidden");
    switchC2.classList.toggle("is-hidden");
    aContainer.classList.toggle("is-txl");
    bContainer.classList.toggle("is-txl");
    bContainer.classList.toggle("is-z200");
}

let mainF = (e) => {
    for (var i = 0; i < allButtons.length; i++)
        allButtons[i].addEventListener("click", getButtons);
    for (var i = 0; i < switchBtn.length; i++)
        switchBtn[i].addEventListener("click", changeForm)
}

window.addEventListener("load", mainF);

document.addEventListener('DOMContentLoaded', function () {
    var messages = document.querySelectorAll('.messages .alert');
    messages.forEach(function (message) {
        setTimeout(function () {
            message.classList.add('hidden'); // hidden 클래스를 추가하여 opacity를 0으로 만들고, display를 none으로 변경
            setTimeout(function () {
                message.remove(); // 요소를 DOM에서 제거
            }, 1000); // 1초 후에 요소 제거 (transition 시간과 일치하도록 조정)
        }, 3000); // 3초 후에 애니메이션 시작
    });
});