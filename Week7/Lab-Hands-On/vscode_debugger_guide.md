# VS Code Debugger: Step-by-Step Guide

### Step 1: Open the Run & Debug Panel

Press **Ctrl+Shift+D** (Windows/Linux) or **⇧⌘D** (Mac), or click the bug icon in the left Activity Bar.

---

### Step 2: Set a Breakpoint

Click the **gutter** (the area just left of the line numbers) on line 3 (`total = 0`).

A **red dot** will appear, this is your breakpoint. You can also press **F9** while your cursor is on any line.

> **Tip:** Right-click a breakpoint to make it **conditional**, e.g. only pause when `price > 20`.

---

### Step 3: Start Debugging

Press **F5**. If prompted, select **Python File** as the debug configuration.

Execution will pause at line 3 and highlight it in yellow.

---

## Step 4: Step Through the Code

Use the **Debug Toolbar** that appears at the top of the screen:

| Action       | Key              | What it does                                      |
|--------------|------------------|---------------------------------------------------|
| Continue     | `F5`             | Run until the next breakpoint                     |
| Step Over    | `F10`            | Execute current line, skip into functions         |
| Step Into    | `F11`            | Enter the function being called                   |
| Step Out     | `Shift+F11`      | Finish current function, return to caller         |
| Restart      | `Ctrl+Shift+F5`  | Restart the session                               |
| Stop         | `Shift+F5`       | End the debug session                             |

Press **F10** a few times to step through the `for` loop and watch `total` update.

---

## Step 5: Inspect Variables

While paused, look at the **Variables** panel (left sidebar):

- **Locals** shows `total`, `price`, `prices` and their current values.
- Click the **arrow** next to `prices` to expand the list and see each element.
- **Double-click** any value to edit it live and test a different scenario.

---

## Step 6: Use the Watch Panel

In the **Watch** panel (below Variables), click **+** and type an expression:

```
total * 2
```

It re-evaluates automatically on every step (useful for monitoring derived values).

---

## Step 7: Use the Debug Console

Press **Ctrl+Shift+Y** to open the **Debug Console**.

Type any Python expression and press Enter to evaluate it in the current frame:

```python
len(prices)        # → 4
prices[0] * 2      # → 21.98
total > 50         # → True
```

This works like a live Read-Eval-Print Loop (REPL), all local variables are in scope.

---

## Step 8: Inspect the Call Stack

When you step **into** `calculate_total` (press F11 on line 16), the **Call Stack** panel shows:

```
calculate_total  (app.py, line 3)
<module>         (app.py, line 16)
```

Click any frame to jump to it and inspect that frame's local variables.

---

## Step 9: Remove Breakpoints & Stop

- Click the red dot again to **remove** a breakpoint, or press **F9** on that line.
- Press **Shift+F5** to **stop** the debug session.

---

## launch.json (Optional Configuration)

If you want a persistent config, VS Code creates `.vscode/launch.json`:

```json
{
  "version": "0.2.0",
  "configurations": [
    {
      "name": "Debug app.py",
      "type": "debugpy",
      "request": "launch",
      "program": "${file}",
      "console": "integratedTerminal"
    }
  ]
}
```

Select **"Debug app.py"** from the dropdown in the Run & Debug panel, then press **F5**.

---

## Quick Reference

```
F5              → start / continue
F9              → toggle breakpoint
F10             → step over
F11             → step into
Shift+F11       → step out
Shift+F5        → stop session
Ctrl+Shift+F5   → restart
Ctrl+Shift+Y    → debug console
Ctrl+Shift+D    → open Run & Debug panel
```
