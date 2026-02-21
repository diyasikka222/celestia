from PySide6.QtWidgets import (
    QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QLabel, QPushButton
)
from PySide6.QtCore import Qt, QPoint
from PySide6.QtGui import QMouseEvent


class CelestiaWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Borderless window
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.resize(1000, 600)

        self.old_pos = None

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        main_layout = QVBoxLayout()
        central_widget.setLayout(main_layout)

        # -------- Custom Title Bar --------
        title_bar = QWidget()
        title_layout = QHBoxLayout()
        title_layout.setContentsMargins(10, 5, 10, 5)
        title_bar.setLayout(title_layout)

        title_label = QLabel("🌌 Celestia")
        title_label.setStyleSheet("color: #c9d1ff; font-size: 14px;")

        close_btn = QPushButton("✕")
        close_btn.setFixedSize(30, 24)
        close_btn.clicked.connect(self.close)

        close_btn.setStyleSheet("""
            QPushButton {
                background-color: transparent;
                color: #ff6b6b;
                border: none;
                font-size: 14px;
            }
            QPushButton:hover {
                background-color: #1a1f33;
                border-radius: 6px;
            }
        """)

        title_layout.addWidget(title_label)
        title_layout.addStretch()
        title_layout.addWidget(close_btn)

        # -------- Content Area --------
        content = QLabel("Welcome to Celestia")
        content.setAlignment(Qt.AlignCenter)
        content.setStyleSheet("color: white; font-size: 24px;")

        main_layout.addWidget(title_bar)
        main_layout.addWidget(content)

        self.apply_theme()

        # Enable dragging
        title_bar.mousePressEvent = self.mousePressEvent
        title_bar.mouseMoveEvent = self.mouseMoveEvent

    def apply_theme(self):
        self.setStyleSheet("""
            QMainWindow {
                background-color: #0b0f1a;
                border: 1px solid #1f2a44;
                border-radius: 12px;
            }
        """)

    def mousePressEvent(self, event: QMouseEvent):
        if event.button() == Qt.LeftButton:
            self.old_pos = event.globalPosition().toPoint()

    def mouseMoveEvent(self, event: QMouseEvent):
        if self.old_pos:
            delta = QPoint(event.globalPosition().toPoint() - self.old_pos)
            self.move(self.x() + delta.x(), self.y() + delta.y())
            self.old_pos = event.globalPosition().toPoint()
