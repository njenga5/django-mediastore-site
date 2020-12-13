const row1 = document.getElementById("row1");
const row2 = document.getElementById("row2");
const row3 = document.getElementById("row3");
const row4 = document.getElementById("row4");

//first row

const div_id_first_name = document.getElementById("div_id_first_name");
const div_id_middle_name = document.getElementById("div_id_middle_name");

const div = document.createElement("div");
div.textContent = "Invalid first name";
div.classList.add("invalid-feedback");

div_id_first_name.appendChild(div);
div_id_first_name.classList.add("col-md-6");
div_id_middle_name.classList.add("col-md-6");

row1.appendChild(div_id_first_name);
row1.appendChild(div_id_middle_name);

//second row

const div_id_last_name = document.getElementById("div_id_last_name");
const div_id_phone_number = document.getElementById("div_id_phone_number");

div_id_last_name.classList.add("col-md-6");
div_id_phone_number.classList.add("col-md-6");

row2.appendChild(div_id_last_name);
row2.appendChild(div_id_phone_number);

//third row

const div_id_email = document.getElementById("div_id_email");
const div_id_date_of_birth = document.getElementById("div_id_date_of_birth");

div_id_email.classList.add("col-md-6");
div_id_date_of_birth.classList.add("col-md-4");

row3.appendChild(div_id_email);
row3.appendChild(div_id_date_of_birth);
