const row1 = document.getElementById("row1");
const row2 = document.getElementById("row2");


//first row

const div_id_full_name = document.getElementById("div_id_full_name");
div_id_full_name.classList.add("col-md-6");
const div_id_email = document.getElementById("div_id_email");
div_id_email.classList.add("col-md-6");


row1.appendChild(div_id_full_name);
row1.appendChild(div_id_email);

//second row


const div_id_phone_number = document.getElementById("div_id_phone_number");
div_id_phone_number.classList.add("col-md-12");

row2.appendChild(div_id_phone_number);


