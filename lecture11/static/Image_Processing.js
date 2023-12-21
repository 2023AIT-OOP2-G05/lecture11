async function uploadFile() {

  //フォームデータオブジェクトに画像を代入
  let formData = new FormData(); 
  formData.append("file", fileupload.files[0]);

  //network request using POST method of fetch
  /*
  await fetch('PASTE_YOUR_URL_HERE', {
  method: "POST", 
  body: formData
  }); 
  */

  fetch("/picture", {
      method: "POST",
      body: formData,
    })
  console.log("送信")
}