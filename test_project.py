import pytest

from project import add_task, delete_task, load_tasks, save_tasks, toggle_task


def test_add_task():
    tasks = []
    add_task(tasks, "  Finish homework  ")
    assert tasks == [{"title": "Finish homework", "completed": False}]


def test_add_task_rejects_empty_title():
    with pytest.raises(ValueError):
        add_task([], "   ")


def test_delete_task():
    tasks = [{"title": "Read", "completed": False}]
    removed = delete_task(tasks, 0)
    assert removed["title"] == "Read"
    assert tasks == []


def test_delete_task_rejects_invalid_index():
    with pytest.raises(IndexError):
        delete_task([], 0)


def test_toggle_task():
    tasks = [{"title": "Practice guitar", "completed": False}]
    toggle_task(tasks, 0)
    assert tasks[0]["completed"] is True
    toggle_task(tasks, 0)
    assert tasks[0]["completed"] is False


def test_save_and_load_tasks(tmp_path):
    tasks = [{"title": "Build a project", "completed": True}]
    file_path = tmp_path / "data" / "tasks.json"
    save_tasks(tasks, file_path)
    assert load_tasks(file_path) == tasks


def test_load_missing_file_returns_empty_list(tmp_path):
    assert load_tasks(tmp_path / "missing.json") == []
