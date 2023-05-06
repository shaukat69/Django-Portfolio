var tablinks = document.getElementsByClassName('tab-links');
var tabcontents = document.getElementsByClassName('tab-contents');

// Function For Tabs 
function opentab(tabname){
    for(tablink of tablinks){
        tablink.classList.remove('active-link')
    }
    for(tabcontent of tabcontents){
        tabcontent.classList.remove('active-tab')
    }
    event.currentTarget.classList.add("active-link");

    document.getElementById(tabname).classList.add('active-tab')
}

// Function For Menu 
var sidemenu = document.getElementById('sidemenu');

// Open menu 
function openmenu(){
    sidemenu.style.right = "0"
}

// Close menu 
function closemenu(){
    sidemenu.style.right = "-200px"
}




const scriptURL = 'https://script.google.com/macros/s/AKfycbyQM3EDsIkxS3laK2RrerszIfH47W57HBXEAhpD5LDnWlEQl8pu7e5AebOPxyp6hUVfyg/exec'
const form = document.forms['submit-to-google-sheet']
const msg = document.getElementById('msg');

form.addEventListener('submit', e => {
  e.preventDefault()
  fetch(scriptURL, { method: 'POST', body: new FormData(form)})
    .then(response => {
      msg.innerHTML= "Message Sent Successfully";
      setTimeout(function(){
          msg.innerHTML =""
      },5000)
      form.reset();
    })
    .catch(error => console.error('Error!', error.message))
})