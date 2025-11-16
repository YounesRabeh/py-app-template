from core.manager.theme_manager import ThemeManager
from core.util.resources import Resources
from gui.stages.base_stage import BaseStage, UIFactory


class Stage1(BaseStage):
    def __init__(self, config: dict):
        super().__init__(config, "🟢 Stage 1: Start")

        # Add “Next” button (right-aligned)
        next_btn = UIFactory.create_button("Next → Stage 2", self.next_stage.emit)
        theme_btn = UIFactory.create_button(
            "Theme",
            lambda : ThemeManager.apply_theme_to_widget(next_btn, Resources.get_in_qss("button_theme_1.qss")))
        file_entry = UIFactory.create_file_entry("")
        ThemeManager.apply_theme_to_widget(file_entry,Resources.get_in_qss("default_file_entry_style.qss"))


        self.main_layout.addWidget(file_entry)
        self.main_layout.addWidget(next_btn)
        self.main_layout.addWidget(theme_btn)
