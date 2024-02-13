# File System Simulator

This Python program simulates a file system with support for basic operations like `ls`, `mkdir`, `cd`, and `touch`. It holds the file system structure entirely in memory and does not interact with the actual file system of the operating system.

## How to Use

### Requirements
- Python 3.x

### Getting Started
1. Clone the repository or download the Python script `fileSystem.py`.

2. Open a terminal or command prompt.

3. Navigate to the directory where the `fileSystem.py` script is located.

4. Run the script by executing the following command:
    ```
    python fileSystem.py
    ```

### Commands
- `ls`: List the contents of the current directory.
- `mkdir <directory_name>`: Create a new directory with the specified name.
- `cd <directory_name>`: Change the current directory to the specified directory.
- `touch <file_name>`: Create a new file with the specified name.
- `exit`: Exit the program.

### Example Usage


## Notes
- The simulated file system starts with a root directory `/`.
- The `..` directory can be used to navigate to the parent directory.
- The file system structure is held entirely in memory and will be lost when the program ends.

Feel free to explore and interact with the simulated file system using the provided commands!
