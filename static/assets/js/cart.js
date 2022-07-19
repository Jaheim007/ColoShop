// I called the class addtocart to my cart.js file
let btns = document.getElementsByClassName('addtocart')
// The condition is to verify the number of buttons in the home page
for(let i = 0; i < btns.length; i++){
	btns[i].addEventListener('click', function(){
		let productId = this.dataset.product
		let action = this.dataset.action
		console.log(productId)

		if (user === "AnonymousUser"){
			console.log("U are an AnonymousUser")
		}
		else{
			updateCart(productId, action)
		}
			
	})
}

function updateCart(id, action){
	let url = 'update/'
	fetch(url, {
		method: 'POST',
		headers:{
			"Content-Type":"application/json",
			"X-CSRFToken": csrftoken,
		},
		body: JSON.stringify({"productId": id , "action": action})
	})
	.then(response => response.json())
	.then(data => console.log(data))
}


 