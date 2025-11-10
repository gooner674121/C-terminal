to use this you need to download GCC copy the tutorial 

1. Install MinGW

You downloaded MinGW, which provides GCC for Windows.

During installation, you chose a directory, for example:

C:\MinGW


Inside this directory:

bin → contains gcc.exe and other compiler executables

lib → standard libraries

include → header files like stdio.h

So the compiler lives at:

C:\MinGW\bin\gcc.exe

2. Add GCC to Windows PATH

We need Windows to find gcc.exe automatically, just like we want Python to run it from the terminal.

Press Windows + S, type “Environment Variables”, and open “Edit the system environment variables”.

Click Environment Variables…

Under System variables, find Path → select → Edit

Click New and add the path to GCC’s bin folder:

C:\MinGW\bin


Click OK to close all windows.

3. Verify

Open a new Command Prompt and type:

gcc --version

You should see:
gcc (tdm64-1) 10.3.0


Now Python scripts and terminals can call gcc from anywhere.
