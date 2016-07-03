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
/*
completed[elt].addEventListener('input', function(e){
		console.log(e.target.checked)
		if (e.target.checked){
			console.log('yes')
		completed[elt].parentElement.parentElement.children[0]
		eltNode.style.textDecoration = 'line-through'
		}
})
*/
function lineThrough(elt, value){
	elt.parentElement.parentElement.firstElementChild.style.textDecoration =  value
}

var completed = $('.completed')
completed.map(function(elt){
	completed[elt].addEventListener('change', function(e){
		if (e.target.checked){
			lineThrough(e.target, 'line-through')
		}else{
			lineThrough(e.target, '')
		}
	})
})














