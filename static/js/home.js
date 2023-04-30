const form = document.querySelector('form');
const voterId = document.querySelector(".voterId");
const submitBtn = document.querySelector(".submitBtn");

form.addEventListener('submit', function (e) {
	// prevent form submission by default
	e.preventDefault();
});

voterId.addEventListener('input', function (e) {
	if (voterId.value.match(/^[A-Z]{3}[0-9]{7}$/)) {
		voterId.style.color = "green"
	} else {
		voterId.style.color = "black"
	}
});

submitBtn.addEventListener("click", () => {
	if (voterId.value.match(/^[A-Z]{3}[0-9]{7}$/)) {
		form.submit();
	} else {
		voterId.style.color = "red"
	}
});

