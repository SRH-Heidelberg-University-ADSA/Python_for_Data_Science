"""check_contract.py - a simple checker for the Habit Tracker project.

Put this file and sample_data.py in the same folder as your module.

How to run it (replace 'storage' with habits, analytics, reports, utils, or all):

    python check_contract.py storage         QUICK check: do the functions exist
                                             and return the right type?
    python check_contract.py storage full    FULL check: are the results correct?
    python check_contract.py all full        FULL check of storage, habits, analytics,
                                             reports and utils (NOT main)
    python check_contract.py utils           QUICK check of Role E's input helpers
    python check_contract.py main            QUICK check of the app: does it start,
                                             show the menu and quit with option 0?
    python check_contract.py main full       FULL check of the app: bad input, end of
                                             input, demo data, broken data files,
                                             options 5 to 8 with data
    python check_contract.py stubs           Which files still start with # STUB?

Use QUICK for your week 3 stub. Use FULL for your real code.
(On macOS or Linux you may need to type python3 instead of python.)

'main' is a separate command and is not part of 'all', because it runs the
whole app and depends on the work of all the other roles.
"""
import contextlib
import copy
import csv
import importlib
import io
import json
import os
import re
import subprocess
import sys
import tempfile
from datetime import date, timedelta
from unittest.mock import patch

from sample_data import make_test_data

# The handout (Role E card, "Fixed order of questions") fixes the order of the
# questions asked by menu options 1 and 3 (option 1: name; option 3: habit id,
# then date). Keep this True. Set it to False only if the handout changes.
PROMPT_ORDER_FIXED = True

HERE = os.path.dirname(os.path.abspath(__file__))
EMPTY = {"habits": {}, "log": {}}
TEMP_FILES = [
    "_check_tmp.json",
    "_check_tmp.csv",
    "_check_tmp.txt",
    "_check_bad.json",
    "_check_tmp.png",
]

# A valid date in the past that is NOT in the test data for habits 1 and 4.
TEST_DAY = (date.today() - timedelta(days=20)).isoformat()

# A date after today. mark_done must refuse it and analytics must ignore it.
FUTURE_DAY = (date.today() + timedelta(days=1)).isoformat()

# Date texts that are NOT valid (see the handout, Section 1.1).
BAD_DATES = ["2026-1-5", "20261005", "2026-W41-1", "05.01.2026", "2026-02-30"]

passed = 0
failed = 0


def check(label, condition):
    """Print PASS or FAIL for one check."""
    global passed, failed
    if condition:
        passed += 1
        print("  PASS ", label)
    else:
        failed += 1
        print("  FAIL ", label)


def cleanup():
    """Delete the temporary files made by the checks."""
    for name in TEMP_FILES:
        if os.path.exists(name):
            os.remove(name)


def read_file(name):
    with open(name, encoding="utf-8") as file:
        return file.read()


# ------------------------------------------------------------ storage.py
def part_load_data(storage, full):
    check("load_data returns a dict", type(storage.load_data("no_such_file.json")) == dict)
    if full:
        check("a missing file gives empty data", storage.load_data("no_such_file.json") == EMPTY)
        with open("_check_bad.json", "w", encoding="utf-8") as file:
            file.write("{this is not json")
        check("a broken file gives empty data", storage.load_data("_check_bad.json") == EMPTY)
        for label, text in [("an empty file", ""),
                            ("JSON with the wrong structure", "[1, 2, 3]"),
                            ("JSON without the key 'log'", '{"habits": {}}'),
                            ("JSON where 'habits' or 'log' is not a dictionary",
                             '{"habits": [], "log": []}')]:
            with open("_check_bad.json", "w", encoding="utf-8") as file:
                file.write(text)
            check(label + " gives empty data", storage.load_data("_check_bad.json") == EMPTY)
        first = storage.load_data("no_such_file.json")
        first["habits"]["x"] = {"name": "x", "created": TEST_DAY}
        check("load_data returns a NEW empty dict on every call",
              storage.load_data("no_such_file.json") == EMPTY)


