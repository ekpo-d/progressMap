//navbar hamburger toggle
  $(".navbar-toggle").on("click", function () {
				    $(this).toggleClass("active");
    });

//curriculum list headings
curriculum = $('.curriculum')
curriculum.map(function(element){
	curriculum[element].textContent = curriculum[element].textContent.toUpperCase()
})