<!DOCTYPE html>
<html>

<head>
  <title>Capture webcam image with php and jquery - ItSolutionStuff.com</title>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/webcamjs/1.0.25/webcam.min.js"></script>
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/twitter-bootstrap/4.1.3/css/bootstrap.min.css" />
  <style type="text/css">
    #results {
      padding: 20px;
      border: 1px solid;
      background: #ccc;
    }
  </style>
</head>

<body>

  <div class="container">
    <h1 class="text-center">Capture webcam image with php and jquery - ItSolutionStuff.com</h1>
    <?php
    // define variables and set to empty values
    $nameErr = $emailErr = $genderErr = $websiteErr = "";
    $name = $email = $gender = $comment = $website = "";

    if ($_SERVER["REQUEST_METHOD"] == "POST") {
      if (empty($_POST["name"])) {
        $nameErr = "Name is required";
      } else {
        $name = test_input($_POST["name"]);
        // check if name only contains letters and whitespace
        if (!preg_match("/^[a-zA-Z-' ]*$/", $name)) {
          $nameErr = "Only letters and white space allowed";
        }
      }

      if (empty($_POST["email"])) {
        $emailErr = "Email is required";
      } else {
        $email = test_input($_POST["email"]);
        // check if e-mail address is well-formed
        if (!filter_var($email, FILTER_VALIDATE_EMAIL)) {
          $emailErr = "Invalid email format";
        }
      }

      if (empty($_POST["gender"])) {
        $genderErr = "Gender is required";
      } else {
        $gender = test_input($_POST["gender"]);
      }

      if ($emailErr == "" && $genderErr == "" && $nameErr == "") {
        header('location: /TARP/storeImage.php');
      }
    }

    function test_input($data)
    {
      $data = trim($data);
      $data = stripslashes($data);
      $data = htmlspecialchars($data);
      return $data;
    }
    ?>
    <form method="POST" action="storeImage.php">
      <div class="row">
        <div class="col-md-10">
          Full Name: <input type="text" name="name">
          <span class="error">* <?php echo $nameErr; ?></span>
          <br><br>
          E-mail: <input type="text" name="email">
          <span class="error">* <?php echo $emailErr; ?></span>
          <br><br>
          Username: <input type="text" name="username">
          <br><br>
          Password: <input type="password" name="password">
          <br><br>
          Date of Birth: <input type="date" id="dob" name="dob">
          <br><br>
          Gender:
          <input type="radio" name="gender" value="female">Female
          <input type="radio" name="gender" value="male">Male
          <input type="radio" name="gender" value="other">Other
          <span class="error">* <?php echo $genderErr; ?></span>
          <br><br>
        </div>
        <div class="col-md-6">
          <div id="my_camera"></div>
          <br />
          <input type=button value="Take Snapshot" onClick="take_snapshot()">
          <input type="hidden" name="image" class="image-tag">
        </div>
        <div class="col-md-6">
          <div id="results">Your captured image will appear here...</div>
        </div>
        <div class="col-md-12 text-center">
          <br />
          <button class="btn btn-success">Submit</button>
        </div>
      </div>
    </form>
  </div>

  <!-- Configure a few settings and attach camera -->
  <script language="JavaScript">
    Webcam.set({
      width: 490,
      height: 390,
      image_format: 'jpeg',
      jpeg_quality: 90
    });

    Webcam.attach('#my_camera');

    function take_snapshot() {
      Webcam.snap(function(data_uri) {
        $(".image-tag").val(data_uri);
        document.getElementById('results').innerHTML = '<img src="' + data_uri + '"/>';
      });
    }
  </script>

</body>

</html>