def part_save_data(storage, full):
    data, answers = make_test_data()
    check("save_data returns True or False", type(storage.save_data(data, "_check_tmp.json")) == bool)
    if full:
        check("save then load gives the same data", storage.load_data("_check_tmp.json") == data)
        check("save_data returns False for a missing folder", storage.save_data(data, "no_such_folder/x.json") is False)


def part_export_csv(storage, full):
    data, answers = make_test_data()
    check("export_csv returns True or False", type(storage.export_csv(data, "_check_tmp.csv")) == bool)
    if full:
        lines = read_file("_check_tmp.csv").splitlines()
        check("the CSV header is habit_id,name,date", lines[:1] == ["habit_id,name,date"])
        check("the CSV has one row per completed date (48)", len(lines) - 1 == 48)
        odd = {"habits": {"1": {"name": "Fr\u00fch, aufstehen", "created": TEST_DAY}},
               "log": {"1": [TEST_DAY]}}
        storage.export_csv(odd, "_check_tmp.csv")
        with open("_check_tmp.csv", encoding="utf-8", newline="") as file:
            rows = list(csv.reader(file))
        check("export_csv handles umlauts and commas in a name",
              len(rows) == 2 and rows[1][1] == "Fr\u00fch, aufstehen")
        orphan = {"habits": {"1": {"name": "Read", "created": TEST_DAY}},
                  "log": {"1": [TEST_DAY], "99": [TEST_DAY]}}
        storage.export_csv(orphan, "_check_tmp.csv")
        with open("_check_tmp.csv", encoding="utf-8", newline="") as file:
            rows = list(csv.reader(file))
        check("export_csv skips log entries of ids that are not habits", len(rows) == 2)
        check("export_csv returns False for a missing folder",
              storage.export_csv(data, "no_such_folder/x.csv") is False)


# ------------------------------------------------------------- habits.py
def part_add_habit(habits, full):
    data, answers = make_test_data()
    check("add_habit returns a string", type(habits.add_habit(data, "Test")) == str)
    if full:
        data, answers = make_test_data()
        new_id = habits.add_habit(data, "Stretch")
        check("add_habit gives a NEW id and stores the habit",
              new_id not in ["1", "2", "3", "4", "5"] and new_id in data["habits"])
        check("add_habit stores the name", data["habits"].get(new_id, {}).get("name") == "Stretch")

        data, answers = make_test_data()
        check("add_habit returns '' for a blank name", habits.add_habit(data, "   ") == "")
        check("a blank name adds nothing", len(data["habits"]) == 5)

        data = copy.deepcopy(EMPTY)
        first_id = habits.add_habit(data, "  Read  ")
        check("the first habit in empty data gets the id '1'", first_id == "1")
        check("add_habit removes spaces around the name",
              data["habits"].get(first_id, {}).get("name") == "Read")
        before = date.today().isoformat()
        data = copy.deepcopy(EMPTY)
        new_id = habits.add_habit(data, "Read")
        after = date.today().isoformat()
        check("'created' is today's date as text",
              data["habits"].get(new_id, {}).get("created") in (before, after))

        data = {"habits": {"1": {"name": "A", "created": TEST_DAY},
                           "3": {"name": "B", "created": TEST_DAY},
                           "abc": {"name": "C", "created": TEST_DAY}}, "log": {}}
        check("the new id is the highest number + 1 (ids that are not digits are ignored)",
              habits.add_habit(data, "D") == "4")

        data = copy.deepcopy(EMPTY)
        id_1 = habits.add_habit(data, "Read")
        id_2 = habits.add_habit(data, "Read")
        check("two habits with the same name get two different ids",
              id_1 != id_2 and len(data["habits"]) == 2)


