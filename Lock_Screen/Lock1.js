const body = document.querySelector("body");

const div = document.createElement("div");
div.setAttribute("class", "container");

const blur = document.createElement("div");
blur.setAttribute("class", "blure");
body.appendChild(div);
div.appendChild(blur);

const display = document.createElement("div");
display.setAttribute("class", "dis");
blur.appendChild(display);

const profile = document.createElement("div");
profile.setAttribute("class", "profile");
display.appendChild(profile);

const a = document.createElement("div");
a.setAttribute("class", "name");
a.textContent=`Admin`
display.appendChild(a);

const input = document.createElement("input");
input.setAttribute("class", "input");
input.setAttribute("type", "password");
input.setAttribute("placeholder", "Enter a Password");
display.appendChild(input);

const forgot = document.createElement("button");
forgot.setAttribute("class", "forget");
forgot.textContent=`Forgot Password?`
display.appendChild(forgot);