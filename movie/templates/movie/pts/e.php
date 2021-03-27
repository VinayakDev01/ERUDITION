
<?php
echo "DATE:".date("d/m/y")."<br/>";
$A=$_POST['username'];


$B=$_POST['Emailid'];
$C=$_POST['number'];
$cont=strlen($C);
$D=$_POST["father'sname"];
$E=$_POST['password'];

if(isset($_POST['submit'])){
	if(!empty(isset($_POST['Chosecource']))){
		$checked_count=count($_POST['Chosecource']);
		echo "SELECTED NUMBER OF SUBJECT:-".$checked_count."<br/>SELECTED SUBJECTS ARE:-";
		
	foreach($_POST['Chosecource'] as $selected)
	{	
		echo  $selected.",";
	}echo "<br/>";
	}
}

$G=$_POST['gender'];

if(isset($_POST['extrasub']))
{
	$H=$_POST['extrasub'];
}

if(isset($_POST['city']))
{
	$I=$_POST['city'];
}

$J=$_POST["bio"];

if($cont!=10)
	echo "PHONE NUMBER INVALID RE ENTER DATA BECAUSE PHONE NUMBER ALWAYS EQUAL 10 LETTER VALID";
else
	echo "USERNAME :- $A<br/> Email id:- $B<br/> PHONE NUMBER:- $C<br/> FATHER'SNAME:- $D<br/>
	PASSWORD:- $E<br/> GENDER:- $G<br/> EXTRA SUBJECT:- $H<br/> CITY:- $I<br/> BIO:- $J";
	
?>