def part_remove_habit(habits, full):
    data, answers = make_test_data()
    check("remove_habit returns True or False", type(habits.remove_habit(data, "1")) == bool)
    if full:
        data, answers = make_test_data()
        check("remove_habit returns True", habits.remove_habit(data, "1") is True)
        check("the habit is gone from data['habits']", "1" not in data["habits"])
        check("the habit's log is gone too", "1" not in data["log"])
        check("remove_habit returns False for an unknown id", habits.remove_habit(data, "999") is False)
        check("the other habits and their logs stay",
              len(data["habits"]) == 4 and "2" in data["log"] and "5" in data["log"])


def part_list_habits(habits, full):
    data, answers = make_test_data()
    check("list_habits returns a list", type(habits.list_habits(data)) == list)
    if full:
        items = habits.list_habits(data)
        check("list_habits gives 5 habits", len(items) == 5)
        check("list_habits contains ('1', 'Read')", ("1", "Read") in items or ["1", "Read"] in items)
        ordered = {"habits": {"1": {"name": "A", "created": TEST_DAY},
                              "2": {"name": "B", "created": TEST_DAY},
                              "10": {"name": "C", "created": TEST_DAY}}, "log": {}}
        check("list_habits keeps the stored order (does not sort the ids as text)",
              [item[0] for item in habits.list_habits(ordered)] == ["1", "2", "10"])


def part_mark_done(habits, full):
    data, answers = make_test_data()

    check(
        "mark_done returns True or False",
        type(habits.mark_done(data, "1", TEST_DAY)) == bool,
    )

    if full:
        data, answers = make_test_data()

        check(
            "mark_done returns True for a new date",
            habits.mark_done(data, "1", TEST_DAY) is True,
        )
        check(
            "the date is in the log",
            TEST_DAY in data["log"]["1"],
        )
        check(
            "the same date twice returns False",
            habits.mark_done(data, "1", TEST_DAY) is False,
        )
        check(
            "the date is not added twice",
            data["log"]["1"].count(TEST_DAY) == 1,
        )
        check(
            "an unknown id returns False",
            habits.mark_done(data, "999", TEST_DAY) is False,
        )
        check(
            "works for a habit with no log yet",
            habits.mark_done(data, "4", TEST_DAY) is True,
        )
        check(
            "an invalid date format returns False",
            all(
                habits.mark_done(data, "1", bad) is False
                for bad in BAD_DATES + [""]
            ),
        )
        check(
            "an invalid date is not stored",
            "20261005" not in data["log"]["1"],
        )
        check(
            "a date in the future returns False",
            habits.mark_done(data, "1", FUTURE_DAY) is False,
        )
        check(
            "a date in the future is not stored",
            FUTURE_DAY not in data["log"]["1"],
        )


# ---------------------------------------------------------- analytics.py
def part_current_streak(analytics, full):
    data, answers = make_test_data()
    check("current_streak returns an int", type(analytics.current_streak(data, "1")) == int)
    if full:
        right = True
        for habit_id in answers["current_streak"]:
            if analytics.current_streak(data, habit_id) != answers["current_streak"][habit_id]:
                right = False
        check("current_streak gives the right answers", right)


def part_longest_streak(analytics, full):
    data, answers = make_test_data()
    check("longest_streak returns an int", type(analytics.longest_streak(data, "1")) == int)
    if full:
        right = True
        for habit_id in answers["longest_streak"]:
            if analytics.longest_streak(data, habit_id) != answers["longest_streak"][habit_id]:
                right = False
        check("longest_streak gives the right answers", right)


