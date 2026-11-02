# Habit Tracker: Group Project 

A group of five students builds a **Habit Tracker** that runs in the terminal. A user can add habits, mark a habit as done for a day, see streaks and statistics, see a report with simple charts, and save and reload everything from a file. Each student builds **one part (one role)** on their own. In Week 7 the five parts are joined into one working application.

> **Final submission: Sunday 29.11.2026, 23:59 CET.** Demo and oral examination: 30.11.2026 or 02.12.2026 (time slots confirmed later).

> **Note for the group:** in Week 3, Role D creates the group's own `README.md` (install, run, example session, one section per module). **That file replaces this starter README**.

---

## 1. What is in the starter pack

| File | What it is for | Do you edit it? |
|---|---|---|
| `Project_Examination.pdf` | The overview: goals, grading (100 points) and what you hand in. | No |
| `Habit_Tracker_Project_Handout.ipynb` | **The full specification:** data format, role cards with exact function names, Git rules, weekly plan. Read it, but do not run the app in Jupyter. | No |
| `check_contract.py` | The instructor's checker. It tells you whether your module follows the contract. | **Never** |
| `sample_data.py` | Fake data with known answers (`make_test_data()`) and a bigger demo set (`make_demo_data()`). | **Never** |
| `contract_template.md` | The group contract. Copy it to `contract.md` and fill it in (Week 3). | Copy it |
| `progress_template.md` | The weekly progress log. Copy it to `progress.md` (Week 3). | Copy it |

> **The PDF and the handout may differ, the handout and the checker decide.**

- You do **not** need to understand the code inside `check_contract.py` or `sample_data.py`. Run the checker for your module and read the `FAIL` lines. 
- `sample_data.py` is mainly useful for Roles C, D and E.

---

## 2. Quick start

1. **Python 3.10 or newer** (check with `python --version`). On macOS and Linux type `python3` wherever this file says `python`.
2. Clone your group's **private** GitHub repository, then run once:
   ```
   git config --global pull.rebase false
   ```
3. Install the libraries:
   ```
   pip install -r requirements.txt
   ```
4. Check that the checker runs:
   ```
   python check_contract.py stubs
   ```
   It lists which files still start with `# STUB` and which contain real code.

Libraries: the standard library by default. `matplotlib` only for Role D, `pandas`/`numpy` only for Role C. Every extra library must be listed in `requirements.txt` (Role A edits that file). No internet is needed to run the app.

---

## 3. The five roles

| Role | Files | You build | Check your work with |
|---|---|---|---|
| **A: Storage** | `storage.py` | `load_data`, `save_data`, `export_csv` | `python check_contract.py storage full` |
| **B: Habit Manager** | `habits.py` | `add_habit`, `remove_habit`, `list_habits`, `mark_done` | `python check_contract.py habits full` |
| **C: Analytics** | `analytics.py` | `current_streak`, `longest_streak`, `completion_rate`, `weekly_summary` (uses pandas or NumPy in at least one function) | `python check_contract.py analytics full` |
| **D: Reports and Charts** | `reports.py` | `text_chart`, `save_chart_image`, `build_report`, `save_report` | `python check_contract.py reports full` |
| **E: Command-Line App** | `main.py`, `utils.py` | The menu (options 1 to 9 and 0) and the input helpers `ask_int`, `ask_date`, `ask_yes_no` (`ask_text` optional) | `python check_contract.py utils full` and `python check_contract.py main full` |

Every student also writes their own unit tests (`test_<module>.py`, at least 5), an integration test file (`test_integration_X.py`, at least 2 tests), a short individual note, and one peer review. The exact tasks of your role are on your **role card** in the handout.

### Checker commands

| Command | Meaning |
|---|---|
| `python check_contract.py <module>` | **Quick check:** do the functions exist and return the right type? Use it for your Week 3 stub. |
| `python check_contract.py <module> full` | **Full check:** are the results correct? Use it for your real code. |
| `python check_contract.py all full` | Full check of storage, habits, analytics, reports and utils (**not** `main`). |
| `python check_contract.py main` / `main full` | Quick / full check of the app: menu, bad input, end of input, demo data, broken files, options 5 to 8 with data, a journey. |
| `python check_contract.py stubs` | Lists which files still start with `# STUB`. |

---

## 4. The shared data format

All five parts use the **same dictionary**, called `data`:

```python
data = {
    "habits": {"1": {"name": "Read 20 minutes", "created": "2026-10-05"}},
    "log":    {"1": ["2026-10-05", "2026-10-06"]},   # dates when habit "1" was done
}
```

- Habit ids are **text** (`"1"`), not numbers.
- Dates are **text** in the form `YYYY-MM-DD` (exactly 10 characters, for example `2026-01-05`).
- `data["log"]` may have no entry for a habit that was never done.
- Roles B, C, D and E check dates with the same `parse_date` function (copy it from Section 1.2 of the handout). Do not use `fromisoformat()`.

---

## 5. How the parts fit together

```
                main.py (E) holds the one `data` dictionary
                 |
   +-------------+---------------+----------------+
   |             |               |                |
storage.py    habits.py     analytics.py      reports.py
 (A)           (B)           (C)               (D)
load / save   changes data  reads data,        reads data,
export CSV    (add, mark)   returns numbers    builds text
```

Because the function names and the data format never change, a real file can take the place of a stub without changing anyone else's code.

---

## 6. Rules to remember

