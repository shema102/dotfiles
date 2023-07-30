#!/bin/sh

DOTFILES_DIR=$(pwd)

## Neovim ##
# save current nvim config
if [ -d ~/.config/nvim ]; then
  mv ~/.config/nvim ~/.config/nvim.old
fi

# create symlink to nvim config
ln -s $DOTFILES_DIR/nvim ~/.config/nvim

