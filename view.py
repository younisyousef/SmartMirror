from tkinter import Tk,Frame, LEFT, BOTH, BOTTOM, TOP, RIGHT
import controller

VSPACE_BETWEEN_LABELS = 40
SPACE_FROM_TOP = 30

root = Tk()
root.overrideredirect(True)
root.overrideredirect(False)
root.attributes('-fullscreen',True)
root.configure(bg = "black")
root.columnconfigure(1, weight = 1)


def refresh(root):
    for w in root.grid_slaves():
        w.destroy()
    controller.date_label(root).grid(row = 0, column = 0, sticky = "nw")
    controller.time_label(root).grid(row = 0, column = 0, sticky = "nw", pady = VSPACE_BETWEEN_LABELS)
    controller.current_temp_label(root).grid(row = 0, column = 2, sticky  = "ne")
    controller.weekdays_label(root).grid(row = 0, column = 2, sticky = "ne", padx = 300, pady = SPACE_FROM_TOP * 4)
    controller.weekly_lows_label(root).grid(row = 0, column = 2, sticky = "ne", padx = 115, pady = SPACE_FROM_TOP * 4)
    controller.weekly_highs_label(root).grid(row = 0, column = 2, sticky = "ne", pady = SPACE_FROM_TOP * 4)
    controller.forcast_title(root).grid(row = 0, column = 2, sticky = "ne", pady = SPACE_FROM_TOP * 2.5)
    controller.top_headlines_label(root).grid(row = 0, column = 0, sticky = "nw", pady = VSPACE_BETWEEN_LABELS * 4)
    controller.quote_label(root).grid(row = 0, column = 1, sticky = "sw")
    
    img = controller.current_weather_icon(root)
    vshift_amt = 0 if 'shift_amt' not in img.__dict__ else img.shift_amt
    img.grid(row = 0, column = 2, sticky = "ne", padx = 175, pady = vshift_amt)
    
    for i,icon_label in enumerate(controller.week_icon_labels(root)):
        shift_amt = 0 if 'shift_amt' not in icon_label.__dict__ else icon_label.shift_amt
        vshift_amt = 0  if 'vshift_amt' not in icon_label.__dict__ else icon_label.vshift_amt
        icon_label.grid(row = 0, column = 2, padx = 230 + shift_amt, pady = SPACE_FROM_TOP* 4 + (i * 39) + vshift_amt, sticky = "ne")
    
    root.after(100, refresh, root)

refresh(root)
root.mainloop()