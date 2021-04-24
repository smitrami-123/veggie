var updateBtns = document.getElementsByClassName('update-smitcart')

for(var i=0; i < updateBtns.length;i++)
{
	updateBtns[i].addEventListener('click',function(){
		var productId = this.dataset.product
		var action = this.dataset.action
		console.log('ProductID :',productId,'Action :',action)

		console.log('USER:',user)
		if(user==='AnonymousUser')
		{
		    addCookieItem(productId,action)
		}
		else
		{
		   updateUserOrder(productId,action)
		}
	})
}

function updateUserOrder(productId,action)
{
    console.log('user is logged in')
    var url = '/product/updateItem/'

    fetch(url, {
        method : 'POST',
        headers : {
            'Content-Type':'application/json',
            'X-CSRFToken':csrftoken,
        },
        body : JSON.stringify({'productId':productId,'action':action})
    })

    .then((response) => {
        return response.json()
    })

    .then((data) => {
        console.log('data:',data)
        location.reload()
    })
}

function addCookieItem(productId,action){
	console.log('User is not authenticated')

	if (action == 'add'){
		if (cart[productId] == undefined){
		cart[productId] = {'quantity':1}

		}else{
			cart[productId]['quantity'] += 1
		}
	}

	if (action == 'remove'){
		cart[productId]['quantity'] -= 1

		if (cart[productId]['quantity'] <= 0){
			console.log('Item should be deleted')
			delete cart[productId];
		}
	}

	if (action == 'cancel'){
	cart[productId]['quantity'] = 0

		if (cart[productId]['quantity'] <= 0){
			console.log('Item should be deleted')
			delete cart[productId];
		}
	}

	document.cookie ='cart=' + JSON.stringify(cart) + ";domain=;path=/"
    console.log('CART:', cart)
	location.reload()
}