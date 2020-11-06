// Redirect
const play          = () => location.href = "/initialization";
const restart       = () => location.href = "/board";
const goHomePage    = () => location.href = "/";

const clickOnCardForReverse = thisCard => {
    let selectedCard = thisCard.getAttribute("data-card");
    let stateImg     = thisCard.getAttribute("src");

    stateImg === "/static/cards/back.png"
        ? stateImg = `/static/cards/${selectedCard}.png`
        : stateImg = `/static/cards/back.png`;

    thisCard.setAttribute("src", stateImg);
}

const checkTime = i => {
    if (i < 10){
        i = "0" + i
    };
    return i;
}

const clock = () => {
    let today = new Date();
    let h = today.getHours();
    let m = today.getMinutes();
    let s = today.getSeconds();

    m = checkTime(m);
    s = checkTime(s);

    document.getElementById('clock').innerHTML = h + ":" + m + ":" + s;
    setTimeout(clock, 500);
  }