def part_completion_rate(analytics, full):
    data, answers = make_test_data()

    check(
        "completion_rate returns a float (like 0.5)",
        type(analytics.completion_rate(data, "1", 10)) == float,
    )

    if full:
        right = True
        for habit_id, days, wanted in answers["completion_rate"]:
            rate = analytics.completion_rate(data, habit_id, days)
            if abs(rate - wanted) > 0.01:
                right = False

        check(
            "completion_rate gives the right answers",
            right,
        )

        # The result is a decimal between 0.0 and 1.0, also for a
        # window longer than the data.
        in_range = True
        for habit_id in data["habits"]:
            for days in [1, 3, 30, 60]:
                rate = analytics.completion_rate(data, habit_id, days)
                if not (0.0 <= rate <= 1.0):
                    in_range = False

        check(
            "completion_rate is not rounded (10 of 30 days is 0.333...)",
            abs(analytics.completion_rate(data, "2", 30) - 10 / 30) < 0.001,
        )

        check(
            "completion_rate is always between 0.0 and 1.0",
            in_range,
        )

        check(
            "completion_rate is 0.0 for days <= 0",
            analytics.completion_rate(data, "1", 0) == 0.0
            and analytics.completion_rate(data, "1", -5) == 0.0,
        )

        check(
            "unknown id gives 0 / 0.0 (right types)",
            type(analytics.completion_rate(data, "999", 10)) == float
            and analytics.completion_rate(data, "999", 10) == 0.0
            and analytics.current_streak(data, "999") == 0
            and analytics.longest_streak(data, "999") == 0,
        )

        data["log"]["99"] = [date.today().isoformat()]  # log entry, but no habit
        check(
            "an id that is only in the log (not in habits) is unknown: 0 / 0.0",
            analytics.current_streak(data, "99") == 0
            and analytics.longest_streak(data, "99") == 0
            and analytics.completion_rate(data, "99", 10) == 0.0,
        )


def part_weekly_summary(analytics, full):
    data, answers = make_test_data()
    check("weekly_summary returns a dict", type(analytics.weekly_summary(data)) == dict)
    if full:
        check("weekly_summary gives the right answers",
              analytics.weekly_summary(data) == answers["weekly_summary"])
        data["log"]["99"] = [date.today().isoformat()]
        check("weekly_summary ignores log entries of habits that do not exist",
              analytics.weekly_summary(data) == answers["weekly_summary"])


def part_bad_log_entries(analytics, full):
    if full:
        data, answers = make_test_data()
        # Habit "1" was done on the last 5 days. Add three bad entries:
        # text that is not a date, a duplicate, and a date in the future.
        data["log"]["1"] += ["not-a-date", data["log"]["1"][0], FUTURE_DAY]
        check("invalid, duplicate and future log entries are ignored",
              analytics.current_streak(data, "1") == 5
              and analytics.longest_streak(data, "1") == 5
              and analytics.weekly_summary(data)["1"] == 5
              and abs(analytics.completion_rate(data, "1", 10) - 0.5) < 0.01)


def part_data_unchanged(analytics, full):
    if full:
        data, answers = make_test_data()
        before = str(data)
        analytics.current_streak(data, "2")
        analytics.longest_streak(data, "2")
        analytics.completion_rate(data, "2", 10)
        analytics.weekly_summary(data)
        check("the functions do not change the data", str(data) == before)


# ------------------------------------------------------------ reports.py
def part_text_chart(reports, full):
    check("text_chart returns a string", type(reports.text_chart({"Read": 5})) == str)
    if full:
        chart = reports.text_chart({"Read": 5, "Run": 3})
        check("text_chart shows every label", "Read" in chart and "Run" in chart)
        check("text_chart gives a message for empty input", reports.text_chart({}).strip() != "")
        big = reports.text_chart({"Big": 1000, "Small": 10})
        longest = max((line.count("#") for line in big.splitlines()), default=0)
        check("text_chart: the longest bar is made of 1 to 40 '#' characters", 0 < longest <= 40)
        small = [line for line in big.splitlines() if "Small" in line]
        check("text_chart: every value above 0 gets at least one '#'",
              bool(small) and small[0].count("#") >= 1)
        check("text_chart does not crash when all values are 0",
              type(reports.text_chart({"A": 0, "B": 0})) == str)


