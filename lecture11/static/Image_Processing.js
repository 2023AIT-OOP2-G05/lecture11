async function uploadFile() {
    //creating form data object and append file into that form data
let formData = new FormData(); 
formData.append("file", fileupload.files[0]);
    //network request using POST method of fetch
await fetch('PASTE_YOUR_URL_HERE', {
  method: "POST", 
  body: formData
}); 
alert('You have successfully upload the file!');
}