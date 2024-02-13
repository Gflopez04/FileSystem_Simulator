class Node:
    def __init__(self, name, is_directory=False):
        self.name = name
        self.is_directory = is_directory
        self.children = []
        self.parent = None

class FileSystem:
    def __init__(self):
        self.root = Node("/", is_directory=True)
        self.current_directory = self.root

    def ls(self):
        return [child.name for child in self.current_directory.children]

    def mkdir(self, directory_name):
        new_directory = Node(directory_name, is_directory=True)
        new_directory.parent = self.current_directory
        self.current_directory.children.append(new_directory)

    def cd(self, directory_name):
        if directory_name == "..":
            if self.current_directory.parent:
                self.current_directory = self.current_directory.parent
        else:
            for child in self.current_directory.children:
                if child.name == directory_name and child.is_directory:
                    self.current_directory = child
                    break

    def touch(self, file_name):
        new_file = Node(file_name)
        new_file.parent = self.current_directory
        self.current_directory.children.append(new_file)

def main():
    fs = FileSystem()

    while True:
        command = input("$ ").split()

        if not command:
            continue

        if command[0] == "ls":
            print(" ".join(fs.ls()))

        elif command[0] == "mkdir":
            if len(command) != 2:
                print("Usage: mkdir <directory_name>")
            else:
                fs.mkdir(command[1])

        elif command[0] == "cd":
            if len(command) != 2:
                print("Usage: cd <directory_name>")
            else:
                fs.cd(command[1])

        elif command[0] == "touch":
            if len(command) != 2:
                print("Usage: touch <file_name>")
            else:
                fs.touch(command[1])

        elif command[0] == "exit":
            break

        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
