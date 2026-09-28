document.addEventListener("DOMContentLoaded", function () {
  // Mobile menu toggle
  var menuBtn = document.getElementById("menuBtn");
  var mnav = document.getElementById("mnav");
  if (menuBtn && mnav) {
    menuBtn.addEventListener("click", function () {
      mnav.classList.toggle("open");
    });
    // close the mobile menu after tapping a link
    mnav.querySelectorAll("a").forEach(function (link) {
      link.addEventListener("click", function () {
        mnav.classList.remove("open");
      });
    });
  }

  // Footer year
  var yearEl = document.getElementById("yr");
  if (yearEl) {
    yearEl.textContent = new Date().getFullYear();
  }

  // FAQ accordion
  document.querySelectorAll(".faq-question").forEach(function (btn) {
    btn.addEventListener("click", function () {
      var expanded = btn.getAttribute("aria-expanded") === "true";
      var answer = btn.nextElementSibling;
      btn.setAttribute("aria-expanded", String(!expanded));
      if (answer) {
        answer.style.maxHeight = expanded ? "0px" : answer.scrollHeight + "px";
      }
    });
  });

  // Scroll-reveal: fade/slide sections in as they enter the viewport
  var revealEls = document.querySelectorAll(".reveal");
  if ("IntersectionObserver" in window && revealEls.length) {
    var observer = new IntersectionObserver(
      function (entries) {
        entries.forEach(function (entry) {
          if (entry.isIntersecting) {
            entry.target.classList.add("in-view");
            observer.unobserve(entry.target);
          }
        });
      },
      { threshold: 0.12 }
    );
    revealEls.forEach(function (el) {
      observer.observe(el);
    });
  } else {
    // no IntersectionObserver support — just show everything
    revealEls.forEach(function (el) {
      el.classList.add("in-view");
    });
  }
});
