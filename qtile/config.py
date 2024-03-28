import os
import subprocess
from libqtile import layout, hook
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal
from colors import onedark

# from bar1 import bar
from bar1 import bar

mod = "mod4"
terminal = guess_terminal()


def run_rofi(qtile):
    script_path = os.path.expanduser("~/.config/rofi/launchers/type-1/launcher.sh")
    subprocess.call([script_path])


def run_powermenu(qtile):
    script_path = os.path.expanduser("~/.config/rofi/powermenu/type-1/powermenu.sh")
    subprocess.call([script_path])


def window_to_previous_screen(qtile, switch_group=False, switch_screen=False):
    i = qtile.screens.index(qtile.current_screen)
    if i != 0:
        group = qtile.screens[i - 1].group.name
        qtile.current_window.togroup(group, switch_group=switch_group)
        if switch_screen:
            qtile.cmd_to_screen(i - 1)


def window_to_next_screen(qtile, switch_group=False, switch_screen=False):
    i = qtile.screens.index(qtile.current_screen)
    if i + 1 != len(qtile.screens):
        group = qtile.screens[i + 1].group.name
        qtile.current_window.togroup(group, switch_group=switch_group)
        if switch_screen:
            qtile.cmd_to_screen(i + 1)


keys = [
    # A list of available commands that can be bound to keys can be found
    # at https://docs.qtile.org/en/latest/manual/config/lazy.html
    # Launch browser
    Key(
        [mod, "shift"],
        "comma",
        lazy.function(window_to_next_screen, switch_screen=True),
    ),
    Key(
        [mod, "shift"],
        "period",
        lazy.function(window_to_previous_screen, switch_screen=True),
    ),
    Key([mod], "g", lazy.spawn("google-chrome"), desc="Launch browser"),
    Key(
        [mod],
        "p",
        lazy.function(run_rofi),
        desc="Run rofi",
    ),
    Key(
        [mod],
        "x",
        lazy.function(run_powermenu),
        desc="Run powermenu",
    ),
    # Switch between windows
    Key([mod], "Left", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "Right", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "Down", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "Up", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(), desc="Move window focus to other window"),
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
    Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),
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
]


groups = [
    Group("1", label="www", matches=[Match("google-chrome")], layout="monadtall"),
    Group("2", label="dev", matches=[Match("code")], layout="monadtall"),
    Group("3", label="bbb", matches=[Match("google-chrome")], layout="monadtall"),
    Group("4", label="ccc", matches=[Match("google-chrome")], layout="monadtall"),
    Group("5", label="ddd", matches=[Match("google-chrome")], layout="monadtall"),
    Group("6", label="eee", matches=[Match("google-chrome")], layout="monadtall"),
]

for i in groups:
    keys.extend(
        [
            # mod1 + group number = switch to group
            Key(
                [mod],
                i.name,
                lazy.group[i.name].toscreen(),
                desc="Switch to group {}".format(i.name),
            ),
            # mod1 + shift + group number = switch to & move focused window to group
            # Key(
            # [mod, "shift"],
            # i.name,
            # lazy.window.togroup(i.name, switch_group=True),
            # desc="Switch to & move focused window to group {}".format(i.name),
            # ),
            # Or, use below if you prefer not to switch to that group.
            # # mod1 + shift + group number = move focused window to group
            Key(
                [mod, "shift"],
                i.name,
                lazy.window.togroup(i.name),
                desc="move focused window to group {}".format(i.name),
            ),
        ]
    )

layouts = [
    layout.MonadTall(
        border_normal=onedark["black"],
        border_focus=onedark["cyan"],
        margin=10,
        border_width=2,
        single_border_width=2,
        single_margin=10,
    ),
    layout.Max(
        border_normal=onedark["black"],
        border_focus=onedark["cyan"],
        border_width=2,
        num_stacks=1,
        margin=10,
    ),
    layout.Columns(
        border_normal=onedark["black"],
        border_focus=onedark["cyan"],
        border_width=2,
        border_normal_stack=onedark["black"],
        border_focus_stack=onedark["cyan"],
        border_on_single=2,
        margin=8,
        margin_on_single=10,
    ),
]

floating_layout = layout.Floating(
    border_normal=onedark["bg"],
    border_focus=onedark["cyan"],
    border_width=2,
    float_rules=[
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(wm_class="zoom "),
        Match(wm_class="bitwarden"),
    ],
)

widget_defaults = dict(
    font="SauceCodePro Nerd Font Mono",
    fontsize=13,
    padding=10,
    background=onedark["bg"],
)

extension_defaults = widget_defaults.copy()

screens = [Screen(top=bar)]

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


## Autostart (start only once - on boot)
@hook.subscribe.startup_once
def autostart():
    home = os.path.expanduser("~/.config/qtile/autostart.sh")
    subprocess.call([home])


dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
floats_kept_above = True
cursor_warp = False
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
wmname = "LG3D"