def part_save_chart_image(reports, full):
    check("save_chart_image returns True or False",
          type(reports.save_chart_image({"Read": 5}, "_check_tmp.png")) == bool)
    if full:
        if os.path.exists("_check_tmp.png"):
            os.remove("_check_tmp.png")
        done = reports.save_chart_image({"Read": 5, "Run": 3}, "_check_tmp.png")
        check("save_chart_image creates a PNG file",
              done is True and os.path.exists("_check_tmp.png")
              and os.path.getsize("_check_tmp.png") > 0)
        check("save_chart_image returns False for a missing folder",
              reports.save_chart_image({"Read": 5}, "no_such_folder/x.png") is False)


def part_build_report(reports, full):
    data, answers = make_test_data()
    check("build_report returns a string", type(reports.build_report(data)) == str)
    if full:
        report = reports.build_report(data)
        all_names_found = True
        for habit in data["habits"].values():
            if habit["name"] not in report:
                all_names_found = False
        check("build_report lists every habit", all_names_found)
        check("build_report works for empty data",
              reports.build_report(copy.deepcopy(EMPTY)).strip() != "")
        twin = {"habits": {"1": {"name": "Read", "created": TEST_DAY},
                           "2": {"name": "Read", "created": TEST_DAY}}, "log": {}}
        check("build_report shows two habits with the same name",
              reports.build_report(twin).count("Read") >= 2)


def part_report_numbers(reports, full):
    if not full:
        return
    def day(days_ago):
        return (date.today() - timedelta(days=days_ago)).isoformat()

    data = {"habits": {"8": {"name": "Zebra", "created": day(30)}},
            "log": {"8": [day(0), day(0), FUTURE_DAY, "not-a-date", day(3), day(10)]}}
    lines = [line for line in reports.build_report(data).splitlines() if "Zebra" in line]
    has_right = any(re.search(r"\b3\b", line) and re.search(r"\b2\b", line) for line in lines)
    has_wrong = any(re.search(r"\b[456]\b", line) for line in lines)
    check("build_report: the line of a habit shows 3 days in total and 2 in the last 7 days",
          has_right)
    check("build_report ignores invalid, duplicate and future log entries", not has_wrong)


def part_save_report(reports, full):
    check("save_report returns True or False", type(reports.save_report("hi", "_check_tmp.txt")) == bool)
    if full:
        reports.save_report("hello report", "_check_tmp.txt")
        check("save_report writes the text to the file", read_file("_check_tmp.txt") == "hello report")
        text = "Fr\u00fch \u2713"
        reports.save_report(text, "_check_tmp.txt")
        with open("_check_tmp.txt", "rb") as file:
            raw = file.read()
        check("save_report writes UTF-8 (umlauts and symbols)", raw == text.encode("utf-8"))


# -------------------------------------------------------------- utils.py
def feed(func, answers, *args):
    """Call func(*args) while input() returns the given answers one by one."""
    with patch("builtins.input", side_effect=list(answers)):
        with contextlib.redirect_stdout(io.StringIO()):
            return func(*args)


def part_ask_int(utils, full):
    check("ask_int returns an int", type(feed(utils.ask_int, ["3"], "n? ", 1, 5)) == int)
    if full:
        check("ask_int asks again after wrong input and out-of-range numbers",
              feed(utils.ask_int, ["abc", "", "2.5", "99", "0", "3"], "n? ", 1, 5) == 3)
        check("ask_int accepts both limits",
              feed(utils.ask_int, ["1"], "n? ", 1, 5) == 1
              and feed(utils.ask_int, ["5"], "n? ", 1, 5) == 5)


def part_ask_date(utils, full):
    check("ask_date returns text (a str)", type(feed(utils.ask_date, [TEST_DAY], "d? ")) == str)
    if full:
        check("ask_date returns the date as typed", feed(utils.ask_date, [TEST_DAY], "d? ") == TEST_DAY)
        check("ask_date refuses every wrong format and asks again",
              feed(utils.ask_date, BAD_DATES + [TEST_DAY], "d? ") == TEST_DAY)
        before = date.today().isoformat()
        got = feed(utils.ask_date, [""], "d? ")
        after = date.today().isoformat()
        check("ask_date: an empty line means today", got in (before, after))