1. **Edit only your own files.** The table "who edits which file" is in Section 4.1 of the handout.
2. **Never rename or remove a contract function.** Names, parameters and return types are fixed.
3. **Roles A to D never import each other's modules.** Only Role E's `main.py` and the integration tests do.
4. **Run `git pull` before `git push`.** Never use `git add .` and never use `git push --force`.
5. Write a **docstring** for every function, follow **PEP 8**, and never crash on bad input or a bad file.
6. **You must be able to explain every line of your own code** in the oral examination.

The usual Git routine:

```
git pull
git add storage.py test_storage.py     # add YOUR files, by name
git commit -m "Add load_data"
git pull
git push
```

---

## 7. Milestones

The dates below are **recommended milestones, not graded deadlines**. Missing one does not affect your marks, but the final repository must contain the evidence that the milestones were worked through (weekly `progress.md` entries, tests, peer reviews). Instructors can look at your repository at any time.

| Week | Suggested dates | What happens |
|---|---|---|
| 3 | 26.10 to 01.11 | Groups and roles final. Contract signed. Every module has a **stub** that passes the quick check. Role E pushes a menu stub. |
| 4 | 02.11 to 08.11 | Build your module, run `full` after each function, update your section of `progress.md`. |
| 5 | 09.11 to 15.11 | Mini-integration: Role A leads, Role E starts `python main.py` with the real modules that exist. |
| 6 | 16.11 to 22.11 | Your module passes `full`. Peer reviews are pushed. Roles A to D crash-test `main.py` and report to Role E. |
| 7 | 23.11 to 29.11 | Integration in six steps, freeze the code, submit on **Sunday 29.11, 23:59 CET**. |
| 8 | 30.11 and 02.12 | 5-minute group demo and individual oral questions. |

**Week 3 tasks by role:**

| Role | Week 3 team task |
|---|---|
| A | Create the private repository and invite the team. Fill in `contract.md`. Add `.gitignore`, `.gitattributes` and `requirements.txt` (at least `matplotlib`).  Push `storage.py` stub.|
| B | Copy `progress_template.md` to `progress.md`. Create the `design_patterns.md` skeleton. Push `habits.py` stub.|
| C | Push your `analytics.py` stub. |
| D | Create the `README.md` skeleton. Push `reports.py` stub |
| E | Push `main.py` and `utils.py` stubs |

A **stub** has the right function names, returns fixed values, and starts with the line `# STUB`. Delete that line when the file contains your real code.

---

## 8. Repository layout (final)

```
habit_tracker_group_XX/
    sample_data.py, check_contract.py     (from the instructor, never edited)
    storage.py  habits.py  analytics.py  reports.py  main.py  utils.py
    test_storage.py  test_habits.py  test_analytics.py  test_reports.py  test_utils.py
    test_integration_A.py ... test_integration_E.py
    README.md  contract.md  progress.md  design_patterns.md
    requirements.txt  .gitignore  .gitattributes
    notes/      note_A.md ... note_E.md
    reviews/    review_of_C_by_A.md, review_of_A_by_C.md, review_of_D_by_B.md,
                review_of_B_by_D.md, review_integration_tests_by_E.md
```

Tests use plain `assert` (no pytest). Temporary files made by unit tests start with `_test_unit_`, and by integration tests with `_test_int_`.

---

## 9. Design-pattern challenge (group)

Every group implements **two** of: Singleton, Factory Method, Strategy, Observer. A pattern counts when it is a **class in one student's own file**, a contract function uses it, and `python check_contract.py all full` still passes. The owner of the file writes the code, and the pattern is explained in `design_patterns.md`. All five students approve the choice. This topic is not taught in the course: treat it as independent research.

---

## 10. Hand-in and grading

| Part | Points | Who gets it |
|---|---|---|
| Group demo | 20 | Same for every student in the group |
| Individual role (module, unit and integration tests, team task, peer review, note, oral Q&A) | 70 | Each student separately |
| Design patterns | 10 | Same for every student in the group |

**Hand-in:** one **private** GitHub repository per group. Do not add the instructor until you receive an email with the GitHub username to add, then share the repository link on Moodle. Only commits made before the deadline count. On a fresh clone, `python main.py` must start and show the menu.

**Individual note** (`notes/note_X.md`, half a page plus pasted outputs): your role and what you built, what you learned on your own, one bug and its fix, the tools you used (books, websites, AI) and for what, your final checker and integration-test output, your review and your answer to the review of your work, and your file name.

---

## 11. AI tools and academic integrity

You may use AI tools to **learn new topics** and to **fix logical or syntax errors**. Describe in your note which tools you used and how. If you cannot explain your own code, or give wrong answers in the Q&A, your Q&A mark may suffer, and in serious cases it can count as an academic integrity violation. Copying another group's code is not allowed.

---

## 12. Common problems

| You see | What it means |
|---|---|
| `ModuleNotFoundError: No module named 'storage'` | The file is missing, or you are in the wrong folder. |
| `ModuleNotFoundError` for `pandas` or `matplotlib` | Run `pip install -r requirements.txt`. |
| `FAIL ... returns a float` | Return `0.5` or `0.0`, not `0` or `1`. |
| `import csv` gives a strange error | Look for a file named `csv.py` in your folder and rename it. |
| `git push` is rejected | Normal. Run `git pull`, then `git push` again. |
| The checker says `main` menu is not shown | Use the menu texts exactly as shown in the handout (for example "Add habit" and "Save and quit"). |

**Stuck for more than 2 days?** Ask a teammate first, then the instructor.
