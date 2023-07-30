#!/bin/sh

DOTFILES_DIR=$(pwd)

handle_symlink() {
  target=$1
  link_name=$2
  # Check if the path is a symlink
  if [ -L "$link_name" ]; then
    # If it is a symlink, just delete it
    rm -f "$link_name"
  elif [ -d "$link_name" ]; then
    # If it is a regular directory, rename it, appending .old as needed
    old_link_name="$link_name.old"
    while [ -e "$old_link_name" ]; do
      old_link_name="$old_link_name.old"
    done
    mv "$link_name" "$old_link_name"
  fi
  # Create symlink
  ln -s "$target" "$link_name"

  echo "Created symlink $link_name -> $target"
}

## Neovim ##
handle_symlink "$DOTFILES_DIR/nvim" "$HOME/.config/nvim"

