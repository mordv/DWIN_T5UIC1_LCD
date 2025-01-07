sudo cp simpleLCD.service /lib/systemd/system/simpleLCD.service
sudo chmod 644 /lib/systemd/system/simpleLCD.service
sudo systemctl daemon-reload
sudo systemctl enable simpleLCD.service
sudo reboot
