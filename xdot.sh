#/bin/bash
libreoffice --writer &
xdotool search --class "libreoffice" windowactivate
sleep 1
xdotool type "Escrito usando xdotool"
sleep 1
xdotool key KP_Enter
xdotool type "Desde un shell script"
xdotool key KP_Enter
xdotool type "Saliendo en:"
xdotool key KP_Enter
xdotool type "3..."
sleep 1
xdotool key KP_Enter
xdotool type "2..."
sleep 1
xdotool key KP_Enter
xdotool type "1..."
sleep 1
xdotool key KP_Enter
xdotool key Ctrl+s
#xdotool type "resultado.txt"
sleep 2
sleep 1
xdotool key xdotool key KP_Enter
sleep 1
xdotool key Ctrl+w
xdotool key Ctrl+w
