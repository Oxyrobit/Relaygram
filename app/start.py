import os
from lang import T 

session_string = os.environ.get("SESSION_STRING")

if not session_string or session_string.strip() == "":
    print(T["no_session"])
    print(T["generate_session"])
    os.system("python generate_session.py")
else:
    print(T["session_found"])
    print(T["launch_main"])
    os.system("python main.py")