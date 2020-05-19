# script for creating symbolic links to dotfiles

#==============
# Variables
#==============
dotfiles_dir=~/dotfiles

#==============
# Delete existing dot files and folders
#==============
sudo rm -rf ~/.vim > /dev/null 2>&1
sudo rm -rf ~/.vimrc > /dev/null 2>&1

sudo rm -rf ~/.shell /dev/null 2>&1
sudo rm -rf ~/.zsh> /dev/null 2>&1
sudo rm -rf ~/.zshrc> /dev/null 2>&1

sudo rm -rf ~/.irssi> /dev/null 2>&1
sudo rm -rf ~/.jupyther> /dev/null 2>&1

sudo rm -rf ~/.gitconf> /dev/null 2>&1
sudo rm -rf ~/.gitignore_global> /dev/null 2>&1
sudo rm -rf ~/.inputrc> /dev/null 2>&1
sudo rm -rf ~/.tmux.conf> /dev/null 2>&1

#==============
# Create symlinks in the home folder
# Allow overriding with files of matching names in the custom-configs dir
#==============
ln -sf $dotfiles_dir/vim ~/.vim
ln -sf $dotfiles_dir/vimrc ~/.vimrc

ln -sf $dotfiles_dir/shell ~/.shell
ln -sf $dotfiles_dir/zsh ~/.zsh
ln -sf $dotfiles_dir/zshrc ~/.zshrc

ln -sf $dotfiles_dir/irssi ~/.irssi
ln -sf $dotfiles_dir/jupyther ~/.jupyther

ln -sf $dotfiles_dir/gitconfig ~/.gitconfig
ln -sf $dotfiles_dir/gitignore_global ~/.gitignore_global
ln -sf $dotfiles_dir/inputrc ~/.inputrc
ln -sf $dotfiles_dir/tmux.conf ~/.tmux.conf


