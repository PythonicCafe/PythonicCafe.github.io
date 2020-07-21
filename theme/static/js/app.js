//Show and hide hamburguer menu in small screens 
const menu = document.getElementById("menu");
const ulMenu = document.getElementById("ulMenu");

function menuToggle() {
    menu.classList.toggle('h-48')
}

// Browser resize listener
window.addEventListener("resize", menuResize);

// Rezise menu if user changing the width with responsive menu opened
function menuResize() {
    // first get the size from the window
    const window_size = window.innerWidth || document.body.clientWidth;
    if (window_size > 640) {
        menu.classList.remove('h-48');
    }
}

// Adding email obfuscated
const em = '\u0063\u006f\u006e\u0074\u0061\u0074\u006f\u0040\u0070\u0079\u0074\u0068\u006f\u006e\u0069\u0063\u002e\u0063\u0061\u0066\u0065';

document.getElementById('email').innerHTML += `<a href="mailto:${em}" class="btn bg-white text-gray-700 mt-3 rounded-full hover:bg-gray-500` +
    `hover:text-gray-100 hover:scale-125 transform transition duration-500">Enviar e-mail</a>`;
