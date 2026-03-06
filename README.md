What is Isit?
  It is an installable python module that can be used to check and convert variable datatypes. (e.g. if 5 is string you can use Intis() to convert it to integer)

How To Install:
  1. Open the folder in VS Code(or something similar. Must have a built-in terminal/command prompt. If you do not have built-in terminal/command prompt, skip to "How To Install Through CMD")
  2. Write: pip3 install . (if you do not have pip3 install pip3 first)
  3. Use import isit to use it in your projects.

How To Install Through CMD:
  1. Open CMD(command prompt)
  2. Navigate to the folder containing isit.py and pyproject.toml files using "cd" command
  3. Write: pip3 install . (if you do not have pip3 install pip3 first)
  4. Use import isit to use it in your projects

How to use:
You can use the following:
  1. Intis()
  2. Floatis()
  3. Boolis()
  4. Stris()
All check or convert the variable.
Contains 6 main arguments:
  1. num - the general input or variable to be checked/converted
  2. mes - message to be printed if data type is incorrect, sendBool is False and useMessage is True
  3. inputmes - message to be printed as a prompt in the input
  4. sendBool - returns True if the data type of the variable is correct and False if incorrect
  5. useMessage - if True, it will print a message from mes argument before prompting for input (ONLY WORKS IF sendBool IS FALSE)
  6. timer - delay(in seconds) between message and input prompt

IMPORTANT:
  THIS MODULE IS NOT LINUX FRIENDLY.
