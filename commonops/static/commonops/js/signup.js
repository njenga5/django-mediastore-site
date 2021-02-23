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

const listClasses = ['list-unstyled', 'mb-0']
const list = document.querySelector('ul')
// list.classList.add(...listClasses)

list.childNodes.forEach((child, index) =>{
    const listItem = document.createElement('li')
    const text = child.textContent.split(' ').slice(2).join(' ').replace(
        child.textContent.split(' ').slice(2).join(' ').charAt(0), child.textContent.split(' ').slice(2).join(' ').charAt(0).toUpperCase()
    )
    listItem.innerText = text
    listItem.classList.add('text-info')
    listItem.setAttribute('id', index.toString())
    list.replaceChild(listItem, child)

})
document.getElementById('pass-rules').appendChild(list)


const pass1 = document.getElementById('id_password1')
setInterval(() => {
    if (pass1.value.length > 0 && pass1.value.length < 8){
        // document.getElementById('1').classList.remove('text-info')
        document.getElementById('1').className = 'text-danger'
    }else if(pass1.value.length === 0){
        document.getElementById('1').className = 'text-info'
    }else{
        document.getElementById('1').className = 'text-success'
    }
}, 100)

document.getElementById('id_email').removeAttribute('autofocus')
document.getElementById('id_full_name').focus()

