var $element = $('input[type="range"]');
var URL = 'http://192.168.1.131:8000'

$element.rangeslider({
	polyfill: false
}).on('input', function() {
	var side = (this.value < 0) ? 'rigth' : 'left'
	var speed = 100 - Math.abs(this.value)
	fetch(URL + '/?side=' + side + '&direction=forward&enabled=true&speed=' + speed)
		.then(response => response.text())
		.then(response => console.log(response))
		.catch(error => console.error(error))
})

$('#stop').click(() => {
	console.log('STOP')
	fetch(URL + '/?side=left&direction=forward&enabled=false&speed=0')
		.then(response => response.text())
		.then(response => console.log(response))
		.catch(error => console.error(error))
	fetch(URL + '/?side=rigth&direction=forward&enabled=false&speed=0')
		.then(response => response.text())
		.then(response => console.log(response))
		.catch(error => console.error(error))
})

$('#go').click(() => {
	console.log('GO')
	fetch(URL + '/?side=left&direction=forward&enabled=true&speed=100')
		.then(response => response.text())
		.then(response => console.log(response))
		.catch(error => console.error(error))
	fetch(URL + '/?side=rigth&direction=forward&enabled=true&speed=100')
		.then(response => response.text())
		.then(response => console.log(response))
		.catch(error => console.error(error))
})