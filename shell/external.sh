# pip should only run if there is a virtualenv currently activated
#export PIP_REQUIRE_VIRTUALENV=true

# Cache pip-installed packages to avoid re-downloading
export PIP_DOWNLOAD_CACHE=$HOME/.pip/cache

# Python startup file
export PYTHONSTARTUP=$HOME/.pythonrc

# Vagrant
VAGRANT_DISABLE_VBOXSYMLINKCREATE=1

# Default editor to nvim
export EDITOR=nvim

# Export npm folder
export PATH="$PATH:$HOME/.npm-global/bin"

# Export local folder
export PATH="$PATH:$HOME/.local/bin"

# Virtualenvwraper
export WORKON_HOME=$HOME/.virtualenvs
export PROJECT_HOME=$HOME/Devel
source $HOME/.local/bin/virtualenvwrapper.sh

# Export Android Studio folder
export PATH="$PATH:/opt/android-studio/bin"
export ANDROID_SDK_ROOT="$HOME/Android/Sdk"
