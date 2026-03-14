import sys
import socket
import whois
from PyQt5 import QtWidgets, QtGui, QtCore

# Modern Dark Theme
DARK_STYLE = """
    QMainWindow { background-color: #0A0A0A; }
    QLabel { color: #BBB; font-family: 'Segoe UI'; font-size: 12px; }
    QLineEdit, QComboBox { 
        background-color: #161616; color: #FFF; border: 1px solid #333; 
        padding: 8px; border-radius: 4px; 
    }
    QTextEdit { 
        background-color: #0D0D0D; color: #00FF41; border: 1px solid #222; 
        font-family: 'Consolas'; font-size: 12px; padding: 5px;
    }
    QPushButton { 
        background-color: #0078D7; color: white; border-radius: 4px; padding: 10px; font-weight: bold; 
    }
    QPushButton:hover { background-color: #005A9E; }
    QProgressBar { border: 1px solid #333; border-radius: 2px; text-align: center; color: white; }
    QProgressBar::chunk { background-color: #0078D7; }
"""

# Scan Presets
PRESETS = {
    "Quick Scan (Top 100)": list(range(1, 101)),
    "Common Ports (HTTP/SSH/DB)": [21, 22, 23, 25, 53, 80, 110, 443, 3306, 3389, 8080],
    "Intense Scan (1-1000)": list(range(1, 1001))
}

class ScannerSignals(QtCore.QObject):
    result = QtCore.pyqtSignal(str)
    progress = QtCore.pyqtSignal(int)
    finished = QtCore.pyqtSignal()

class ScanWorker(QtCore.QRunnable):
    def __init__(self, target, ports):
        super().__init__()
        self.target, self.ports = target, ports
        self.signals = ScannerSignals()

    def run(self):
        for i, port in enumerate(self.ports, 1):
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.settimeout(0.1) # Fast timeout for speed
                if s.connect_ex((self.target, port)) == 0:
                    try: service = socket.getservbyport(port)
                    except: service = "unknown"
                    self.signals.result.emit(f"[+] Port {port:5} | {service}")
            self.signals.progress.emit(i)
        self.signals.finished.emit()

class ArgusApp(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.threadpool = QtCore.QThreadPool()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Argus V2.0 - Network Auditor")
        self.resize(750, 600)
        self.setStyleSheet(DARK_STYLE)

        widget = QtWidgets.QWidget()
        layout = QtWidgets.QVBoxLayout(widget)
        
        layout.addWidget(QtWidgets.QLabel("TARGET IP / DOMAIN"))
        self.target_in = QtWidgets.QLineEdit()
        layout.addWidget(self.target_in)

        layout.addWidget(QtWidgets.QLabel("SCAN PROFILE"))
        self.preset_box = QtWidgets.QComboBox()
        self.preset_box.addItems(PRESETS.keys())
        layout.addWidget(self.preset_box)

        self.btn = QtWidgets.QPushButton("START AUDIT")
        self.btn.clicked.connect(self.start_scan)
        layout.addWidget(self.btn)

        self.console = QtWidgets.QTextEdit()
        self.console.setReadOnly(True)
        layout.addWidget(self.console)

        self.bar = QtWidgets.QProgressBar()
        layout.addWidget(self.bar)

        self.setCentralWidget(widget)

    def start_scan(self):
        target = self.target_in.text().strip()
        if not target: return
        
        self.console.clear()
        self.console.append(f"[*] Analyzing: {target}...")
        
        # Whois
        try:
            w = whois.whois(target)
            self.console.append(f"[WHOIS] Registrar: {w.registrar}\n")
        except: pass

        ports = PRESETS[self.preset_box.currentText()]
        self.bar.setMaximum(len(ports))
        
        worker = ScanWorker(target, ports)
        worker.signals.result.connect(lambda s: self.console.append(s))
        worker.signals.progress.connect(self.bar.setValue)
        self.threadpool.start(worker)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = ArgusApp()
    window.show()
    sys.exit(app.exec_())
    
