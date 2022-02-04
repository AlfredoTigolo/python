MacOS
Install homebrew
Brew install virtualbox
Brew install vagrant
Vagrant box add Laravel/homestead
Git clone https://github.com/laravel/homestead.git Homestead
cd Homestead
init.sh #comment out ssh keys line in Homestead.yaml
vagrant up #starting VM
vagrant ssh #remoting into command line
vagrant halt #stopping VM

# for windows
'''
Just install "git for windows" to obtain the command line option of git
homebrew is optional in windows
install vagrant
intall virtualbox
Vagrant box add Laravel/homestead
Git clone https://github.com/laravel/homestead.git Homestead
cd Homestead
init.bat #comment out ssh keys line in Homestead.yaml
vagrant up #starting VM
vagrant ssh #remoting into command line
vagrant halt #stopping VM
'''
