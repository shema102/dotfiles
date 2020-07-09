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
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from libqtile.config import Key, Screen, Group, Drag, Click
from libqtile.lazy import lazy
from libqtile import layout, bar, widget

from typing import List  # noqa: F401

import os

mod = "mod4"

# class Commands:
    # dmenu = "dmenu_run -i -b -p '>>>' - fn 'Open Sans-10' -nb '#000' -nf '#fff' -sb '#00BF32' -sf '#fff'"
    # dmenu_session = "dmenu_session"
    # dmenu_run = "dmenu_run"
    # dmenu_window = "dmenu-qtile-windowlist.py"

keys = [
    # Switch between windows in current stack pane
    Key([mod], "k", lazy.layout.down()),
    Key([mod], "j", lazy.layout.up()),

    # Move windows up or down in current stack
    Key([mod, "control"], "k", lazy.layout.shuffle_down()),
    Key([mod, "control"], "j", lazy.layout.shuffle_up()),

    # Switch window focus to other pane(s) of stack
    Key([mod], "space", lazy.layout.next()),

    # Swap panes of split stack
    Key([mod, "shift"], "space", lazy.layout.rotate()),

    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key([mod, "shift"], "Return", lazy.layout.toggle_split()),
    Key([mod], "Return", lazy.spawn("sakura")),
    Key([mod], "e", lazy.spawn('rofi -combi-modi window,drun,ssh -theme solarized -font "hack 10" -show combi -icon-theme "Papirus" -show-icons')),
    Key([mod], "w", lazy.spawn("chromium")),
    Key([mod], "q", lazy.spawn("code")),

    # backlight control
    Key([], "XF86MonBrightnessUp", lazy.spawn("brightnessctl set +4%")),
    Key([], "XF86MonBrightnessDown", lazy.spawn("brightnessctl set 4%-")),

    # general volume
    Key([], "XF86AudioRaiseVolume", lazy.spawn("ponymix increase 5")),
    Key([], "XF86AudioLowerVolume", lazy.spawn("ponymix decrease 5")),
    Key([], "XF86AudioMute", lazy.spawn("ponymix toggle")),

    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout()),
    Key([mod, "shift"], "c", lazy.window.kill()),

    Key([mod, "shift"], "r", lazy.restart()),
    Key([mod, "shift"], "l", lazy.shutdown()),
    Key([mod], "r", lazy.spawncmd()),
]

#### GROUPS #####
group_names = [("WWW", {'layout': 'max'}),
               ("DEV", {'layout': 'monadtall'}),
               ("SYS", {'layout': 'monadtall'}),
               ("DOC", {'layout': 'monadtall'}),
               ("GFX", {'layout': 'floating'})]

groups = [Group(name, **kwargs) for name, kwargs in group_names]

for i, (name, kwargs) in enumerate(group_names, 1):
    keys.append(Key([mod], str(i), lazy.group[name].toscreen()))        # Switch to another group
    keys.append(Key([mod, "shift"], str(i), lazy.window.togroup(name))) # Send current window to another group

##### DEFAULT THEME SETTINGS FOR LAYOUTS #####
layout_theme = {"border_width": 2,
                "margin": 2,
                "border_focus": "e1acff",
                "border_normal": "1D2330"
                }

##### THE LAYOUTS #####
layouts = [
    #layout.MonadWide(**layout_theme),
    #layout.Bsp(**layout_theme),
    #layout.Stack(stacks=2, **layout_theme),
    #layout.Columns(**layout_theme),
    #layout.RatioTile(**layout_theme),
    #layout.VerticalTile(**layout_theme),
    #layout.Matrix(**layout_theme),
    #layout.Zoomy(**layout_theme),
    layout.MonadTall(**layout_theme),
    layout.Max(**layout_theme),
    layout.Tile(shift_windows=True, **layout_theme),
    layout.Stack(num_stacks=2),
    layout.TreeTab(
         font = "Ubuntu",
         fontsize = 10,
         sections = ["FIRST", "SECOND"],
         section_fontsize = 11,
         bg_color = "141414",
         active_bg = "90C435",
         active_fg = "000000",
         inactive_bg = "384323",
         inactive_fg = "a0a0a0",
         padding_y = 5,
         section_top = 10,
         panel_width = 320
         ),
    layout.Floating(**layout_theme)
]

widget_defaults = dict(
    font='sans',
    fontsize=12,
    padding=3,
)
extension_defaults = widget_defaults.copy()

# shutdown script
def shutdown(qtile):
    qtile.cmd_spawn('poweroff')

##### COLORS #####
colors = [["#282a36", "#282a36"], # panel background
          ["#434758", "#434758"], # background for current screen tab
          ["#ffffff", "#ffffff"], # font color for group names
          ["#ff5555", "#ff5555"], # border line color for current tab
          ["#8d62a9", "#8d62a9"], # border line color for other tab and odd widgets
          ["#668bd7", "#668bd7"], # color for the even widgets
          ["#e1acff", "#e1acff"]] # window name

