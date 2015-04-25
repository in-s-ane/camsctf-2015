<?php
// Redacted

class Login {
    private $table;
    private $success;
    
    function __construct() {
        $this->table = 'login';
    }
    
    public function checkPass($user, $pass) {
        $database = Database::getConnection();
        $query = sprintf("SELECT `username` FROM %s WHERE username = '%s' AND password = '%s'", $this->table, $database->real_escape_string($user), $database->real_escape_string($pass));
        $result = $database->query($query);
        if ($result !== false && mysqli_num_rows($result) === 1) {
            $this->success = '1';
        } else {
            $this->success = '0';
        }
    }
    
    function __toString() {
        if (!isset($this->success)) {
            // Not initialized.
            $this->checkPass('', '');
        }
        return $this->success;
    }
}

class Admin {
    public $name;
    
    function __construct($name) {
        $this->name = $name;
    }
    
    function __toString() {
        if (isset($this->name) && $this->name == '127.0.0.1') {
            return 'Source: Knp3HWpc.php';
        } else if (strlen($this->name) > 0) {
            return sprintf("Hello %s! You do not look like admin at all. Thus, go away.", $this->name);
        }
    }
}

// user1:iamprincess
// aliston:aliston
// iamsomeuser:iamsomepassword
// kbarr:barrbarr

show_source(__FILE__); 
?>