// ml5.js: Pose Estimation with PoseNet
// The Coding Train / Daniel Shiffman
// https://thecodingtrain.com/learning/ml5/7.1-posenet.html
// https://youtu.be/OIo-DIOkNVg
// https://editor.p5js.org/codingtrain/sketches/ULA97pJXR

// let video;
// let poseNet;
// let pose;
// let skeleton;

// function setup() {
  // createCanvas(640, 480);
  // video = createCapture(VIDEO);
  // video.hide();
  // poseNet = ml5.poseNet(video, modelLoaded);
  // poseNet.on('pose', gotPoses);
// }

// function gotPoses(poses) {
  //console.log(poses);
  // if (poses.length > 0) {
    // pose = poses[0].pose;
    // skeleton = poses[0].skeleton;
  // }
// }

// function modelLoaded() {
  // console.log('poseNet ready');
// }

// function draw() {
  // image(video, 0, 0);

  // if (pose) {
    // let eyeR = pose.rightEye;
    // let eyeL = pose.leftEye;
    // let d = dist(eyeR.x, eyeR.y, eyeL.x, eyeL.y);
    // fill(255, 0, 0);
    // ellipse(pose.nose.x, pose.nose.y, d);
    // fill(0, 0, 255);
    // ellipse(pose.rightWrist.x, pose.rightWrist.y, 32);
    // ellipse(pose.leftWrist.x, pose.leftWrist.y, 32);

    // for (let i = 0; i < pose.keypoints.length; i++) {
      // let x = pose.keypoints[i].position.x;
      // let y = pose.keypoints[i].position.y;
      // fill(0, 255, 0);
      // ellipse(x, y, 16, 16);
    // }

    // for (let i = 0; i < skeleton.length; i++) {
      // let a = skeleton[i][0];
      // let b = skeleton[i][1];
      // strokeWeight(2);
      // stroke(255);
      // line(a.position.x, a.position.y, b.position.x, b.position.y);
    // }
  // }
// }

var video = document.getElementById('video');
var canvas = document.getElementById('canvas');
var ctx = canvas.getContext('2d');

// The detected positions will be inside an array
let poses = [];

// Create a webcam capture
// if (navigator.mediaDevices && navigator.mediaDevices.getUserMedia) {
  // navigator.mediaDevices.getUserMedia({ video: true }).then(function(stream) {
    // video.srcObject=stream;
    // video.play();
  // });
// }
navigator.mediaDevices.getUserMedia({ video: true }).then(function(stream) {
	console.log("i have reached here");
    video.srcObject=stream;
    video.play();
});

// A function to draw the video and poses into the canvas.
// This function is independent of the result of posenet
// This way the video will not seem slow if poseNet 
// is not detecting a position
function drawCameraIntoCanvas() {
  // Draw the video element into the canvas
  console.log("i have reached here");
  ctx.drawImage(video, 0, 0, 640, 480);
  // We can call both functions to draw all keypoints and the skeletons
  drawKeypoints();
  drawSkeleton();
  window.requestAnimationFrame(drawCameraIntoCanvas);
}
// Loop over the drawCameraIntoCanvas function
drawCameraIntoCanvas();

// Create a new poseNet method with a single detection
const poseNet = ml5.poseNet(video, modelReady);
poseNet.on('pose', gotPoses);

// A function that gets called every time there's an update from the model
function gotPoses(results) {
  poses = results;
}

function modelReady() {
  console.log("model ready")
  poseNet.multiPose(video)
}

// A function to draw ellipses over the detected keypoints
function drawKeypoints()  {
  //Loop through all the poses detected
  for (let i = 0; i < poses.length; i++) {
    //For each pose detected, loop through all the keypoints
    for (let j = 0; j < poses[i].pose.keypoints.length; j++) {
      let keypoint = poses[i].pose.keypoints[j];
      //Only draw an ellipse is the pose probability is bigger than 0.2
      if (keypoint.score > 0.2) {
        ctx.beginPath();
        ctx.arc(keypoint.position.x, keypoint.position.y, 10, 0, 2 * Math.PI);
        ctx.stroke();
      }
    }
  }
}

// A function to draw the skeletons
function drawSkeleton() {
  //Loop through all the skeletons detected
  for (let i = 0; i < poses.length; i++) {
   // For every skeleton, loop through all body connections
    for (let j = 0; j < poses[i].skeleton.length; j++) {
      let partA = poses[i].skeleton[j][0];
      let partB = poses[i].skeleton[j][1];
      ctx.beginPath();
      ctx.moveTo(partA.position.x, partA.position.y);
      ctx.lineTo(partB.position.x, partB.position.y);
      ctx.stroke();
    }
  }
}