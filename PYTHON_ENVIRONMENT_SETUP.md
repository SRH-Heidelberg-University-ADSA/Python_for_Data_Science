# Python Environment Installation

Setting up a Python environment is essential for running code, data analysis, and machine learning projects.

Below are detailed instructions for installing three popular Python environments: **Anaconda / Jupyter Notebook**, **Visual Studio Code (VS Code)**, and **Google Colab**.

> **For this module**, we will primarily use **Anaconda / Jupyter Notebook** and **VS Code**.

---

#### 1. Anaconda / Jupyter Notebook

**Anaconda** is a popular Python distribution that comes with many scientific libraries and tools pre-installed. **Jupyter Notebook** allows you to write and run Python code interactively.

1. Download **Anaconda** from the official website: [https://www.anaconda.com/products/distribution](https://www.anaconda.com/products/distribution)
2. Run the installer and follow the instructions. You may choose to add Anaconda to your system PATH (optional but recommended).
3. Open **Anaconda Navigator** from your start menu or applications folder.
4. Launch **Jupyter Notebook** via Anaconda Navigator or by typing the following command in your terminal or command prompt:
   ```bash
   jupyter notebook
   ```
5. A browser window will open. Create a new Python notebook and run a test command to ensure everything works:
   ```python
   print("Hello, Python!")
   ```
6. You can now write, run, and save Python code in cells interactively.

---

#### 2. Visual Studio Code (VS Code)

**VS Code** is a lightweight, flexible code editor that supports Python development with extensions.

1. Download and install VS Code from [https://code.visualstudio.com/](https://code.visualstudio.com/)

2. Open VS Code and go to the Extensions Marketplace (icon on the left toolbar).

3. Search for the **Python** extension by Microsoft and install it.

4. Ensure that the correct Python interpreter is selected:
   - Press `Ctrl+Shift+P` (or `Cmd+Shift+P` on Mac)
   - Search for **Python: Select Interpreter**
   - Choose the Python version installed via Anaconda or your system Python

5. Create a new Python file (`.py`) and test your setup by running:
   ```python
   print("Hello, VS Code!")
   ```
6. You can now write and run Python scripts efficiently, with features like debugging, linting, and code completion.

---

#### 3. Google Colab

**Google Colab** is a cloud-based Python environment that allows you to write and run code without any installation. It is ideal for beginners or collaborative projects.

1. Open Google Colab in your browser: [https://colab.research.google.com/](https://colab.research.google.com/)

2. Sign in using your Google account.

3. Create a new notebook by selecting **File → New Notebook**.

4. Test Python execution by running:
   ```python
   print("Hello, Colab!")
   ```

5. Optionally, you can mount your Google Drive to read or save files directly from your Drive:
   ```python
   from google.colab import drive
   drive.mount('/content/drive')
   ```

6. Colab also provides free **GPU** and **TPU** resources for running intensive computations.
