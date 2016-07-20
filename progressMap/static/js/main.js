//SELECT TOGGLE IN ADD FORM
//toggle the select tag to reveal the appropriate form field
//e represents the target element (select) and the value is the string val of its curent option

var select = $('select')
var courseField = $('.course'), curriculumField = $('.curriculum')
if (select){
select.change(function(e){
	var optionVal = e.target.value
	if (optionVal == 'article'){
		courseField.css('display', 'block')
		curriculumField.css('display', 'block')
	} else if (optionVal == 'course'){
		courseField.css('display', 'none')
		curriculumField.css('display', 'block')
	} else{
		courseField.css('display', 'none')
		curriculumField.css('display', 'none')
	}
})
}