def part_ask_yes_no(utils, full):
    check("ask_yes_no returns a bool", type(feed(utils.ask_yes_no, ["y"], "? ")) == bool)
    if full:
        check("ask_yes_no: y, yes and Y mean True",
              all(feed(utils.ask_yes_no, [a], "? ") is True for a in ["y", "yes", "Y"]))
        check("ask_yes_no: n, no and NO mean False",
              all(feed(utils.ask_yes_no, [a], "? ") is False for a in ["n", "no", "NO"]))
        check("ask_yes_no asks again after another answer",
              feed(utils.ask_yes_no, ["maybe", "", "1", "y"], "? ") is True)


def part_ask_text(utils, full):
    if not hasattr(utils, "ask_text"):
        print("  (ask_text is optional and was not found: skipped)")
        return
    check("ask_text returns a str", type(feed(utils.ask_text, ["Read"], "t? ")) == str)
    if full:
        check("ask_text asks again after an empty line",
              feed(utils.ask_text, ["", "Read"], "t? ").strip() == "Read")


class _TooManyAsks(Exception):
    """Raised by the fake input() when a helper asks again and again."""


def part_end_of_input(utils, full):
    if not full:
        return
    helpers = [("ask_int", ("n? ", 1, 5)), ("ask_date", ("d? ",)),
               ("ask_yes_no", ("y? ",)), ("ask_text", ("t? ",))]
    for name, args in helpers:
        func = getattr(utils, name, None)
        if func is None:
            continue
        calls = []

        def fake_input(prompt=""):
            calls.append(1)
            if len(calls) > 50:
                raise _TooManyAsks()
            raise EOFError

        outcome = "returned a value"
        try:
            with patch("builtins.input", fake_input):
                with contextlib.redirect_stdout(io.StringIO()):
                    func(*args)
        except EOFError:
            outcome = "ok"
        except _TooManyAsks:
            outcome = "asked again forever"
        except Exception as error:
            outcome = type(error).__name__
        check(name + " lets EOFError through at the end of input (no endless loop)",
              outcome == "ok")
        if outcome != "ok":
            print("        It", outcome)


# ------------------------------------------------------------------ main
def run_app(answers, args=("_check_tmp.json",), setup=None, folder=None):
    """Run main.py with the answers. Return (result, saved), or (None, None) after a timeout.

    'saved' is the content of _check_tmp.json afterwards: a dict, the text
    'broken' if it is not valid JSON, or None if the file does not exist.
    """
    if folder is None:
        with tempfile.TemporaryDirectory(ignore_cleanup_errors=True) as new_folder:
            return run_app(answers, args, setup, new_folder)
    if setup:
        setup(folder)
    env = dict(os.environ, PYTHONUTF8="1", PYTHONIOENCODING="utf-8")
    text = "".join(answer + "\n" for answer in answers)
    try:
        result = subprocess.run(
            [sys.executable, os.path.join(HERE, "main.py"), *args],
            input=text, capture_output=True, text=True, encoding="utf-8",
            errors="replace", timeout=15, cwd=folder, env=env)
    except subprocess.TimeoutExpired:
        return None, None
    saved = None
    path = os.path.join(folder, "_check_tmp.json")
    if os.path.exists(path):
        try:
            with open(path, encoding="utf-8") as file:
                saved = json.load(file)
        except ValueError:
            saved = "broken"
    return result, saved


def clean_exit(result):
    """True if the app ended with exit code 0 and no Traceback."""
    return result is not None and result.returncode == 0 and "Traceback" not in result.stderr


def check_run(label, answers, **kwargs):
    """Run the app, check that it ended cleanly, return (result, saved)."""
    result, saved = run_app(answers, **kwargs)
    check(label + " (exit code 0, no Traceback, no hang)", clean_exit(result))
    if result is None:
        print("        The app did not stop within 15 seconds.")
    elif not clean_exit(result):
        lines = result.stderr.strip().splitlines()
        print("        Exit code", result.returncode, "-", lines[-1] if lines else "no error text")
    return result, saved


