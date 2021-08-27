function handler () {
    python3 script.py $BUFFER
}

zle -N handler
bindkey "§" handler