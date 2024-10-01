from unittest import mock
import pytest
import tkinter as tk
from gendiff.scripts import gui_gendiff


@pytest.fixture
def diff_app():
    root = tk.Tk()
    app = gui_gendiff.DiffApp(root)
    return app


def test_open_file1(diff_app, monkeypatch):
    mock_file_path = "/path/to/test_file1.txt"
    monkeypatch.setattr('tkinter.filedialog.askopenfilename', lambda *args, **kwargs: mock_file_path)

    diff_app.load_file1()

    assert diff_app.file1_label.cget("text") == 'Файл 1: Загружен'
    assert diff_app.file1 == mock_file_path


def test_open_file2(diff_app, monkeypatch):
    mock_file_path = "/path/to/test_file2.txt"
    monkeypatch.setattr('tkinter.filedialog.askopenfilename', lambda *args, **kwargs: mock_file_path)

    diff_app.load_file2()

    assert diff_app.file2_label.cget("text") == 'Файл 2: Загружен'
    assert diff_app.file2 == mock_file_path


def test_open_file_dialog(diff_app, monkeypatch):
    mock_file_path = "/path/to/test_file.txt"
    monkeypatch.setattr('tkinter.filedialog.askopenfilename', lambda *args, **kwargs: mock_file_path)

    with mock.patch('tkinter.messagebox.showwarning') as mock_showwarning:
        result = diff_app.open_file_dialog("Выберите Файл")
        assert result == mock_file_path
        mock_showwarning.assert_not_called()


def test_open_file_dialog_errors(diff_app, monkeypatch):
    mock_file_path = ""
    monkeypatch.setattr('tkinter.filedialog.askopenfilename', lambda *args, **kwargs: mock_file_path)

    with mock.patch('tkinter.messagebox.showwarning') as mock_showwarning:
        result = diff_app.open_file_dialog("Выберите Файл")
        assert result == mock_file_path
        mock_showwarning.assert_called_once_with("Ошибка", "Вы не выбрали файл.")


def test_update_status(diff_app):
    mock_label = mock.MagicMock(spec=tk.Label)
    test_text = "New Status"
    diff_app.update_status(mock_label, test_text)
    mock_label.config.assert_called_once_with(text=test_text)


def test_ask_exit_app(diff_app, monkeypatch):
    monkeypatch.setattr('tkinter.messagebox.askyesno', lambda title, message: True)
    with mock.patch.object(diff_app.root, 'destroy') as mock_destroy:
        diff_app.exit_app()
        mock_destroy.assert_called_once()