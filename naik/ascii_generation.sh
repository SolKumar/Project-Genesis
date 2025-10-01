#!/bin/bash
# "Install Cowsay"
sudo apt-get install -y cowsay
# "Execute the Cowsay command"
cowsay -f dragon "Run boy run a Dragon is in town" >> dragon.txt
grep -i "dragon" dragon.txt
cat dragon.txt