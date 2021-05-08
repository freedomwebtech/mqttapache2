<!DOCTYPE html>
<html>
<meta name="viewport" content= "width=device-width, initial-scale=1.0">

<body style="text-align:center;">
	

	
	<?php
                $command = escapeshellcmd('python3 /home/pi/ytvideo/mqttstatus.py');
                $output = shell_exec($command);
                echo $output
                
	?>

	<script type="text/javascript">
		var x = "<?php echo"$output"?>";


		document.write(x);
	</script>
</body>

<html>

