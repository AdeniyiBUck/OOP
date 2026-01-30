# Setup Instructions

Follow the instructions below in order to work with the application in this repository.

# Pre-Requisites

1. You must install the latest version of Python.
2. You must have Git installed. Run the following command to install or get from https://git-scm.com/install/windows.

```powershell
winget install --id Git.Git -e --source winget
```
3. You must have GitHub CLI installed. Download and install it from https://cli.github.com.
4. Ensure you are authenticated with GitHub using the GitHub CLI, as shown below.

```powershell
gh auth login
```

# Clone Repository

1. Open your browser and navigate to https://github.com/AdeniyiBUck/OOP.
2. Click on the green Open button and copy the URL presented.
3. Create a `SourceCode` folder in you `C:\` drive of your PC.
4. Open the Terminal / PowerShell application and type and run the commmand below to change the directory to the one you created in step 3.

```powershell
cd C:\SourceCode
```

5. Type the command below to clone the repository. Replace `<URL>` in the command with the URL you copied from step 2.

```powershell
git clone <URL>
```

6. Withing Terminal / PowerShell, type and run the command below to change directory to the newly created `OOP` directory.

```powershell
cd OOP
```

7. Open the `OOP` folder in Visual Studio Code by typing and running the following command in Terminal / PowerShell.

```powershell
code .
```

