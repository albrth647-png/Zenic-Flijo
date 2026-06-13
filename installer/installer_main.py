#!/usr/bin/env python3
"""
Workflow Determinista — GUI Installer Wizard
==============================================

NOTA: Entry point esbelto (~150 lines). La lógica de UI está en
installer/ui.py y los pasos de instalación en installer/steps.py.
"""

from __future__ import annotations

import sys
import threading
import tkinter as tk
import tkinter.messagebox as messagebox
from pathlib import Path

# ── Ensure project root on sys.path BEFORE package imports ───────────────
_INSTALLER_DIR = Path(__file__).resolve().parent
_PROJECT_ROOT = _INSTALLER_DIR.parent
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))

from installer.config import (  # noqa: E402
    IS_WINDOWS,
    LANG,
    PROJECT_ROOT,
    logger,
)
from installer.steps import (  # noqa: E402
    InstallError,
    _configure_autostart_linux,
    _configure_autostart_windows,
    _install_step_configure_autostart,
    _install_step_configure_license,
    _install_step_copy_files,
    _install_step_create_database,
    _install_step_create_dirs,
    _install_step_save_password,
    _install_step_start_server,
)
from installer.ui import (  # noqa: E402
    _browse_directory,
    _build_step_complete,
    _build_step_directory,
    _build_step_language,
    _build_step_license,
    _build_step_password,
    _build_step_progress,
    _build_ui,
    _go_back,
    _go_next,
    _init_window,
    _on_cancel,
    _on_finish,
    _on_language_change,
    _on_license_focus_in,
    _on_license_focus_out,
    _open_browser,
    _show_step,
    _validate_password,
)


class InstallerWizard(tk.Tk):
    """Multi-step installation wizard for Workflow Determinista."""

    TOTAL_STEPS = 6
    _is_windows = IS_WINDOWS

    def __init__(self):
        super().__init__()
        self.selected_lang = tk.StringVar(value="es")
        self.install_dir = tk.StringVar(
            value=LANG["es"]["dir_default_win"] if IS_WINDOWS else LANG["es"]["dir_default_linux"]
        )
        self.license_key = tk.StringVar(value="")
        self.admin_password = tk.StringVar(value="")
        self.admin_password_confirm = tk.StringVar(value="")
        self.current_step = tk.IntVar(value=0)
        self.install_error = None

        self._init_window()
        self._build_ui()
        self._show_step(0)
        logger.info("Installer wizard started")

    def _clear_content(self):
        """Remove all widgets from the content frame."""
        for widget in self.content_frame.winfo_children():
            widget.destroy()

    def _txt(self, key: str) -> str:
        """Get localized text for the current language."""
        return LANG[self.selected_lang.get()].get(key, key)

    def _log_progress(self, message: str):
        """Append a message to the progress log area."""
        self.log_text.config(state="normal")
        self.log_text.insert("end", message + "\n")
        self.log_text.see("end")
        self.log_text.config(state="disabled")
        logger.info(message)

    def _update_progress(self, percent: int, message: str):
        """Update the progress bar and label."""
        self.progress_bar["value"] = percent
        self.progress_label.config(text=message)
        self._log_progress(message)
        self.update_idletasks()

    # ── Installation orchestration ──────────────────────────

    def _start_install(self):
        """Kick off the installation in a background thread."""
        if not self._validate_password():
            return
        self.btn_next.config(state="disabled")
        self.btn_back.config(state="disabled")
        self.btn_cancel.config(state="disabled")
        thread = threading.Thread(target=self._run_install, daemon=True)
        thread.start()

    def _run_install(self):
        """Perform all installation steps. Updates the GUI from the main thread."""
        try:
            self._install_step_create_dirs()
            self._install_step_copy_files()
            self._install_step_create_database()
            self._install_step_save_password()
            self._install_step_configure_license()
            self._install_step_configure_autostart()
            self._install_step_start_server()
            self._update_progress(100, self._txt("progress_done"))
            self.after(0, lambda: self._show_step(self.TOTAL_STEPS - 1))
        except InstallError as exc:
            self.install_error = str(exc)
            logger.error(f"Installation failed: {exc}")
            self._log_progress(f"ERROR: {exc}")
            self.after(0, lambda: self._show_step(self.TOTAL_STEPS - 1))
        except Exception as exc:
            self.install_error = str(exc)
            logger.exception("Unexpected installation error")
            self._log_progress(f"FATAL ERROR: {exc}")
            self.after(0, lambda: self._show_step(self.TOTAL_STEPS - 1))


# ── Bind UI functions as methods ──────────────────────────────────────────

InstallerWizard._init_window = _init_window
InstallerWizard._build_ui = _build_ui
InstallerWizard._show_step = _show_step
InstallerWizard._go_next = _go_next
InstallerWizard._go_back = _go_back
InstallerWizard._on_cancel = _on_cancel
InstallerWizard._on_finish = _on_finish
InstallerWizard._open_browser = _open_browser
InstallerWizard._on_language_change = _on_language_change
InstallerWizard._browse_directory = _browse_directory
InstallerWizard._on_license_focus_in = _on_license_focus_in
InstallerWizard._on_license_focus_out = _on_license_focus_out
InstallerWizard._validate_password = _validate_password
InstallerWizard._build_step_language = _build_step_language
InstallerWizard._build_step_directory = _build_step_directory
InstallerWizard._build_step_license = _build_step_license
InstallerWizard._build_step_password = _build_step_password
InstallerWizard._build_step_progress = _build_step_progress
InstallerWizard._build_step_complete = _build_step_complete

# ── Bind install step functions as methods ─────────────────────────────────

InstallerWizard._install_step_create_dirs = _install_step_create_dirs
InstallerWizard._install_step_copy_files = _install_step_copy_files
InstallerWizard._install_step_create_database = _install_step_create_database
InstallerWizard._install_step_save_password = _install_step_save_password
InstallerWizard._install_step_configure_license = _install_step_configure_license
InstallerWizard._install_step_configure_autostart = _install_step_configure_autostart
InstallerWizard._configure_autostart_windows = _configure_autostart_windows
InstallerWizard._configure_autostart_linux = _configure_autostart_linux
InstallerWizard._install_step_start_server = _install_step_start_server


# ═══════════════════════════════════════════════════════════════════════════
#  Entry point
# ═══════════════════════════════════════════════════════════════════════════

def main():
    """Launch the installer wizard."""
    import platform as _platform

    logger.info("=" * 60)
    logger.info("Workflow Determinista Installer starting")
    logger.info(f"Platform: {_platform.system()} {_platform.release()}")
    logger.info(f"Python: {sys.version}")
    logger.info(f"Project root: {PROJECT_ROOT}")
    logger.info("=" * 60)

    try:
        app = InstallerWizard()
        app.mainloop()
    except Exception as exc:
        logger.exception("Fatal installer error")
        from contextlib import suppress
        with suppress(Exception):
            messagebox.showerror("Fatal Error", str(exc))
        sys.exit(1)


if __name__ == "__main__":
    main()
