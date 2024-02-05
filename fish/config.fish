if status is-interactive
    # Commands to run in interactive sessions can go here
    starship init fish | source
    set fish_greeting ""
    neofetch
end
#neofetch

# >>> conda initialize >>>
# !! Contents within this block are managed by 'conda init' !!
if test -f /home/alan/miniconda3/bin/conda
    eval /home/alan/miniconda3/bin/conda "shell.fish" "hook" $argv | source
else
    if test -f "/home/alan/miniconda3/etc/fish/conf.d/conda.fish"
        . "/home/alan/miniconda3/etc/fish/conf.d/conda.fish"
    else
        set -x PATH "/home/alan/miniconda3/bin" $PATH
    end
end
# <<< conda initialize <<<

