# Week 1 - Task 1: Environment & Tool Installation Guide

**Student Name:** Ali Muhammad Younis (886)  
**Course:** Artificial Intelligence, Machine Learning & Deep Learning  
**Week:** 1  
**Task Title:** Installation of Anaconda3, PyTorch, TensorFlow 2.0, VSCode, and PyCharm  

---

## 1. Overview
In this task, the complete foundational development environment for Artificial Intelligence and Deep Learning is prepared and configured. The environment includes:
1. **Anaconda3** - Package & virtual environment manager for Python data science.
2. **VSCode (Visual Studio Code)** - Lightweight, extensible source code editor.
3. **PyCharm Community / Professional** - Dedicated Python IDE with powerful debugging tools.
4. **PyTorch** - Open-source deep learning framework based on Torch.
5. **TensorFlow 2.0+** - End-to-end open-source machine learning platform by Google.

---

## 2. Step-by-Step Installation Procedures

### A. Anaconda3 Installation
1. Download installer for your platform from official website: `https://www.anaconda.com/download`
2. Run installer (`Anaconda3-xxxx-Windows-x86_64.exe`).
3. Accept license agreement and select installation folder.
4. Check option: "Register Anaconda3 as default Python".
5. Verify installation via terminal:
   ```bash
   conda --version
   python --version
   ```
6. Create an isolated environment for AI/ML:
   ```bash
   conda create -n ai_env python=3.10 -y
   conda activate ai_env
   ```

### B. Visual Studio Code (VSCode) Installation
1. Download installer from `https://code.visualstudio.com/`
2. Run installer and enable:
   - "Add 'Open with Code' to Windows Explorer context menu"
   - "Add to PATH"
3. Launch VSCode and install the recommended extensions:
   - **Python** (by Microsoft)
   - **Pylance** (Language Server)
   - **Jupyter** (Interactive notebooks)

### C. PyCharm Installation
1. Download PyCharm Community Edition from `https://www.jetbrains.com/pycharm/download/`
2. Run the installation wizard and select 64-bit launcher and `.py` associations.
3. Open PyCharm and configure the Python interpreter to point to your Anaconda/system environment.

### D. PyTorch Installation
Install PyTorch via pip or conda:
- **CPU version:**
  ```bash
  pip install torch torchvision torchaudio
  ```
- **CUDA (GPU) version (e.g. CUDA 11.8/12.1):**
  ```bash
  pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
  ```

### E. TensorFlow 2.0+ Installation
Install TensorFlow 2.x using pip:
```bash
pip install tensorflow
```

---

## 3. Environment Verification Script
Run `Task_01_verify_environment.py` located in this directory to verify the installed packages and their versions automatically.
