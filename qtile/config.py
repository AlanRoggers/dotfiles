# Copyright (c) 2010 Aldo Cortesi
# Copyright (c) 2010, 2014 dequis
# Copyright (c) 2012 Randall Ma
# Copyright (c) 2012-2014 Tycho Andersen
# Copyright (c) 2012 Craig Barnes
# Copyright (c) 2013 horsik
# Copyright (c) 2013 Tao Sauvage
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN TH

from distutils.command.config import LANG_EXT
from libqtile import bar, layout, widget, qtile
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal
from libqtile import hook

import os
import subprocess

increase_volume = 5
decrease_volume = 5


def noty_of_volume():
    noti_id = "1000000"
    timeout = 800  # Medido en milisegundos

    # Obtener el valor del volumen con pamixer
    volume = subprocess.run(
        "pamixer --get-volume", shell=True, capture_output=True, text=True
    )
    volume = int(volume.stdout)
    if volume >= 70:
        return f"dunstify '󰕾 {volume}' -t {timeout} -r {noti_id}"
    elif volume >= 30:
        return f"dunstify '󰖀 {volume}' -t {timeout} -r {noti_id}"
    elif volume > 0:
        return f"dunstify '󰕿 {volume}' -t {timeout} -r {noti_id}"
    else:
        return f"dunstify '󰖁 {volume}' -t {timeout} -r {noti_id}"


@lazy.function
def pamixerUp(qtile):

    # Subir el volumen con pamixer
    subprocess.run(
        f"pamixer -i {increase_volume}", shell=True, capture_output=False, text=True
    )
    command = noty_of_volume()
    subprocess.run(command, shell=True)


@lazy.function
def pamixerDown(qtile):
    subprocess.run(
        f"pamixer -d {decrease_volume}", shell=True, capture_output=False, text=True
    )
    command = noty_of_volume()
    subprocess.run(command, shell=True)


@hook.subscribe.startup_once
def autostart():
    home = os.path.expanduser("~/.config/qtile/autostart.sh")
    subprocess.Popen([home])


@hook.subscribe.client_new
def new_client(client):
    if client.name == "ArchLinux Logout":
        qtile.hide_show_bar()
    if client.name == "Alacritty":
        # client.center()
        client.set_size_floating(861, 425)
        client.disable_floating()


@hook.subscribe.client_killed
def logout_killed(window):
    if window.name == "ArchLinux Logout":
        qtile.hide_show_bar()


mod = "mod4"
terminal = guess_terminal()

keys = [
    # A list of available commands that can be bound to keys can be found
    # at https://docs.qtile.org/en/latest/manual/config/lazy.html
    # Switch between windows
    Key([mod], "Left", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "Right", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "Down", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "Up", lazy.layout.up(), desc="Move focus up"),
    Key(
        [mod, "shift"],
        "space",
        lazy.layout.next(),
        desc="Move window focus to other window",
    ),
    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key(
        [mod, "shift"],
        "Left",
        lazy.layout.shuffle_left(),
        desc="Move window to the left",
    ),
    Key(
        [mod, "shift"],
        "Right",
        lazy.layout.shuffle_right(),
        desc="Move window to the right",
    ),
    Key([mod, "shift"], "Down", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "Up", lazy.layout.shuffle_up(), desc="Move window up"),
    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key(
        [mod, "control"],
        "Left",
        lazy.layout.grow_left(),
        desc="Grow window to the left",
    ),
    Key(
        [mod, "control"],
        "Right",
        lazy.layout.grow_right(),
        desc="Grow window to the right",
    ),
    Key([mod, "control"], "Down", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "Up", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key(
        [mod, "shift"],
        "Return",
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack",
    ),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "q", lazy.window.kill(), desc="Kill focused window"),
    Key(
        [mod],
        "f",
        lazy.window.toggle_fullscreen(),
        desc="Toggle fullscreen on the focused window",
    ),
    Key(
        [mod],
        "t",
        lazy.window.toggle_floating(),
        desc="Toggle floating on the focused window",
    ),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod], "r", lazy.spawncmd(), desc="Spawn a command using a prompt widget"),
    # Personal Shortcuts
    Key(
        [mod],
        "space",
        lazy.spawn("/home/alan/.config/rofi/launchers/type-5/launcher.sh"),
    ),
    Key([mod], "w", lazy.spawn("google-chrome-stable")),
    Key([mod], "Escape", lazy.spawn("archlinux-logout")),
    Key([], "XF86AudioNext", lazy.spawn("playerctl --player=spotify next")),
    Key([], "XF86AudioPrev", lazy.spawn("playerctl --player=spotify previous")),
    Key([], "XF86AudioPlay", lazy.spawn("playerctl --player=spotify play-pause")),
    Key([], "XF86AudioRaiseVolume", pamixerUp),
    Key([], "XF86AudioLowerVolume", pamixerDown),
    Key([], "XF86AudioMute", lazy.spawn("pactl set-sink-mute @DEFAULT_SINK@ toggle")),
    Key([mod, "shift"], "s", lazy.spawn("xfce4-screenshooter -r")),
    Key([], "Print", lazy.spawn("xfce4-screenshooter")),
    Key([mod], "Print", lazy.spawn("xfce4-screenshooter -w")),
]

