#!/bin/sh

DOTFILES_DIR=$(pwd)

#==============
# Create symlinks in the home folder
# Allow overriding with files of matching names in the custom-configs dir
#==============
mkdir -p ~/.config
rm -rf ~/.config/nvim
ln -s $DOTFILES_DIR/config/nvim ~/.config/nvim

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

echo "Created symlinks"

#==============
# Install plug.nvim
#==============
sh -c 'curl -fLo "${XDG_DATA_HOME:-$HOME/.local/share}"/nvim/site/autoload/plug.vim --create-dirs \
       https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim'
echo "Installed plug.nvim"

#==============
# Install oh-my-zsh
#==============
sh -c "$(curl -fsSL https://raw.github.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"

rm -rf ~/.zshrc
ln -s $DOTFILES_DIR/zshrc ~/.zshrc