screens = [
    Screen(
        top=bar.Bar(
            [
                widget.Sep(
                        linewidth = 0,
                        padding = 6,
                        foreground = colors[2],
                        background = colors[0]
                        ),
                widget.TextBox(
                        text = "⏻",
                        fontsize = 16,
                        linewidth = 0,
                        padding = 6,
                        foreground = colors[2],
                        background = colors[0],
                        mouse_callbacks = {"Button1": shutdown}
                        ),
                widget.Sep(
                        linewidth = 0,
                        padding = 6,
                        foreground = colors[2],
                        background = colors[0]
                        ),
                widget.CurrentLayoutIcon(custom_icon_paths=[os.path.expanduser("~/.config/qtile/icons")],
                        foreground = colors[0],
                        background = colors[4],
                        padding = 0,
                        scale=0.7
                        ),
                widget.Sep(
                        linewidth = 0,
                        padding = 6,
                        foreground = colors[2],
                        background = colors[0]
                        ),
                widget.GroupBox(font="Ubuntu Bold",
                        fontsize = 10,
                        margin_y = 3,
                        margin_x = 0,
                        padding_y = 5,
                        padding_x = 5,
                        borderwidth = 3,
                        active = colors[2],
                        inactive = colors[2],
                        rounded = False,
                        highlight_color = colors[1],
                        highlight_method = "line",
                        this_current_screen_border = colors[3],
                        this_screen_border = colors [4],
                        other_current_screen_border = colors[0],
                        other_screen_border = colors[0],
                        foreground = colors[2],
                        background = colors[0]
                        ),
                # widget.Prompt(),
                # widget.WindowName(),
                widget.Spacer(
                        background = colors[0]
                        ),
                widget.TextBox(
                        text='',
                        foreground = colors[4],
                        background = colors[0],
                        padding=-14,
                        fontsize=69
                        ),
                widget.Memory(
                        font="Ubuntu Bold",
                        foreground=colors[2],
                        background=colors[4],
                        margin_y = 3,
                        margin_x = 0,
                        padding_y = 5,
                        padding_x = 5,
                        borderwidth = 3,
                        ),
                widget.TextBox(
                        text='',
                        foreground = colors[5],
                        background = colors[4],
                        padding=-14,
                        fontsize=69
                        ),
                widget.Wlan(interface="wlp3s0",
                        font="Ubuntu Bold",
                        foreground=colors[2],
                        background=colors[5],
                        margin_y = 3,
                        margin_x = 0,
                        padding_y = 5,
                        padding_x = 5,
                        borderwidth = 3,
                        ),
                widget.TextBox(
                        text='',
                        foreground = colors[4],
                        background = colors[5],
                        padding=-14,
                        fontsize=69
                        ),
                widget.Battery(
                        font="Ubuntu Bold",
                        foreground=colors[2],
                        background=colors[4],
                        margin_y = 3,
                        margin_x = 0,
                        padding_y = 5,
                        padding_x = 5,
                        borderwidth = 3,

                        ),
                widget.TextBox(
                        text='',
                        foreground = colors[5],
                        background = colors[4],
                        padding=-14,
                        fontsize=69
                        ),
                widget.KeyboardLayout(
                        configured_keyboards = ["us", "ru", "ua"],
                        font="Ubuntu Bold",
                        fontsize=14,
                        foreground=colors[2],
                        background=colors[5],
                        margin_y = 3,
                        margin_x = 0,
                        padding_y = 5,
                        padding_x = 5,
                        borderwidth = 3,
                        ),
                widget.Sep(
                        linewidth = 0,
                        padding = 6,
                        foreground = colors[2],
                        background = colors[5]
                        ),
                widget.TextBox(
                        text='',
                        foreground = colors[4],
                        background = colors[5],
                        padding=-14,
                        fontsize=69
                        ),
                widget.Clock(format='%H:%M %d-%m-%y',
                        font="Ubuntu Bold",
                        foreground=colors[2],
                        background=colors[4],
                        margin_y = 3,
                        margin_x = 0,
                        padding_y = 5,
                        padding_x = 5,
                        borderwidth = 3,
                        ),
                widget.TextBox(
                        text='',
                        foreground = colors[5],
                        background = colors[4],
                        padding=-14,
                        fontsize=69
                        ),
                widget.Systray(
                        font="Ubuntu Bold",
                        fontsize=14,
                        foreground=colors[2],
                        background=colors[5],
                        margin_y = 3,
                        margin_x = 0,
                        padding_y = 5,
                        padding_x = 5,
                        borderwidth = 3,
                        ),
                widget.Sep(
                        linewidth = 0,
                        padding = 6,
                        foreground = colors[5],
                        background = colors[5]
                        ),
            ],
            24,
        ),
    ),
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front())
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: List
main = None
follow_mouse_focus = False
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(float_rules=[
    # Run the utility of `xprop` to see the wm class and name of an X client.
    {'wmclass': 'confirm'},
    {'wmclass': 'dialog'},
    {'wmclass': 'download'},
    {'wmclass': 'error'},
    {'wmclass': 'file_progress'},
    {'wmclass': 'notification'},
    {'wmclass': 'splash'},
    {'wmclass': 'toolbar'},
    {'wmclass': 'confirmreset'},  # gitk
    {'wmclass': 'makebranch'},  # gitk
    {'wmclass': 'maketag'},  # gitk
    {'wname': 'branchdialog'},  # gitk
    {'wname': 'pinentry'},  # GPG key password entry
    {'wmclass': 'ssh-askpass'},  # ssh-askpass
])
auto_fullscreen = True
focus_on_window_activation = "smart"

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
