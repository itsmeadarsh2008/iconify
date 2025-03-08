import reflex as rx
from typing import List, Optional


class IconifyIcon(rx.Component):
    """An Iconify icon component."""

    # Set library and tag
    library = "@iconify/react"
    tag = "Icon"

    # Define required props
    icon: rx.Var[str]

    # Define optional props
    inline: rx.Var[bool]
    width: rx.Var[str | int]
    height: rx.Var[str | int]
    h_flip: rx.Var[bool]
    v_flip: rx.Var[bool]
    flip: rx.Var[str]
    rotate: rx.Var[str | int]
    color: rx.Var[str] = rx.color_mode_cond(light="black", dark="white")

    # Since this uses dynamic imports, we should use NoSSRComponent
    # is_default = True
    @classmethod
    def create(cls, *children, **props):
        if children:
            if len(children) == 1 and isinstance(children[0], str):
                props["icon"] = children[0]
            else:
                raise AttributeError(
                    f"Passing multiple children to Icon component is not allowed: remove positional "
                    f"argument: {children[1:]} to fix"
                )
        return super().create(*children, **props)
    

icon = IconifyIcon.create
