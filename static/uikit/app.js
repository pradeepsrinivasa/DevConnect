// Invoke Functions Call on Document Loaded
document.addEventListener('DOMContentLoaded', function () {
  hljs.highlightAll();

  // Select alert elements only after the DOM is fully loaded
  let alertwrapper = document.querySelector('.alert');
  let alertclose = document.querySelector('.alert__close');

  // Check if the alert wrapper and close button exist
  if (alertwrapper && alertclose) {
    console.log('Alert wrapper found');
    alertclose.addEventListener('click', () => {
      alertwrapper.style.display = 'none';
    });
  }
});


document.addEventListener('DOMContentLoaded', () => {
  let tags = document.getElementsByClassName('project-tag');
  
  for (let i = 0; i < tags.length; i++) {
      tags[i].addEventListener('click', (e) => {
          let tagId = e.target.dataset.tag;
          let projectId = e.target.dataset.project;

          let url = 'http://127.0.0.1:8000/api/remove-tag/';
          fetch(url, {
              method: 'DELETE',
              headers: {
                  'Content-Type': 'application/json'
              },
              body: JSON.stringify({
                  'project': projectId,
                  'tag': tagId
              })
          })
          .then(response => {
              if (!response.ok) {
                  throw new Error('Network response was not ok');
              }
              return response.json();
          })
          .then(data => {
              e.target.remove();
          })
          .catch(error => {
              console.error('There has been a problem with your fetch operation:', error);
          });
      });
  }
});