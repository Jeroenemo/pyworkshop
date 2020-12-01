# 66 characters is perfect, no more than 79

canvas.drawString(x, y,
    'Please press {}' .format(key))

# What if you introduce a name instead?

message = 'Please press {}' .format(key)
canvas.drawstring(x, y, message)



widget.reset(True)  # forces re-draw

# VS

force_redraw = True
widget.reset(force_redraw)


