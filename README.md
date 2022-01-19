# ssh-manager
manage ssh connect


# install 
    git clone https://github.com/yinzhiqing/ssh-manager.git
    cd ssh-manager
    git submodule init 
    git submodule update

# execute
    python3 sshs.py

# config [conf.toml]
    [[host]]
        name = SHOW_NAME
        host = "ADDRESS"
        user = SSH_USER
        port = SSH_PORT
        passwd = SSH_PASSWORD
