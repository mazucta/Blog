'use strict'
function showActiveLink(menu) {
    const menuLinks = document.getElementById(menu)
    const links = menuLinks.querySelectorAll('a')
    const url = document.location.href
    for (const link of links) {
        if (link.href === url) {
            link.classList.add("active")
        }
    }
}
showActiveLink('menu')