def is_data(saved):
    """True if saved looks like the data dictionary."""
    return (isinstance(saved, dict) and isinstance(saved.get("habits"), dict)
            and isinstance(saved.get("log"), dict))


def part_main_start(_, full):
    result, saved = check_run("main.py starts and option 0 quits", ["0"])
    shown = result.stdout.lower() if result is not None else ""
    check("the menu is shown", "add habit" in shown and "save and quit" in shown)
    if full:
        check("option 0 saves the data file (JSON with 'habits' and 'log')", is_data(saved))


def part_main_end_of_input(_, full):
    if full:
        result, saved = check_run("end of input (Ctrl+D) quits like option 0", [])
        check("end of input saves the data file", is_data(saved))


def part_main_bad_input(_, full):
    if full:
        wrong = ["abc", "99", "-1", "", "   ", "99999999999999999999", "\u00e4\u00f6", "0"]
        check_run("wrong menu input is refused", wrong)


def part_main_empty_options(_, full):
    if full:
        for option in ["2", "3", "4", "5", "6", "7", "8"]:
            check_run("menu option " + option + " with no habits does not crash",
                      [option, "n", "0"])


def part_main_demo(_, full):
    if full:
        result, saved = check_run("option 9 + yes loads the demo data", ["9", "y", "0"])
        check("the demo data has 10 habits", is_data(saved) and len(saved["habits"]) == 10)
        result, saved = check_run("option 9 + no keeps the data", ["9", "n", "0"])
        check("answering no changes nothing", is_data(saved) and len(saved["habits"]) == 0)


def part_main_files(_, full):
    if full:
        check_run("a data file in a missing folder does not crash the app", ["0"],
                  args=("no_such_folder/x.json",))

        def write_broken(folder):
            with open(os.path.join(folder, "_check_tmp.json"), "w", encoding="utf-8") as file:
                file.write("{this is not json")

        check_run("a broken data file does not crash the app", ["0"], setup=write_broken)


def part_main_journey(_, full):
    if not full:
        return
    if not PROMPT_ORDER_FIXED:
        print("  (journey skipped: PROMPT_ORDER_FIXED is False in check_contract.py)")
        return
    today = date.today().isoformat()
    with tempfile.TemporaryDirectory(ignore_cleanup_errors=True) as folder:
        result, saved = check_run("a journey (add, mark done, report, quit)",
                                  ["1", "Read", "3", "1", "", "6", "n", "0"], folder=folder)
        check("the habit and today's date are saved",
              is_data(saved) and saved["habits"].get("1", {}).get("name") == "Read"
              and today in saved["log"].get("1", []))
        result, saved = check_run("a second start of the app", ["0"], folder=folder)
        check("the data is still there after a restart",
              is_data(saved) and today in saved["log"].get("1", []))


def part_main_options_with_data(_, full):
    """Options 5 to 8 with real data (10 demo habits), and option 6 with 'y'."""
    if not full:
        return
    names = ["Read", "Exercise", "Meditate", "Journal", "Drink water"]
    # Option 5: statistics for every habit (answers: demo data, yes, option 5).
    result, saved = check_run("option 5 (statistics) with 10 habits does not crash",
                              ["9", "y", "5", "0"])
    shown = result.stdout if result is not None else ""
    check("option 5 shows the habits of the demo data", all(n in shown for n in names))
    # Options 6, 7 and 8 with 10+ habits. Option 6 asks 'Save a chart image?'
    # (answer n), options 7 and 8 ask nothing.
    with tempfile.TemporaryDirectory(ignore_cleanup_errors=True) as folder:
        result, saved = check_run("options 6, 7 and 8 with 10 habits do not crash",
                                  ["9", "y", "6", "n", "7", "8", "0"], folder=folder)
        report_path = os.path.join(folder, "report.txt")
        csv_path = os.path.join(folder, "habits.csv")
        check("option 7 writes report.txt with the habit names",
              os.path.exists(report_path)
              and all(n in read_file(report_path) for n in names))
        check("option 8 writes habits.csv with the header habit_id,name,date",
              os.path.exists(csv_path)
              and read_file(csv_path).splitlines()[:1] == ["habit_id,name,date"])
        check("the demo data is still saved after these options",
              is_data(saved) and len(saved["habits"]) == 10)
    # Option 6 with 'y': the chart image is saved as chart.png (needs matplotlib).
    with tempfile.TemporaryDirectory(ignore_cleanup_errors=True) as folder:
        check_run("option 6 + yes (chart image) does not crash",
                  ["9", "y", "6", "y", "0"], folder=folder)
        check("option 6 + yes writes chart.png",
              os.path.exists(os.path.join(folder, "chart.png")))


