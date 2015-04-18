<?php
error_reporting(0);

include('flag.php');
session_start();

if(!isset($_SESSION['rand0'])) {
    mt_srand(time() ^ 424242424242); // Ultra secure random seed.
    $_SESSION['rand0'] = mt_rand();
    $_SESSION['rand1'] = mt_rand();
    $_SESSION['rand2'] = mt_rand();
}

$data = "You haven't fulfilled all of my requests.";

$flag = "qweqqweqweqweq";

echo strtotime(date('Y-m-d', time() + abs((int)$_POST['1'])));
echo "\n<br>";
echo strtotime('2013-12-12');
echo "\n<br>";
echo strtotime(date('Y-m-d', time() + abs((int)$_POST['1']))) < strtotime('2013-12-12'); // Should get 1
echo "\n<br>-------------------<br>\n";

echo $_POST['2'] . "\n";
echo hash('sha512', $_POST['2']);
echo "\n<br>";
echo $_POST['3'] . "\n";
echo hash('sha512', $_POST['3']);
echo "\n<br>";
echo $_POST['2'] != $_POST['3'] && hash('sha512', $_POST['2']) == hash('sha512', $_POST['3']);
echo "\n<br>-------------------<br>\n";

echo $_POST['4'] . "  =  " . $_SESSION['rand0'] . "\n";
echo "\n<br>-------------------<br>\n";

echo strcmp($_POST['5'], $flag) == 0;
echo "\n<br>-------------------<br>\n";

if(isset($_POST['1']) && isset($_POST['2']) && isset($_POST['3']) && isset($_POST['4']) && isset($_POST['5'])) {
    if(strtotime(date('Y-m-d', time() + abs((int)$_POST['1']))) < strtotime('2013-12-12')) {
        if($_POST['2'] != $_POST['3'] && hash('sha512', $_POST['2']) == hash('sha512', $_POST['3'])) {
            if($_SESSION['rand0'] == $_POST['4']) {
                if(strcmp($_POST['5'], $flag) == 0) {
                    $data = $flag;
                }
            }
        }
    }
} 
?>
<!DOCTYPE HTML>
<html>
    <head>
        <link rel="stylesheet" href="style.css" type="text/css" />
        <link href='http://fonts.googleapis.com/css?family=Ubuntu+Mono' rel='stylesheet' type='text/css'>
        <title>Web Exploitation 9</title>
    </head>
    
    <body>
        <p>"Let's make a deal. I will give you the flag if you do 4 simple things for me." - M4gn4te Troll</p>
        <form method="post" action="index.php">
            <p>Travel back in time to a date before December 12, 2013.</p>
            <input type="text" name="1">
            <br>
            <p>Give me two strings that do not equal each other but have the same SHA-512 hash.</p>
            <input type="text" name="2">
            <input type="text" name="3">
            <br>
            <p>Guess the random number I generated before the following two numbers: <?php echo $_SESSION['rand1'] . ', ' . $_SESSION['rand2'] . '.' ?></p>
            <input type="text" name="4">
            <br>
            <p>Give me the flag to this challenge.</p>
            <input type="text" name="5">
            <br>
            
            <button type="submit" style="margin-top:20px">Submit</button>
        </form>
        
        <br>
        <p style="color: #f90;"><?php echo $data; ?></p>
    </body>
</html>

<!-- Source: source.php -->