groups = [Group(name=i) for i in "12345"]
workspace_icons = "󰼾󱂟󰅶󱐟󱄖"

for i, workspace in enumerate(groups):
    workspace.label = workspace_icons[i]
    keys.extend(
        [
            # mod1 + letter of group = switch to group
            Key(
                [mod],
                workspace.name,
                lazy.group[workspace.name].toscreen(),
                desc="Switch to group {}".format(workspace.name),
            ),
            # mod1 + shift + letter of group = switch to & move focused window to group
            Key(
                [mod, "shift"],
                workspace.name,
                lazy.window.togroup(workspace.name, switch_group=True),
                desc="Switch to & move focused window to group {}".format(
                    workspace.name
                ),
            ),
            # Or, use below if you prefer not to switch to that group.
            # # mod1 + shift + letter of group = move focused window to group
            # Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
            #     desc="move focused window to group {}".format(i.name)),
        ]
    )

layouts = [
    layout.Columns(
        border_width=0,
        margin=4,
    ),
    layout.Max(),
    # Try more layouts by unleashing below layouts.
    # layout.Stack(num_stacks=2),
    # layout.Bsp(),
    # layout.Matrix(),
    # layout.MonadTall(),
    # layout.MonadWide(),
    # layout.RatioTile(),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    layout.Zoomy(),
]

widget_defaults = dict(
    font="FiraCode Nerd Font Mono Bold",
    fontsize=12,
    padding=4,
    foreground="#ffffff",
)
extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        top=bar.Bar(
            [
                widget.Systray(),
                widget.Spacer(),
                widget.GroupBox(
                    font="FiraCode Nerd Font Mono",
                    fontsize=19,
                    highlight_method="line",
                    highlight_color=["00000000", "00000000"],
                    this_current_screen_border="FF2B69",
                ),
                widget.Spacer(),
                # widget.WindowName(),
                # NB Systray is incompatible with Wayland, consider using StatusNotifier instead
                # widget.QuickExit(),
                widget.CurrentLayoutIcon(scale=0.48),
                widget.Spacer(length=20),
                widget.Clock(format="%I:%M %p", fontsize=13),
                widget.Spacer(length=10),
                widget.Volume(theme_path="/home/alan/.local/share/icons/Tela-dark"),
            ],
            28,
            background="#000000",
            border_width=[0, 0, 1, 0],  # Draw top and bottom borders
            border_color=[
                "000000",
                "000000",
                "000000",
                "000000",
            ],  # Borders are magenta
        ),
        # You can uncomment this variable if you see that on X11 floating resize/moving is laggy
        # By default we handle these events delayed to already improve performance, however your system might still be struggling
        # This variable is set to None (no cap) by default, but you can set it to 60 to indicate that you limit it to 60 events per second
        # x11_drag_polling_rate = 60,
    ),
]

# Drag floating layouts.
mouse = [
    Drag(
        [mod],
        "Button1",
        lazy.window.set_position_floating(),
        start=lazy.window.get_position(),
    ),
    Drag(
        [mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()
    ),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
floats_kept_above = True
cursor_warp = True
floating_layout = layout.Floating(
    border_width=0,
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
        Match(title="Animation", wm_class="Unity"),
    ],
)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "Qtile"