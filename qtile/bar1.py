from libqtile.bar import Bar
from libqtile.widget.clock import Clock
from libqtile.widget.cpu import CPU
from libqtile.widget.currentlayout import CurrentLayout
from libqtile.widget.groupbox import GroupBox
from libqtile.widget.memory import Memory
from libqtile.widget.net import Net
from libqtile.widget.systray import Systray
from libqtile.widget.window_count import WindowCount
from libqtile.widget.windowname import WindowName
from libqtile.widget.quick_exit import QuickExit

from unicodes import left_half_circle, right_arrow, right_half_circle
from colors import onedark

BAR_HEIGHT = 28
# BAR_MARGIN = 5

bar = Bar(
    [
        GroupBox(
            disable_drag=True,
            active=onedark["fg"],
            inactive=onedark["bg_highlight"],
            highlight_method="border",
            block_highlight_text_color=onedark["blue"],
            borderwidth=2,
            background=onedark["bg"],
            spacing=2,
        ),
        left_half_circle(onedark["red"], onedark["bg"]),
        CurrentLayout(
            background=onedark["red"],
            foreground=onedark["black"],
            margin=10,
        ),
        right_arrow(onedark["fg_gutter"], onedark["red"]),
        WindowCount(
            text_format="\uf2d2 {num}",
            background=onedark["fg_gutter"],
            foreground=onedark["black"],
            show_zero=True,
        ),
        right_half_circle(onedark["fg_gutter"], onedark["bg"]),
        WindowName(background=onedark["bg"], foreground=onedark["fg"]),
        left_half_circle(onedark["black"], onedark["bg"]),
        CPU(
            format=" {freq_current}GHz {load_percent}%",
            background=onedark["black"],
            foreground=onedark["pink"],
        ),
        Memory(
            format=" {MemUsed: .0f}{mm}/{MemTotal: .0f}{mm}",
            background=onedark["black"],
            foreground=onedark["cyan"],
        ),
        Net(background=onedark["black"], foreground=onedark["green"]),
        Clock(
            background=onedark["black"],
            foreground=onedark["white"],
            format="\uf43a %Y-%m-%d %a %I:%M %p",
        ),
    ],
    background=onedark["bg"],
    size=BAR_HEIGHT,
    margin=8,
)
