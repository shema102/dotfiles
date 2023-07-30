function Handle-Symlink {
  param(
    [string]$target,
    [string]$linkName
  )

  # Check if the path is a symbolic link
  if ((Get-Item $linkName -ErrorAction SilentlyContinue).Attributes -eq 'ReparsePoint') {
    # If it is a symbolic link, just delete it
    Remove-Item -Force $linkName
  }
  elseif (Test-Path -PathType Container $linkName) {
    # If it is a regular directory, rename it, appending .old as needed
    $oldLinkName = "$linkName.old"
    while (Test-Path $oldLinkName) {
      $oldLinkName = "$oldLinkName.old"
    }
    Move-Item $linkName $oldLinkName
  }

  # Create symlink
  New-Item -ItemType SymbolicLink -Path $linkName -Target $target
}

# Get the DOTFILES_DIR from the script location
$DOTFILES_DIR = $PSScriptRoot

# Example usage for Neovim
Handle-Symlink -target "$DOTFILES_DIR\nvim" -linkName "$env:LOCALAPPDATA\nvim"

