function uploadFile() {
    var fileInput = document.getElementById('fileInput');
    var file = fileInput.files[0];

    var formData = new FormData();
    formData.append('file', file);

    // Use AJAX to send the file to the server
    var xhr = new XMLHttpRequest();
    xhr.open('POST', '/upload', true);

    xhr.onload = function() {
        if (xhr.status === 200) {
            // Handle success
            console.log(xhr.responseText);
        } else {
            // Handle error
            console.error(xhr.responseText);
        }
    };

    xhr.send(formData);
}
