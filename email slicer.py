Python 3.11.0 (v3.11.0:deaf509e8f, Oct 24 2022, 14:43:23) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> while(True):
... 
...     email_id = input("Enter email id: ")
...     if "@" in email_id:
...         username = email_id[:email_id.index('@')]
... 
...         domain = email_id[email_id.index('@')+1:]
... 
...         a=domain.upper()
...         print(f"username: {username} and domain: {(a)}")
...     else:
...         print("Please enter valid emailid !")
