let re = document.querySelector("#review_button");
let text = document.querySelector("#review_text");
let table = document.querySelector(".review_table");
let m = document.querySelector(".review_message");
re.addEventListener('click',()=>{
    let val = Math.floor(Math.random() * 10)%5;
    table.innerHTML += `<tr>
    <th><img src="A${val}.png" id="img"></th>
    <td>${text.value}</td>
</tr>`;
setTimeout(() => {
    m.innerHTML = "Contribute a Review";
}, 8000);

var params = {
message:text.value,
product:document.querySelector(".product-name").innerHTML
};
const service_id = "service_6sxn973";
const template_id = "template_kdvk1wu";
emailjs.send(service_id,template_id,params)
.catch(err=>{
    alert("some error occured");
});
});
