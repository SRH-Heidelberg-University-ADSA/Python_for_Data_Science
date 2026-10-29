# Progress Log: Habit Tracker

**Group number:** ____

**How to use this file:**
1. **Role B** copies it, names the copy `progress.md` and puts it in your group repository (Week 3).
2. Update **your own section** once a week, on the day you chose in your contract. Do not edit another student's section.
3. Keep it short: one or two lines in each cell.
4. Run `git pull` right before you edit this file and again before `git push`, so that you work on the latest version (or edit the file in the browser on GitHub, which always uses the latest version). If Git shows a conflict, keep **both** versions and follow the steps in the handout (Section 4.1, "Git without clashes").

**Integration test** means the state of your own `test_integration_X.py`. Write it like this: `not started`, `2 written, 1 passes`, or `2 written, 2 pass`.

**Checker result** means the last result of `python check_contract.py <module>` (quick) or `python check_contract.py <module> full`. Write it like this: `quick: 4 passed, 0 failed` or `full: 9 passed, 3 failed`. Role E writes two results, for `utils` and for `main`, for example `utils full: 14 passed, 0 failed; main full: 23 passed, 0 failed`.

**Example row:**

| Week | Done this week | Blocked / need help | Plan for next week | Checker result | Integration test |
|---|---|---|---|---|---|
| 4 | `add_habit` and `remove_habit` work. Wrote 2 tests. | `mark_done`: it accepts a date in the future. | Read about `datetime.date.today()`. Fix `mark_done`. | `full: 22 passed, 9 failed` | not started |

---

## Group section (Role B updates this section)

**Weekly check-ins**

| Week | Did we meet? (yes / no) | Main decision or problem |
|---|---|---|
| 4 | ____ | ____ |
| 5 | ____ | ____ |
| 6 | ____ | ____ |
| 7 | ____ | ____ |

**Week 5 mini-integration** (which real modules did we have, what worked, what failed; Role A tells Role B, Role B writes it):

____

**Week 6 peer reviews** (are all 5 reviews pushed? what did the owners change afterwards?):

____

**Week 7 integration** (which problems did we find, who fixed them; did all five integration tests pass?):

____

**Final check before submission** (Role C runs it and posts it; Role B pastes the last lines of `python check_contract.py all full` and of `python check_contract.py main full`):

```
____
```

---

## Role A: Storage (`storage.py`)

**Name:** ____

**Team tasks:** `contract.md` (Week 3), `.gitignore`, `.gitattributes`, `requirements.txt`, lead the Week 5 mini-integration.  
**Integration test:** `test_integration_A.py`  
**Review task (Week 6):** review `analytics.py` (Role C) -> `reviews/review_of_C_by_A.md`

| Week | Done this week | Blocked / need help | Plan for next week | Checker result | Integration test |
|---|---|---|---|---|---|
| 3 (stub) | ____ | ____ | ____ | ____ | ____ |
| 4 | ____ | ____ | ____ | ____ | ____ |
| 5 | ____ | ____ | ____ | ____ | ____ |
| 6 | ____ | ____ | ____ | ____ | ____ |
| 7 | ____ | ____ | ____ | ____ | ____ |

---

## Role B: Habit Manager (`habits.py`)

**Name:** ____

**Team tasks:** in Week 3 copy `progress_template.md` to `progress.md` and create the `design_patterns.md` skeleton; keep the group section of this file; write the Week 5 lines.  
**Integration test:** `test_integration_B.py`  
**Review task (Week 6):** review `reports.py` (Role D) -> `reviews/review_of_D_by_B.md`

| Week | Done this week | Blocked / need help | Plan for next week | Checker result | Integration test |
|---|---|---|---|---|---|
| 3 (stub) | ____ | ____ | ____ | ____ | ____ |
| 4 | ____ | ____ | ____ | ____ | ____ |
| 5 | ____ | ____ | ____ | ____ | ____ |
| 6 | ____ | ____ | ____ | ____ | ____ |
| 7 | ____ | ____ | ____ | ____ | ____ |

---

## Role C: Analytics (`analytics.py`)

**Name:** ____

**Team tasks:** run `python check_contract.py all full` and `python check_contract.py main full` in Week 7 and post both outputs.  
**Integration test:** `test_integration_C.py`  
**Review task (Week 6):** review `storage.py` (Role A) -> `reviews/review_of_A_by_C.md`

| Week | Done this week | Blocked / need help | Plan for next week | Checker result | Integration test |
|---|---|---|---|---|---|
| 3 (stub) | ____ | ____ | ____ | ____ | ____ |
| 4 | ____ | ____ | ____ | ____ | ____ |
| 5 | ____ | ____ | ____ | ____ | ____ |
| 6 | ____ | ____ | ____ | ____ | ____ |
| 7 | ____ | ____ | ____ | ____ | ____ |

---

## Role D: Reports and Charts (`reports.py`)

**Name:** ____

**Team tasks:** `README.md` (skeleton in Week 3, install, run, example session).  
**Integration test:** `test_integration_D.py`  
**Review task (Week 6):** review `habits.py` (Role B) -> `reviews/review_of_B_by_D.md`

| Week | Done this week | Blocked / need help | Plan for next week | Checker result | Integration test |
|---|---|---|---|---|---|
| 3 (stub) | ____ | ____ | ____ | ____ | ____ |
| 4 | ____ | ____ | ____ | ____ | ____ |
| 5 | ____ | ____ | ____ | ____ | ____ |
| 6 | ____ | ____ | ____ | ____ | ____ |
| 7 | ____ | ____ | ____ | ____ | ____ |

---

## Role E: Command-Line App (`main.py`, `utils.py`)

**Name:** ____

**Team tasks:** none beyond the app.  
**Integration test:** `test_integration_E.py`  
**Review task (Week 6):** review the four integration test files -> `reviews/review_integration_tests_by_E.md`; fix the crash-test reports from Roles A to D

Role E has two checks: `python check_contract.py utils` (`full`) for `utils.py` and `python check_contract.py main` (`full`) for the app. Write both results in the column "Checker result". In the column "What works in the app", write what works in `main.py` (for example: "menu 1 to 3 work with the stubs").

| Week | Done this week | Blocked / need help | Plan for next week | Checker result (`utils` / `main`) | What works in the app | Integration test |
|---|---|---|---|---|---|---|
| 3 (stub) | ____ | ____ | ____ | ____ | ____ | ____ |
| 4 | ____ | ____ | ____ | ____ | ____ | ____ |
| 5 | ____ | ____ | ____ | ____ | ____ | ____ |
| 6 | ____ | ____ | ____ | ____ | ____ | ____ |
| 7 | ____ | ____ | ____ | ____ | ____ | ____ |
