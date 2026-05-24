# 🖱️ AutoClicker

A lightweight Python autoclicker you can toggle on/off with a hotkey — no GUI needed.

## Requirements

- Python 3.x
- [pynput](https://pypi.org/project/pynput/)

```bash
pip install pynput
```

## Usage

```bash
python main.py
```

| Key | Action |
|-----|--------|
| `F6` | Toggle clicking on / off |
| `ESC` | Quit |

## Configuration

Edit the constants at the top of `main.py`:

```python
TOGGLE_KEY        = Key.f6        # Hotkey to start/stop
CLICK_BUTTON      = Button.left   # left / right / middle
CLICKS_PER_SECOND = 10            # Click speed (CPS)
```

## Platform Notes

- **Windows / Linux** — works out of the box.
- **macOS** — grant your terminal Accessibility permissions in **System Settings → Privacy & Security → Accessibility**.

## License

MIT
