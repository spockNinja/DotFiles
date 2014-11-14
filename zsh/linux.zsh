ZSH_DIR=$(dirname `readlink $HOME/.zshrc`)
export PATH="$HOME/bin:$HOME/Documents/go-zone/bin:${PATH}"
export GOPATH="$HOME/Documents/go-zone"
export GTK2_RC_FILES="$HOME/.gtkrc-2.0"

alias ls='ls --color=auto'
alias hammertime='sudo supervisorctl stop all && sudo service rabbitmq-server stop && sudo service mysql restart'

source "$ZSH_DIR/common.zsh"

PROMPT='%{$fg[cyan]%}%~ '

RPROMPT='%{$fg[cyan]%}%D|%T%{$reset_color%}'
