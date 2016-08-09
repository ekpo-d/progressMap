//navbar hamburger toggle
  $(".navbar-toggle").on("click", function () {
				    $(this).toggleClass("active");
    });

//curriculum list headings (make them uppercase)
curriculum = $('.curriculumH')
curriculum.map(function(element){
	curriculum[element].textContent = curriculum[element].textContent.toUpperCase()
})

//completed checkbox
var completed = $('.completed')
completed.map(function(elt){
	var eltNode = (completed[elt].previousSibling)
	console.log(eltNode)
	eltNode.css('text-decoration', 'line-through')
})
