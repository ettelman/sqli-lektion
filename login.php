<?php
$pdo = new PDO("mysql:host=localhost;dbname=test", "root", "");
$username = $_GET['username'];
$password = $_GET['password'];

$sql = "SELECT * FROM users WHERE username = '$username' AND password = '$password'";
$result = $pdo->query($sql)->fetch();

if ($result) {
    echo "Welcome, " . $result['username'];
} else {
    echo "Login failed";
}
?>

<?php

// safe

$stmt = $pdo->prepare("SELECT * FROM users WHERE username = ? AND password = ?");
$stmt->execute([$username, $password]);
$result = $stmt->fetch();

?>