 
# Iconify

A Reflex wrapper for the [@iconify/react](https://www.npmjs.com/package/@iconify/react) component library, allowing you to use Iconify icons in your Reflex applications.

## Installation

```bash
pip install git+https://github.com/itsmeadarsh2008/iconify.git
```

## Usage

```python
import reflex as rx
from iconify import icon

def index():
    return rx.hstack(
        icon("mdi:home", color="blue", width=24),
        icon("fa:arrow-right", height=32, rotate="90deg"),
        icon("simple-icons:python", h_flip=True),
    )
```

## Props

The component supports the following props:

- `icon` (required): The icon name/id to display (e.g. "mdi:home")
- `inline` (optional): Whether to render the icon inline
- `width` (optional): Icon width (number for pixels or string with units)
- `height` (optional): Icon height (number for pixels or string with units)
- `h_flip` (optional): Flip icon horizontally
- `v_flip` (optional): Flip icon vertically  
- `flip` (optional): Flip icon ("horizontal", "vertical", or "both")
- `rotate` (optional): Rotation (number for degrees or string)
- `color` (optional): Icon color (defaults to black in light mode, white in dark mode)

## License

MIT