# ------------------------------------------------------------------ run
# Each module is checked function by function, so one crash does not
# stop the checks of the other functions.
CHECKS = {
    "storage": [("load_data", part_load_data), ("save_data", part_save_data),
                ("export_csv", part_export_csv)],
    "habits": [("add_habit", part_add_habit), ("remove_habit", part_remove_habit),
               ("list_habits", part_list_habits), ("mark_done", part_mark_done)],
    "analytics": [("current_streak", part_current_streak), ("longest_streak", part_longest_streak),
                  ("completion_rate", part_completion_rate), ("weekly_summary", part_weekly_summary),
                  ("bad log entries", part_bad_log_entries), ("data not changed", part_data_unchanged)],
    "reports": [("text_chart", part_text_chart), ("save_chart_image", part_save_chart_image),
                ("build_report", part_build_report), ("report numbers", part_report_numbers),
                ("save_report", part_save_report)],
    "utils": [("ask_int", part_ask_int), ("ask_date", part_ask_date),
              ("ask_yes_no", part_ask_yes_no), ("ask_text", part_ask_text),
              ("end of input", part_end_of_input)],
    "main": [("start and quit", part_main_start), ("end of input", part_main_end_of_input),
             ("bad input", part_main_bad_input), ("options with no habits", part_main_empty_options),
             ("demo data", part_main_demo), ("data files", part_main_files),
             ("options 5 to 8 with data", part_main_options_with_data),
             ("journey", part_main_journey)],
}

# 'all' does not include 'main' (see the top of this file).
ALL_MODULES = ["storage", "habits", "analytics", "reports", "utils"]


def run(name, full):
    print("\n" + name + ".py")
    module = None
    if name != "main":  # main.py is started as a program, not imported
        try:
            module = importlib.import_module(name)
        except Exception as error:  # the file is missing or has an error
            check(name + ".py can be imported", False)
            print("        Python says:", type(error).__name__, "-", error)
            return

    for part_name, part in CHECKS[name]:
        try:
            part(module, full)
        except Exception as error:  # the student's code crashed
            check(part_name + " runs without crashing", False)
            print("        Python says:", type(error).__name__, "-", error)
        cleanup()


def find_stubs():
    """Print which files are real code and which still start with # STUB."""
    for name in ["storage", "habits", "analytics", "reports", "main", "utils"]:
        path = name + ".py"
        if not os.path.exists(path):
            print("  MISSING", path)
            continue
        with open(path, encoding="utf-8") as file:
            first_line = file.readline().lstrip("\ufeff").strip()
        print("  STUB   " if first_line == "# STUB" else "  real   ", path)


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        return

    name = sys.argv[1]
    if name == "stubs":
        find_stubs()
        return
    full = len(sys.argv) > 2 and sys.argv[2] == "full"

    if name == "all":
        names = ALL_MODULES
    elif name in CHECKS:
        names = [name]
    else:
        print("Unknown module. Choose: storage, habits, analytics, reports, utils, main, all, stubs")
        return

    for module_name in names:
        run(module_name, full)

    print("\nResult:", passed, "passed,", failed, "failed")
    if failed > 0:
        print("Read the FAIL lines, fix your code, and run the checker again.")


main()