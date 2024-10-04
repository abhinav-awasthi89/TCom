function sendmail(){
    var params = {
        seller_name : document.querySelector(".seller-name").innerHTML,
        my_name : document.querySelector(".my-name").value,
        product_name : document.querySelector(".product-name").innerHTML,
        my_mail : document.querySelector(".my-mail").value,
        seller_mail: document.querySelector(".seller-mail").innerHTML,
        mess: document.querySelector(".my-mess").value
    };
    const service_id = "service_6sxn973";
    const template_id = "template_5vclz9r";
    emailjs.send(service_id,template_id,params)
    .then(res=>{

         document.querySelector(".my-name").value = "";
         document.querySelector(".my-mail").value = "";
        alert("request sent to the seller successfully");
    }).catch(err=>{
        alert("some error occured");
    });
}
