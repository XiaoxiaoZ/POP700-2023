import matplotlib.pyplot as plt
import matplotlib.patches as patches

class Operation:
    def __init__(self, job_id, op_id, machine, start, duration, color):
        self.job_id = job_id
        self.op_id = op_id
        self.machine = machine
        self.start = start
        self.duration = duration
        self.color = color
        self.rect = None

# Example schedule (job i, operation j, on machine m, duration)
operations = [
    Operation("J1", "O1", 0, 0, 3, "tab:blue"),
    Operation("J1", "O2", 1, 3, 3, "tab:blue"),
    Operation("J1", "O3", 2, 5, 2, "tab:blue"),

    Operation("J2", "O1", 0, 0, 1, "tab:orange"),
    Operation("J2", "O2", 2, 2, 5, "tab:orange"),
    Operation("J2", "O3", 1, 5, 3, "tab:orange"),

    Operation("J3", "O1", 1, 0, 3, "tab:green"),
    Operation("J3", "O2", 0, 4, 2, "tab:green"),
    Operation("J3", "O3", 2, 7, 3, "tab:green"),
]

fig, ax = plt.subplots(figsize=(10, 5))
ax.set_xlim(0, 15)
ax.set_ylim(-1, 3)
ax.set_yticks([0, 1, 2])
ax.set_yticklabels(["M1", "M2", "M3"])
ax.set_xlabel("Time")
ax.set_title("Job Shop: Drag operations to reschedule")

dragging = {"op": None, "press_x": 0, "start_x": 0}

def draw_operations():
    for op in operations:
        rect = patches.Rectangle(
            (op.start, op.machine - 0.4),
            op.duration, 0.8,
            facecolor=op.color, edgecolor="black"
        )
        ax.add_patch(rect)
        op.rect = rect
        ax.text(op.start + op.duration/2, op.machine,
                f"{op.job_id}-{op.op_id}",
                va="center", ha="center", color="white", weight="bold")

def on_press(event):
    for op in operations:
        if op.rect.contains(event)[0]:
            dragging["op"] = op
            dragging["press_x"] = event.xdata
            dragging["start_x"] = op.start
            break

def on_motion(event):
    if dragging["op"] is None or event.xdata is None:
        return
    dx = event.xdata - dragging["press_x"]
    dragging["op"].start = max(0, dragging["start_x"] + dx)
    redraw()

def on_release(event):
    dragging["op"] = None

def redraw():
    ax.cla()
    ax.set_xlim(0, 15)
    ax.set_ylim(-1, 3)
    ax.set_yticks([0, 1, 2])
    ax.set_yticklabels(["M1", "M2", "M3"])
    ax.set_xlabel("Time")
    draw_operations()
    fig.canvas.draw()

draw_operations()
fig.canvas.mpl_connect("button_press_event", on_press)
fig.canvas.mpl_connect("motion_notify_event", on_motion)
fig.canvas.mpl_connect("button_release_event", on_release)
plt.show()
