document.addEventListener(
  "DOMContentLoaded",
  function () {
    const timer = document.querySelector(".timer");

    const themeButton = document.querySelector(".theme-change");
    const musicButton = document.querySelector(".music-player");
    const testNav = document.querySelector(".test-nav");
    const testLinks = testNav.querySelectorAll(".test-nav-link");
    const testBody = document.querySelector(".test-body");
    const testQuestions = testBody.querySelectorAll(".test-question");
    const nextQuestionButtons = document.querySelectorAll(".next-question-button");

    let count = 15;
    started = false;

    function start() {
      if (started) {
        return;
      }
      let start_time = new Date();
      let stop_time = start_time.setMinutes(start_time.getMinutes() + count);
      let countdown = setInterval(function () {
        let now = new Date().getTime();
        let remain = stop_time - now;
        let min = Math.floor((remain % (1000 * 60 * 60)) / (1000 * 60));
        let sec = Math.floor((remain % (1000 * 60)) / 1000);
        sec = sec < 10 ? "0" + sec : sec;
        timer.innerHTML = min + ":" + sec;
        if (remain < 0) {
          clearInterval(countdown);
          timer.innerHTML = "Всё!";
        }
      }, 1000);
      started = true;
    }
    start();

    const removeActiveStyles = function () {
      testLinks.forEach((lnk) => {
        lnk.classList.remove("active-link");
      });
      testQuestions.forEach((question) => {
        question.classList.add("question-hide");
      });
    };

    nextQuestionButtons.forEach((button) => {
      button.addEventListener("click", (event) => {
        event.preventDefault();
        removeActiveStyles();
        let index = parseInt(event.target.parentNode.dataset.id) + 1;
        testLinks[index - 1].classList.add("test-link-success");
        testLinks[index - 1].classList.add("test-link-good");
        testLinks[index].classList.add("active-link");
        testQuestions[index].classList.remove("question-hide");
      });
    });

    if (localStorage.getItem("light-theme") === "true") {
      document.body.classList.add("light-theme");
    }
    themeButton.addEventListener("click", (event) => {
      event.preventDefault();
      document.body.classList.toggle("light-theme");
      let flag = document.body.classList.contains("light-theme");
      localStorage.setItem("light-theme", flag);
    });

    if (localStorage.getItem("current-question")) {
      removeActiveStyles();
      testQuestions[localStorage.getItem("current-question")].classList.remove("question-hide");

      testLinks[localStorage.getItem("current-question")].classList.add("active-link");
    } else {
      testLinks[0].classList.add("active-link");
      testQuestions[0].classList.remove("question-hide");
    }

    testLinks.forEach((link) => {
      link.addEventListener("click", (event) => {
        event.preventDefault();
        let index = parseInt(event.target.dataset.id);
        localStorage.setItem("current-question", index);

        removeActiveStyles();
        link.classList.add("active-link");

        testQuestions[index].classList.remove("question-hide");
      });
    });
  },
  false
);

$(function () {
  $(".sortable-container").sortable();
});

$(function () {
  $(".relations-drag-elements").sortable();
});
