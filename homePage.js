let submitBtn = document.querySelector(".submitBtn");
let voterId = document.querySelector(".voterId");
let text = document.querySelector(".content h3");

let regex = /^[A-Z]{3}[0-9]{7}$/;

submitBtn.addEventListener("click", () => {
	if (voterId.value == "") {
		text.innerText = "Please Enter a Voter Id";
	}
	else if (voterId.value.match(regex)) {
		text.innerText = "Valid Voter Id"
	}
	else {
		text.innerText = "Invalid Voter Id";
	}
}); 