<html>

<head>
    <title>LIST OF HOSPITALS</title>
    <script src="https://code.jquery.com/jquery-3.6.0.js" integrity="sha256-H+K7U5CnXl1h5ywQfKtSj8PCmoN9aaq30gDh27Xc0jk=" crossorigin="anonymous"></script>
    <script>
        function submit_soap() {
            var city = $("#city").val();
            $.get("form_get.php", {
                    city: city
                },
                function(data) {
                    $("#json_response").html(data);
                });
        }
    </script>
</head>

<body>
    <center>
        <h3>GET HOSPITALS</h3>
        <form>
            LIST OF HOSPITALS<input name="city" id="city" type="text" /><br />
            <input type="button" value="Submit" onclick="submit_soap()" />
        </form>
        <br>-----------
        <div id="json_response"></div>
    </center>
</body>

</html>