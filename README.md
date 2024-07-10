# dotfiles
Archivos de configuración de mi Workflow


# Instrucciones especificas
Los temas de Rofi se sacan de: https://github.com/adi1090x/rofi 
El contenido de ese repositorio lo incluí en este repositorio por si acaso.

Clipton utiliza Rofi para mostrar el historial de cosas copiadas, para ponerle estilo a ese menú
se tiene que copiar el .rasi del estilo escojido a la carpeta /usr/share/rofi/themes/

Nota: Algunos estilos tienen dependencias, por eso recomiendo que se copie la carpeta "shared" que
esta en el repositorio de los temas de rofi a /usr/share/rofi/themes/

El tema de iconos es Tela y el tema es Graphite-Dark-Compact, se pueden obtener desde los siguientes
links:
    Tela icons: https://github.com/vinceliuice/Tela-icon-theme
    Graphite: https://github.com/vinceliuice/Graphite-gtk-theme

El tema del mouse es Breeze light

Nota: Tela icons lo instale por medio de aur, pero recomiendo instalarlos usando el repo de Github
parece que el paquete de Aur esta desactualizado

Para hacer que la imagen de usuario aparezca, se pone una imagen en /var/lib/AccountsService/icons/
y luego se usa esa ruta + el nombre de la imagen en el archivo /var/lib/AccountsService/users/alan

Nota: Se requieren permisos root para entrar a esa carpeta

# Secure Boot en ArchLinux
Logre instalar Archlinux y que iniciara con SecureBoot activado haciendo lo siguiente:
- Tener instalado EndeavourOS con systemd-boot (Grub no me jalo)
- Usar los pasos del siguiente video: Install Secure Boot on Arch Linux (the easy way):
    https://www.youtube.com/watch?v=yU-SE7QX6WQ
- Cuando esta haciendo el paso de firmar /efi/EFI/linux/arch-linux.efi yo no encontré el archivo 
debido a que EndeavourOS usa dracut en vez de mkinitcpio, por lo que decidí intentar firmar los tres archivos que la herramienta "sbctl verify" me arroja relacionados con linux:
    /efi/EFI/Boot/bootx64.efi
    /efi/EFI/systemd/systemd-bootx64.efi
    /efi/13(monton de numeros y letras)/6.7.1-arch1-1/linux

Nota: Supongo que el tercer archivo va variar de ubicación debido a que se trata de version del 
Kernel pero con usar "sbctl verify" este mostrará los archivos que faltan por firmar de Linux 
incluso muestra los archivos que faltan por firmar de Windows pero no se si los tenga que firmar 
tambien (Por ahora mi Windows inicia tambien en DualBoot sin haberlos firmado)

Nota: Se supone que las actualizaciones de Linux se firmarán automaticamente, ya lo comprobe asi que 
en teoría no debería haber problemas

# Editar/Eliminar aplicaciones mostradas en Rofi
"Hidden=true" en cada archivo .desktop de la aplicacion/paquete que se quiere esconder ubicados en 
-> /usr/share/applications
-> /usr/local/share/applications
-> /.local/share/applications

# Qtile
Los iconos que se ven en la barra de estatus del widget del Layout se deben poner en la carpeta de ~/.icons, ver la documentación de Qtile para tener mejores ejemplos

# Paquetes instalados (Lista que hice manualmente)
dmenu - Lanzador de aplicaciones que permite crear menús en las barras de estado
lxappearance - Cambiador de temas GTK2
lxappearance-gtk3 - Cambiador de temas GTK3
picom-simpleanims-git - Compositor de ventanas (Fork de picom que trae animaciones)
polkit-gnome - Interfaz para permitir operaciones como sudo a las aplicaciones no iniciadas con sudo
python-psutil - libreria de pyton para obtener informacion del sistema
python-setuptools - libreria para administrar paquetes de python instalados, actualizarlos, eliminarlos, etc
rofi - Lanzador de aplicaciones (Menú principal)
thunar - Explorador de archivos
thunar-archive-plugin - Plugin del explorador de archivos para extraer cosas (algo asi)
thunar-volman - Plugin para administrar los medios extraibles
volumeicon - Applet de control de volumen (Supongo que para ponerlo en las barras)
dunst - Servicio de notificaciones
xfce4-screenshooter - Para tomar capturas de pantalla
arcolinux-logout - Es un paquete para hacer display de los botones para apagar reinciar etc.
archlinux-tweak-tool-git - Paquete para adminsitrar el sistema operativo
arcolinux-desktop-trasher-git - Paquete que ayuda a eliminar un DE (creo que solo se puede instalar en arco linux)
remmina - Software de escritorio remoto
snapper - Software para snapshots
snapper-support
snapper-tools
snap-pac
nitrogen
discord
spotify
visual-studio-code-bin
autorandr
unity
starship
blueman
web-greeter
lightdm-theme-neon-git
gendesk - Herramienta para crear entradas de escritorio de los paquetes instalados
gvfs - Algo para que thunar funcione correctamente
betterlockscreen - Dependencia chida para arolinux-logout
ttf-material-design-icons-extended
