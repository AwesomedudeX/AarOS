# AarOS
Houses my console and its compatible apps.

This is a terminal-based console that I decided to develop for a fun personal project. It should be pretty helpful in terms of data analysis or just everyday use. One thing to note though: this console is built specifically for WindowsOS computers. I've tested it with MacOS and some features are not available when this is run there. As for Linux or other OS computers, they have not been tested, so I cannot guarantee full functionality on there.

Also, don't forget to read the app usage notes if this is your first time using the console, and turn on notifications so you know when I'm making updates to apps or releasing new ones, and if you run into any problems, feel free to tell me in the Discussions section. Hope you find this console useful!

## On First Use:

You will need to install Python 3.10 or later using the link in the About section. After this, you will need to install pip along with the required modules. To do this, download the get-pip program and save it to a folder. Then, navigate to the file, right-click on it and click "Copy as path". Next, open up Powershell (step 1 of Running AarOS on Windows Powershell), type "cd", followed by the copied path and press Enter. From here, type "./get-pip.py" and wait for the program to install Pip onto your device - it's the Python tool that'll be used to install modules so that you can use them with Python programs. Finally, just type in these commands to install the required modules:

1. pip install seaborn
2. pip install sklearn
3. pip install datetime
4. pip install numpy

Once all of these commands have run, the console will be ready for use. One last thing; I suggest entering all of your personal information into the Settings app, as certain features may rely on these for full functionality. Don't worry though - none of these features will be stored anywhere other than your device, as the console cannot access the internet or anything of the sort, making it isolated to your device alone.

## Usage Notes:

 - You will need to download the source programs and App Manager manually, as they will not be included in the App Manager. All other apps, however, can be downloaded using the App Manager.
 - Make sure that all the files that you download from here are in the same folder so that they'll work properly. Also, don't change the file names, since this will prevent apps from working.
 - Make sure not to tamper with any of the code unless you know what you're doing. This may affect the functionality of the programs, though there isn't much risk that comes with this other than messing up the source programs, which is specific to your device. Other than that, if you accidentally mess up an app, don't be afraid to just delete it and redownload it from this page.
 - The App Manager, Checklist, Settings, DataFrames and File Manager apps all require the console to be run on Powershell (Windows), or if the app crashes due to lack of resources, then it will require an IDE to save changes, so if you want to use them, then you can use the instructions below to run the console using Powershell.
 - Don't run any of the apps separately, as they will not do anything. However, if you run the Checklist app, it will reset, so do not do this unless you want a quick way to reset it.

## Running AarOS on Windows Powershell:

 1. First, open up the start menu, search for "powershell" and run it.
 2. After this, head to the folder with the AarOS file in it, right-click on the folder, and click "Copy as path".
 3. Then, go back to Powershell, and type "cd", followed by a space and the copied path (press "Ctrl-V" to paste), and press Enter.
 4. Finally, type "./AarOS.py" and press Enter to run the console.

Note: Next time you want to use Powershell, you can use the up and down arrow keys to select previously run commands, which is faster if you haven't put in any commands after running the console.
