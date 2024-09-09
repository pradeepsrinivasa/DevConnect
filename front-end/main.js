let loginBtn= document.getElementById('login-btn')
let logoutBtn= document.getElementById('logout-btn')

let token=localStorage.getItem('token')
if(token){
     loginBtn.remove()
}
else{
     logoutBtn.remove()
}

logoutBtn.addEventListener('click',(e)=>{
     e.preventDefault()
     localStorage.removeItem('token')
     window.location='login.html'
})

let projectsurl = "http://127.0.0.1:8000/api/projects/";

let getprojects = () => {

   fetch(projectsurl)
  .then(response => response.json())
  .then(data => {
       console.log(data)
       buildprojects(data)
  })
}

let buildprojects = (projects) => {
     let projetcswrapper=document.getElementById('projects-wrapper')
     projetcswrapper.innerHTML=''
     

     for (let i = 0; i< projects.length; i++) {
          let project =projects[i]

          let projectsCard=`
          <div class="project--card">
          <img src="http://127.0.0.1:8000${project.featured_img}"/>
            <div>
                <div class='card--header'>
                  <h3>${project.title}</h3>
                  <strong class='vote--option' data-vote='up' data-project="${project.id}">&#43;</strong>
                  <strong class='vote--option' data-vote='down' data-project="${project.id}">&#8722;</strong>


                </div>
                <i>${project.vote_ratios}% Positive Feedback</i>
                <p>${project.description.substring(0,150)}</p>
            </div>
          </div>
          `
          projetcswrapper.innerHTML+=projectsCard
          
     }

     //add event listener
     addVoteEvents()

}
let addVoteEvents = () => {

     let voteBtns= document.getElementsByClassName('vote--option')
     for (let i=0;voteBtns.length>i;i++){
        voteBtns[i].addEventListener('click',(e)=>{

          let token=localStorage.getItem('token')
          console.log(token)
          let vote =e.target.dataset.vote
          let project=e.target.dataset.project

          fetch(`http://127.0.0.1:8000/api/projects/${project}/vote/`,{
               method:'POST',headers:{
                    'Content-type':'application/json',Authorization:`Bearer  ${token}`
               },
               body:JSON.stringify({"value":vote})

          })

          .then(response => response.json())
          .then(data =>{
               console.log("success:",data)
               getprojects()

          })

        })

     }



}



getprojects()
