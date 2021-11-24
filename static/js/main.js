var updateBtn = document.getElementsByClassName('update-cart')

for(var i =0; i<updateBtn.length;i++){
    updateBtn[i].addEventListener('click', function(){
        var productId = this.dataset.product
        var action = this.dataset.action
        console.log('product:', productId,'action:', action)

       // console.log('User', user)
       // if(user == 'AnnonemousUser'){
          //  console.log('Not login')
       // }else{
        //    console.log('User login, sending data')
       // }

        //showItem(productId, action)
    })
}

function showItem(productId, action){

    console.log('log in js')

    var url = '/update_item/'
    fetch(url,{
        method:'POST',
        headers:{
            'Content-Type':'applicaiton/json',
            'X-CSRFToken': csrftoken,
        },
        body:JSON.stringify({'productId': productId, 'action': action})
    })

    .then((response) =>{
        return response.json();
    })

    .then((data) =>{
        console.log('data', data)
    })

}

var form_fields = document.getElementsByTagName('input')
form_fields[1].placeholder='Username..';
form_fields[2].placeholder='Email..';
form_fields[3].placeholder='Enter password...';
form_fields[4].placeholder='Re-enter Password...';


for (var field in form_fields){	
    form_fields[field].className += ' form-control'
}