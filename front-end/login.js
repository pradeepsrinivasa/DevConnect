let form =document.getElementById('login-form')



form.addEventListener('submit', (e)=>{
    e.preventDefault()

    let formData={
       'username':form.username.value,
       'password':form.password.value
       
    }
    fetch('http://127.0.0.1:8000/api/users/token/',{
       method:'POST',
       headers:{
              'Content-type':'application/json',
       },
       body:JSON.stringify(formData)
    })
    .then(response => response.json())
    .then(data =>{
       console.log("data:",data.access)
       if(data.access){
        localStorage.setItem("token",data.access)
        window.location='project-list.html'


       }
       else{
              alert('username is not exist')
       }

    })

})