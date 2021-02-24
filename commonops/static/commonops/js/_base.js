const fans = document.querySelectorAll('.fan')
fans.forEach(fan => {
    fan.classList.remove('bg-light')
    fan.classList.add(...['bg-dark', 'rounded'])
});

const classNames = ['bg-dark', 'text-white']
try{
  const inputFields = document.querySelectorAll('.form-control')
  inputFields.forEach(field => {
    field.classList.add(...classNames)
    if (field.localName === 'input'){
      field.classList.add('text-center')
    }
  })
  const textArea = document.querySelector('textarea')
  textArea.setAttribute('rows', "5")
}catch(error){

}
const darkToggler = document.getElementById('dark-theme')
const fanDivs = document.querySelectorAll('.fan')
const formFields = document.querySelectorAll('.form-control')
const navBar = document.querySelector('.navbar')
const navLinks = document.querySelectorAll('.nav-link')

const changeTheme = (value) => {
    if (parseInt(value) === 0){

        fanDivs.forEach(div =>{
            div.classList.remove('bg-dark')
            div.classList.add('bg-light')
            document.body.style.backgroundColor = 'antiquewhite'
            document.body.style.color = '#000'
        })


        formFields.forEach(field => {
            field.classList.remove('bg-dark')
            field.classList.add('text-dark')
            field.classList.remove('text-white')
        }) 
        
        darkToggler.style.border = '1px solid antiquewhite'
        navBar.classList.remove(...['navbar-dark', 'bg-dark'])
        navBar.classList.add('bg-light')

        navLinks.forEach(link => {
            link.classList.add('text-dark')
        })

    }else if (parseInt(value) === 1){

        fanDivs.forEach(div => {
            div.classList.remove('bg-light')
            div.classList.add('bg-dark')
            document.body.style.backgroundColor = 'rgb(30, 35, 39, 0.911)'
            document.body.style.color = '#fff'
        })

        formFields.forEach(field => {
            field.classList.add('bg-dark')
            field.classList.remove('text-dark')
            field.classList.add('text-white')
        })

        navBar.classList.add(...['navbar-dark', 'bg-dark'])
        navBar.classList.remove('bg-light')

        navLinks.forEach(link => {
            link.classList.remove('text-dark')
        })
    }
}

const data = localStorage.getItem('dark-theme')
if (data){
    darkToggler.value = data 
    changeTheme(darkToggler.value)
}else{
    changeTheme(1)
}

darkToggler.onchange = (e) => {
    localStorage.setItem('dark-theme', e.target.value)
    changeTheme(e.target.value)
}
