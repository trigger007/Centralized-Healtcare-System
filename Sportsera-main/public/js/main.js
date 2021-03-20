const player = document.getElementById('player');
const canvas = document.getElementById('canvas');
const context = canvas.getContext('2d');
const captureButton = document.getElementById('buttonconfig');

function convertToImageData(canvas) {
	return canvas.toDataURL('image/png');
};

const constraints = {
	video: true,
};

function capButton() {
	captureButton.addEventListener('click', () => {
	// Draw the video frame to the canvas.
		context.drawImage(player, 0, 0, canvas.width, canvas.height);
	});

	var data = convertToImageData(canvas);
	console.log(data);
	// alert(data);
	document.getElementById('fileInput').value = data;
	alert("Signed Up Successfully!");
};


// Attach the video stream to the video element and autoplay.
navigator.mediaDevices.getUserMedia(constraints).then((stream) => {
	player.srcObject = stream;
})

/*var dataURL = canvas.toDataURL(); 
$.ajax({ 
	type: "POST", 
	url: "script.php", 
	data: { 
		imgBase64: dataURL 
	} 
}).done(function(o) { 
	console.log('saved'); 
});*/ 
