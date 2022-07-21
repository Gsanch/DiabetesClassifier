
let urlSrv = "http://127.0.0.1:3000/getHtml";
fetch(urlSrv)
    .then(
        function (response) {
            if (response.status !== 200) {
                console.log('Looks like there was a problem. Status Code: ' +
                    response.status);
                return;
            }

            // Examine the text in the response
            response.json().then(function (data) {

                let rNumber=1;
                data.forEach(book => {         
                    let list = `
                    <tr>
                    <th scope="row">${rNumber}</th>
                    <td>${book.title}</td>
                    <td>${book.author}</td>
                    <td>...</td>
                  </tr>`;
                  document.getElementById("bookList").innerHTML += list;
                  rNumber++;
                });
            });
        
        }
    )
    .catch(function (err) {
        console.log('Fetch Error :-S', err);
    });

