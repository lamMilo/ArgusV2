# Argus V2.0 👁️

[![Python 3.13](https://img.shields.io/badge/python-3.13-blue.svg)](https://www.python.org/downloads/) [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

**Argus** is a modern, high-performance network reconnaissance and auditing tool designed for security professionals and network enthusiasts. Built with a focus on speed and aesthetic, it provides real-time insights into open ports and target infrastructure.

## Features
- ⚡ **High-Speed Scanning**: Asynchronous threading for rapid port discovery.
- 🎨 **Modern UI**: Built with PyQt5 for a smooth, dark-mode glass-morphism aesthetic.
- 🎯 **Intelligent Presets**: Quick-scan profiles for common scenarios (Zenmap-style).
- 🔍 **WHOIS Integration**: Built-in reconnaissance to gather domain/IP ownership data.
- 💾 **Export**: Save your findings directly to text reports for later analysis.

## Installation

[Download ArgusV2.exe (Portable)](https://github.com/lamMilo/ArgusV2/releases/latest/download/ArgusV2.exe)


### Prerequisites
Ensure you have Python 3.x installed. 

1. **Clone this repository**: 
   `git clone https://github.com/lammilo/ArgusV2`
   `cd ArgusV2`

2. **Install the required dependencies**: 
   `pip install python-whois pyqt5`

## Usage
Run the application directly from your terminal:
`python ArgusV2.py`

1. **Target**: Enter the domain (e.g., google.com) or IP address.
2. **Preset**: Choose an intensity profile from the dropdown (Quick, Common, or Intense).
3. **Audit**: Click **START AUDIT** and watch the results stream in real-time.

## Scan Presets
Argus includes curated port profiles to maximize speed and relevance:
- **Quick Scan**: Focuses on the top 100 ports.
- **Common Ports**: Targets core services (SSH, HTTP, SQL, RDP).
- **Intense Scan**: Comprehensive check of the first 1000 ports.

## Contribution
Contributions are welcome! Please feel free to open an issue or submit a pull request if you want to add features like advanced service fingerprinting or custom port range inputs.

## Legal Disclaimer
*Argus is intended for educational and authorized security testing purposes only. The author takes no responsibility for misuse of this tool against unauthorized systems.*

---
*Created ⚡ by Milo*
