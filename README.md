<h1>DentMirror - Indirect Vision Simulator</h1>

DentMirror is a hybrid (C++ / Python) simulation software designed for dental students to improve their indirect vision and hand-eye coordination skills using a dental mirror.

As students move a virtual surgical tool (mouse) on the screen, the system reverses these movements in real-time, accelerating the brain's adaptation to mirror-image working environments.

## Features
* **Real-Time C++ Engine:** Mouse X and Y coordinates are captured in milliseconds by the C++ engine (via pybind11) and inverted based on the selected mirror mode.
* **Various Mirror Modes:** Horizontal Reverse, Vertical Reverse, and Full Mirror simulations.
* **Smooth Drawing (Anti-Aliasing):** Every mouse movement is converted into seamless and fluid vector lines using PyQt6.
* **Time Limit (Exam Mode):** Optional, dynamic countdown timer to test students under pressure.
* **Progress Tracking (Logging):** After each test, the student's name, date, test mode, and success score are automatically saved to the `data/gelisimRaporu.csv` file.
* **Visual Reporting:** Instant visual analysis and success rate calculation post-test with Matplotlib and Pandas integration.

## Download for Windows (Portable)

You can run the DentMirror simulator directly on Windows without setting up a Python environment or dealing with C++ compilers. 

Simply head over to the **[Releases](https://github.com/cagatay005/dentMirror/releases)** section, download the latest `.zip` file, extract it to a folder, and run the executable file to start your simulation immediately. No installation is required!

## Project Architecture
The project consists of two main layers: **C++** (Core) for performance-heavy calculations and **Python** (App) for the UI/analytics:

    dentMirror/
    ├── app/                  # Python UI and Analytics Layer
    │   ├── analytics/        # Data processing, plotting, and CSV logging
    │   ├── ui/               # PyQt6 screens (Main Menu, Test Screen, Report)
    │   └── baslangic.py      # Main script to launch the application
    ├── core/                 # C++ Calculation and Simulation Engine
    │   ├── include/          # Header (.hpp) files
    │   └── src/              # Source (.cpp) files (including pybind11 wrapper)
    ├── data/                 # Directory for student progress reports (CSV)
    ├── CMakeLists.txt        # C++ build configuration
    └── requirements.txt      # Python dependencies

## Installation & Build (Ubuntu/Linux)

### 1. Install Requirements
Ensure Python 3, CMake, and a C++ compiler are installed on your system. Then, install the Python libraries (and pybind11):

```bash
sudo apt update && sudo apt install python3-dev pybind11-dev
pip3 install -r requirements.txt
```
### 2. Build the C++ Engine
```bash
mkdir build
cd build
cmake ..
make
cd ..
```
### 3. Run the Simulator
After a successfull build, run the application from the root directory:
```bash
python3 app/baslangic.py
```

## Technologies Used
*Backend: C++11, pybind11, CMake*

*Frontend: Python 3, PyQt6*

*Data & Analytics: Pandas, Matplotlib*
