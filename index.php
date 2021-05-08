<?php 

//$command = escapeshellcmd('python3 /var/www/html/hello.py');
//$output = shell_exec($command);
//#echo$output;
//echo "<p align='center'> <font color=blue  size='6pt'>$output</font> </p"   


if (isset($_POST['button']))
    {
       echo shell_exec("python3 /home/pi/ytvideo/mqttsubon.py");
 

    }

if (isset($_POST['butn']))
    {
       echo shell_exec("python3 /home/pi/ytvideo/mqttsuboff.py");
 

    }
  

  



?>




<!DOCTYPE html>
<html>
<meta name="viewport" content= "width=device-width, initial-scale=1.0">

<body style="text-align:center;">




        <form method="post">

        <input type="submit" value="ON" name="button" class="btn btn-primary">
        <input type="submit" value="OFF" name="butn" class="btn btn-primary">
        

        

        <script type="text/javascript">
                var x = "<?php echo"$output"?>";


                document.write(x);
        </script>

       </form>
</body>

<html>


