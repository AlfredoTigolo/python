MacOS
Install homebrew
Brew install virtualbox
Brew install vagrant
Vagrant box add Laravel/homestead
Git clone https://github.com/laravel/homestead.git Homestead
init.sh #comment out ssh keys line in Homestead.yaml
vagrant up #starting VM
vagrant ssh #remoting into command line
vagrant halt #stopping VM
