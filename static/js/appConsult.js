function consult_user() {
    let id = document.getElementById("ident").value
    let obj_data = {
        "id":id
    }
    fetch("/consult_user", {
        "method":"post",
        "headers":{"Content-Type":"application/json"},
        "body": JSON.stringify(obj_data)
    })
    .then( response => response.json())
    .then( data => {
        if (data.status == "ok") {
            document.getElementById("txt-data").value = data.name + "\n" + data.lastname
            document.getElementById("img-user").src = "https://cymetria-aws.s3.us-east-2.amazonaws.com/images/" + id + ".jpg"
        }
        else {
            alert("Usuario no encontrado")
        }
    })
    .catch(err => alert(err))
}