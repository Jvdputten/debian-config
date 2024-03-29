sudo apt install zsh curl kitty &&

# make zsh default shell
chsh -s $(which zsh)

sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)" # install ohmyzsh
git clone --depth=1 https://github.com/romkatv/powerlevel10k.git ${ZSH_CUSTOM:-$HOME/.oh-my-zsh/custom}/themes/powerlevel10k # get powerlevel10k theme

# kitty theme
THEME=https://raw.githubusercontent.com/dexpota/kitty-themes/master/themes/OneDark.conf
wget "$THEME" -P ~/.config/kitty/kitty-themes/themes
cd ~/.config/kitty
ln -s ./kitty-themes/themes/OneDark.conf ~/.config/kitty/theme.conf
echo "include ./theme.conf" > kitty.conf
chmod +x ~/.config/kitty/kitty-themes/themes/OneDark.conf
sed -i "6s/background.*/background #222222/" ~/.config/kitty/kitty-themes/themes/OneDark.conf

echo "font_family FiraCode Nerd Font Mono" > font.conf


curl -sS https://raw.githubusercontent.com/ajeetdsouza/zoxide/main/install.sh | bash # install zoxide

# install nerd font SourceCodePro
wget -P ~/.local/share/fonts https://github.com/ryanoasis/nerd-fonts/releases/download/v3.1.1/FiraCode.zip\
&& cd ~/.local/share/fonts \
&& unzip FiraCode.zip \
&& rm FiraCode.zip \
&& fc-cache -fv
