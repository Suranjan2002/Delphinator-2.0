/*--------------------------------------------------------------
* PROJECT NAME: DELPHINATOR
* TEAM NAME: THE HACKTIVISTS
* AUTHOR: SAYAK KARAR
--------------------------------------------------------------*/




(function () {
  "use strict";


  /*--------------------------------------------------------------
  # EASY SELECTOR HELPER FUNCTION
  --------------------------------------------------------------*/
  const select = (el, all = false) => {
    el = el.trim()
    if (all) {
      return [...document.querySelectorAll(el)]
    } else {
      return document.querySelector(el)
    }
  }


  /*--------------------------------------------------------------
  # EASY EVENT LISTENER FUNCTION
  --------------------------------------------------------------*/
  const on = (type, el, listener, all = false) => {
    let selectEl = select(el, all)
    if (selectEl) {
      if (all) {
        selectEl.forEach(e => e.addEventListener(type, listener))
      } else {
        selectEl.addEventListener(type, listener)
      }
    }
  }


  /*--------------------------------------------------------------
  # EASY ON SCROLL EVENT LISTENER
  --------------------------------------------------------------*/
  const onscroll = (el, listener) => {
    el.addEventListener('scroll', listener)
  }


  /*--------------------------------------------------------------
  # NAVBAR LINKS ACTIVE STATE ON SCROLL
  --------------------------------------------------------------*/
  let navbarlinks = select('#navbar .scrollto', true)
  const navbarlinksActive = () => {
    let position = window.scrollY + 200
    navbarlinks.forEach(navbarlink => {
      if (!navbarlink.hash) return
      let section = select(navbarlink.hash)
      if (!section) return
      if (position >= section.offsetTop && position <= (section.offsetTop + section.offsetHeight)) {
        navbarlink.classList.add('active')
      } else {
        navbarlink.classList.remove('active')
      }
    })
  }
  window.addEventListener('load', navbarlinksActive)
  onscroll(document, navbarlinksActive)


  /*--------------------------------------------------------------
  # SCROLLS TO AN ELEMENT WITH HEADER OFFSET
  --------------------------------------------------------------*/
  const scrollto = (el) => {
    let header = select('#header')
    let offset = header.offsetHeight

    if (!header.classList.contains('header-scrolled')) {
      offset -= 20
    }

    let elementPos = select(el).offsetTop
    window.scrollTo({
      top: elementPos - offset,
      behavior: 'smooth'
    })
  }


  /*--------------------------------------------------------------
  # TOOGLE .HEADER-SCROLLED CLASS TO #HEADER WHEN PAGE IS SCROLLED
  --------------------------------------------------------------*/
  let selectHeader = select('#header')
  if (selectHeader) {
    const headerScrolled = () => {
      if (window.scrollY > 100) {
        selectHeader.classList.add('header-scrolled')
      } else {
        selectHeader.classList.remove('header-scrolled')
      }
    }
    window.addEventListener('load', headerScrolled)
    onscroll(document, headerScrolled)
  }


  /*--------------------------------------------------------------
  # BACK TO TOP BUTTON
  --------------------------------------------------------------*/
  let backtotop = select('.back-to-top')
  if (backtotop) {
    const toggleBacktotop = () => {
      if (window.scrollY > 100) {
        backtotop.classList.add('active')
      } else {
        backtotop.classList.remove('active')
      }
    }
    window.addEventListener('load', toggleBacktotop)
    onscroll(document, toggleBacktotop)
  }


  /*--------------------------------------------------------------
  # MOBILE NAV TOGGLE
  --------------------------------------------------------------*/
  on('click', '.mobile-nav-toggle', function (e) {
    select('#navbar').classList.toggle('navbar-mobile')
    this.classList.toggle('bi-list')
    this.classList.toggle('bi-x')
  })


  /*--------------------------------------------------------------
  # MOBILE NAV DROPDOWNS ACTIVATE
  --------------------------------------------------------------*/
  on('click', '.navbar .dropdown > a', function (e) {
    if (select('#navbar').classList.contains('navbar-mobile')) {
      e.preventDefault()
      this.nextElementSibling.classList.toggle('dropdown-active')
    }
  }, true)


  /*--------------------------------------------------------------
  # SCROLL WITH OFFSET ON LINKS WITHA CLASS NAME .SCROLLTO
  --------------------------------------------------------------*/
  on('click', '.scrollto', function (e) {
    if (select(this.hash)) {
      e.preventDefault()

      let navbar = select('#navbar')
      if (navbar.classList.contains('navbar-mobile')) {
        navbar.classList.remove('navbar-mobile')
        let navbarToggle = select('.mobile-nav-toggle')
        navbarToggle.classList.toggle('bi-list')
        navbarToggle.classList.toggle('bi-x')
      }
      scrollto(this.hash)
    }
  }, true)


  /*--------------------------------------------------------------
  # SCROLL WITH OFFSET ON PAGE LOAD WITH HASH LINKS IN THE URL
  --------------------------------------------------------------*/
  window.addEventListener('load', () => {
    if (window.location.hash) {
      if (select(window.location.hash)) {
        scrollto(window.location.hash)
      }
    }
  });


  /*--------------------------------------------------------------
  # PRELOADER
  --------------------------------------------------------------*/
  let preloader = select('#preloader');
  if (preloader) {
    window.addEventListener('load', () => {
      preloader.remove()
    });
  }


  /*--------------------------------------------------------------
  # ANIMATION ON SCROLL
  --------------------------------------------------------------*/
  window.addEventListener('load', () => {
    AOS.init({
      duration: 1000,
      easing: 'ease-in-out',
      once: true,
      mirror: false
    })
  });


  /*--------------------------------------------------------------
  # DIGITAL CLOCK
  --------------------------------------------------------------*/
  let clock = select('.footer-newsletter');
  const output = clock.innerHTML;

  const countDownDate = function () {
    let timeleft = new Date(clock.getAttribute('data-count')).getTime() - new Date().getTime();
    var now = new Date();

    var dname = now.getDay(),
      mo = now.getMonth(),
      dnum = now.getDate(),
      yr = now.getFullYear();

    var months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"];

    var days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"];

    var hr = now.getHours();
    var ap = "AM";

    if (hr == 0) {
      hr = 12;
    }
    if (hr > 12) {
      hr = hr - 12;
      ap = "PM";
    }

    Number.prototype.pad = function (digits) {
      for (var n = this.toString(); n.length < digits; n = 0 + n);
      return n;
    }

    let hours = hr.pad(2);
    let minutes = now.getMinutes().pad(2);
    let seconds = now.getSeconds().pad(2);
    clock.innerHTML = output.replace('Day', days[dname]).replace('Month', months[mo]).replace('Date', dnum).replace('Year', yr).replace('00', hours).replace('00', minutes).replace('00', seconds).replace('AM', ap);
  }
  countDownDate();
  setInterval(countDownDate, 1000);


  /*--------------------------------------------------------------
  # VISITORS COUNT
  --------------------------------------------------------------*/
  var url = window.location.href;
  $.getJSON('https://api.gosquared.com/now/v3/pages?api_key=demo&site_token=GSN-106863-S&href=' + encodeURIComponent(url), function (data) {
    $('#online-now').find('.visitors').text(data.visitors);
  });
})()

/*--------------------------------------------------------------
# COPY TO CLIPBOARD
--------------------------------------------------------------*/
function copyToClipBoard(id) {
  var value = document.getElementById(id).innerHTML;
  var input_temp = document.createElement("input");
  input_temp.value = value;
  document.body.appendChild(input_temp);
  input_temp.select();
  document.execCommand("copy");
  document.body.removeChild(input_temp);
}