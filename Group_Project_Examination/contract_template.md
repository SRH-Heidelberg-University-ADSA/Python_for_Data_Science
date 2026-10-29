# Group Contract: Habit Tracker

**How to use this file:**
1. Copy it and name the copy `contract.md`. Put it in your group repository.
2. In your Week 3 meeting, **Role A** fills in every `____` in **Sections 1, 3, and 5** (except the pattern table, which may be filled in later) while everybody is present, and pushes **once**. (One person edits, so Git has nothing to clash.) Then everybody runs `git pull`.
3. **Do not change Section 4.** The rules are the same for all groups.
4. After Role A's push and your `git pull`, each student signs **only in their own block** in Section 7, then runs `git pull` and `git push`.
5. After Week 3, role A may update only the Done boxes, the pattern table, and the change log (git pull first). These are not contract changes.

---

## 1. Our group

Use your university e-mail address.

**Group number:** ____  
**Group name (optional):** ____

| Role | File | Student name | GitHub username | Email |
|---|---|---|---|---|
| A: Storage | `storage.py` | ____ | ____ | ____ |
| B: Habit Manager | `habits.py` | ____ | ____ | ____ |
| C: Analytics | `analytics.py` | ____ | ____ | ____ |
| D: Reports and Charts | `reports.py` | ____ | ____ | ____ |
| E: Command-Line App | `main.py`, `utils.py` | ____ | ____ | ____ |

---

## 2. What we agree to build

- We build the Habit Tracker described in the project handout.
- We use the **exact function names, parameters, return types, and rules** in Section 2 (Role cards) of the handout.
- We use the **shared data format** in Section 1 of the handout: habit ids are text, dates are text in the format `YYYY-MM-DD`.
- We do not change `sample_data.py` or `check_contract.py`.
- We check our work with the instructor's checker: Roles A to D run `python check_contract.py <module> full`, Role E runs `python check_contract.py utils full` and `python check_contract.py main full`, and the group runs `python check_contract.py all full` (it does not include `main`).
- **Peer review:** in Week 6 we review each other's work as written in Section 4.6 of the handout (A reviews C, C reviews A, B reviews D, D reviews B, E reviews the four integration test files). A reviewer never edits the reviewed file.
- **Integration and testing are a team job.** Every student writes their own `test_integration_X.py` (at least 2 tests) and takes the team tasks of their role (see Section 2 of the handout).

---

## 3. Our working agreements

**Python version we all use:** ____ (3.10 or newer, for example 3.12)  
**Name of the data file:** `habits.json`

**Weekly group check-in (about 10 minutes)**
- Day and time: ____
- Where (in person / online, which tool): ____
- Who reminds the group: ____

**Weekly update in `progress.md`**
- Every student writes in their own section by (day): ____
- We write: what is done, what is blocked.

**How we talk:** (chat group, email, ...) ____

**How we work with Git**
- Each student changes **only their own files** and their own section of the shared files.
- We run `git pull` before `git push`. Everybody ran `git config --global pull.rebase false` once.
- We never use `git add .` and never use `git push --force`.
- We follow the table in Rule 1 of Section 4.1 ("Git without clashes") of the handout.
- Our repository is at: ____ (it is **private** and the instructor is added as a collaborator)

**If someone is stuck for more than 2 days:** first we ask a teammate, and then we ask the instructor.

**Our plan for the design-pattern challenge** (you can fill this in later, but write the date):

The **group** is required to implement 2 design-patterns. See Section 5 of the handout. All five students approve each choice. The pattern's class lives in **one student's own file** (one of `storage.py`, `habits.py`, `analytics.py`, `reports.py`, `utils.py`, because `python check_contract.py all full` does not run `main.py`), and that student writes the code.

| Pattern | Student who owns the file (role) | Which file and function | Date decided |
|---|---|---|---|
| 1: ____ | ____ | ____ | ____ |
| 2: ____ | ____ | ____ | ____ |

---

## 4. Our rules (fixed, do not change)

**Rule 1: The contract is locked after Week 3.**
A change is allowed only if **all five** students agree, and it must be written in the change log in Section 6. A change may only **add** something. We never rename or remove a function, because the instructor's checker does not change.

**Rule 2: Missing module rule.**
If a student does not deliver a real module, the group keeps that student's **stub** (a file that still starts with `# STUB`), so the app still starts. A stub earns no marks for that module. The demo will be incomplete, so the **group mark** goes down. The **individual marks of the other four students are not affected.**

**Rule 3: Own work and independence.**
Every student writes their own module. Nobody edits another student's file. Roles A to D do not import each other's modules inside their modules or unit tests. Only Role E's `main.py` and the integration test files (`test_integration_X.py`) do. A reviewer writes comments in their own review file and never edits the reviewed file. If you find a bug in a teammate's module, send a short report: **function, input, expected result, real result.**

---

## 5. Our milestones

Write the calendar date of each milestone. The handout gives week numbers (use the course calendar). The dates of the submission and of the demo are fixed and already written below. Tick each box when it is done.

| Milestone | Date | Done |
|---|---|---|
| Week 3, part 1: groups and roles final | ____ | [ ] |
| Week 3, part 2: contract signed, Roles A to D stubs (quick check passes); Role E menu stub, `.gitignore`, `.gitattributes` and `requirements.txt` added (Role A), README.md skeleton (Role D); `progress.md` copied and `design_patterns.md` skeleton created (Role B) | ____ | [ ] |
| Week 5: mini-integration (led by Role A) | ____ | [ ] |
| End of Week 6: every module passes its `full` check, every student has pushed their `test_integration_X.py` and their peer review | ____ | [ ] |
| Week 7, part 1: integration done (all five integration tests pass) and code frozen (freeze checklist done by all) | ____ | [ ] |
| Submission | Sunday 29.11.2026, 23:59 CET | [ ] |
| Demo and oral examination | 30.11.2026 or 02.12.2026 (time slot confirmed later: ____) | [ ] |

---

## 6. Change log

Write every change after Week 3 here. All **five students** *must agree*. Use initials. Role A writes the entry only after all five students agreed in writing (group chat or GitHub comment); the initials show who agreed.

| Date | What we added or changed (and why) | Agreed by (all 5 initials) |
|---|---|---|
| ____ | ____ | ____ |

---

## 7. Signatures

By typing my name and the date, I confirm that I have read this contract and that I agree to Sections 1 to 5.

**Role A**  
Name: ____   Date: ____

---

**Role B**  
Name: ____   Date: ____

---

**Role C**  
Name: ____   Date: ____

---

**Role D**  
Name: ____   Date: ____

---

**Role E**  
Name: ____   Date: ____
