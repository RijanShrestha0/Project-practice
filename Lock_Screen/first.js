const body = document.querySelector("body");

const scr = document.createElement("div");
scr.setAttribute("class", "screen");
body.appendChild(scr);

const profile = document.createElement("a");
profile.setAttribute("class", "profile");
profile.setAttribute("href", "Lock.html");
scr.appendChild(profile);

const pic = document.createElement("div");
pic.setAttribute("class", "prof");
profile.appendChild(pic);

const a = document.createElement("div");
a.setAttribute("class", "name");
a.textContent=`25T_Kid`
profile.appendChild(a);

// --------------------------------------------

const scr1 = document.createElement("div");
scr1.setAttribute("class", "screen1");
body.appendChild(scr1);

const profile1 = document.createElement("a");
profile1.setAttribute("class", "profile1");
profile1.setAttribute("href", "Lock1.html")
scr1.appendChild(profile1);

const pic1 = document.createElement("div");
pic1.setAttribute("class", "prof1");
profile1.appendChild(pic1);

const b = document.createElement("div");
b.setAttribute("class", "name1");
b.textContent=`Admin`
profile1.appendChild(b);