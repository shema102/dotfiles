# pip should only run if there is a virtualenv currently activated
export PIP_REQUIRE_VIRTUALENV=true

#Explicitly specify locale
export LC_ALL=en_US.UTF-8

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
export PROJECT_HOME=$HOME/Documents/Develop
export VIRTUALENVWRAPPER_PYTHON=$(which python3)
export VIRTUALENVWRAPPER_VIRTUALENV=$(which virtualenv)
source $(which virtualenvwrapper.sh)

# Export Android Studio folder
export PATH="$PATH:/opt/android-studio/bin"
export PATH="$PATH:$HOME/Library/Android/sdk/platform-tools"
export ANDROID_SDK_ROOT="$HOME/Library/Android/sdk"

# Init SDKMAN
source $HOME/.sdkman/bin/sdkman-init.sh
