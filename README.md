# debian-config
configuration files and scripts for fresh debian install

## Prerequisites
### Add superuser
1. Run the following commands
```bash
$ su --login
Password: (enter here the password of the root user that you specified during your Debian installation, and press Enter)

# apt install sudo

# adduser joost sudo
```
2. Logout and log back in

### Get scripts
1. Install git
```bash
sudo apt install git
```

2. Make Scripts directory
 ```bash
 mkdir Scripts
 cd Scripts
 ```

2. clone this repo
```bash
git clone https://github.com/Jvdputten/debian-config
```

## Installation scripts
[qtile-setup.sh](https://github.com/Jvdputten/debian-config/blob/main/qtile-setup.sh) - Enable global management of pip and install qtile.
