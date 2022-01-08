#!/usr/bin/sh

DOTFILES_DIR=$(pwd)

#==============
# Create symlinks in the home folder
# Allow overriding with files of matching names in the custom-configs dir
#==============
cp -r ~/.config/* $DOTFILES_DIR/config
rm -rf ~/.config
ln -s $DOTFILES_DIR/config ~/.config

rm -rf ~/.vim
ln -s $DOTFILES_DIR/vim/ ~/.vim

rm -rf ~/.vimrc
ln -s $DOTFILES_DIR/vimrc ~/.vimrc

rm -rf ~/.shell
ln -s $DOTFILES_DIR/shell ~/.shell
rm -rf ~/.zsh
ln -s $DOTFILES_DIR/zsh ~/.zsh

rm -rf ~/.gitconfig
ln -s $DOTFILES_DIR/gitconfig ~/.gitconfig
rm -rf ~/.gitignore_global
ln -s $DOTFILES_DIR/gitignore_global ~/.gitignore_global
rm -rf ~/.tmux.conf
ln -s $DOTFILES_DIR/tmux.conf ~/.tmux.conf

echo "Created symlinks"

#==============
# Install dein.vim for NEOVIM
#==============
curl https://raw.githubusercontent.com/Shougo/dein.vim/master/bin/installer.sh > installer.sh 
sh ./installer.sh ~/.vim/dein 1>/dev/null
rm installer.sh

echo "Installed dein.vim"

#==============
# Install vim-plug for vim
#==============
curl -fLo ~/.vim/autoload/plug.vim --create-dirs \
    https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim

echo "Installed plug.vim. To update plugins run :PlugUpgrade"

#==============
# Install oh-my-zsh
#==============
sh -c "$(curl -fsSL https://raw.github.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"

rm -rf ~/.zshrc
ln -s $DOTFILES_DIR/zshrc ~/.zshrc

