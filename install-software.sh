sudo apt install zsh curl

# make zsh default shell
chsh -s $(which zsh)

sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)" # install ohmyzsh
git clone --depth=1 https://github.com/romkatv/powerlevel10k.git ${ZSH_CUSTOM:-$HOME/.oh-my-zsh/custom}/themes/powerlevel10k # get powerlevel10k theme


curl -sS https://raw.githubusercontent.com/ajeetdsouza/zoxide/main/install.sh | bash # install zoxide


wget -P ~/.local/share/fonts https://github.com/ryanoasis/nerd-fonts/releases/download/v3.0.2/SourceCodePro.zip \
&& cd ~/.local/share/fonts \
&& unzip SourceCodePro.zip \
&& rm SourceCodePro.zip \
&& fc-cache -fv
