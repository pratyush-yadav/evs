const form = document.querySelector('form');
const voterId = document.querySelector(".voterId");
const submitBtn = document.querySelector(".submitBtn");

form.addEventListener('submit', function (e) {
    // prevent form submission by default
    e.preventDefault();

	//voterID validation
	submitBtn.addEventListener("click", () => {
		if (voterId.value.match(/^[A-Z]{3}[0-9]{7}$/)) {
			form.submit();
		}
		else {
			alert("Invalid Voter Id");
		}
	});
});

