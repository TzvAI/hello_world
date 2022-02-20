"""test code with security problems."""
user_input=input()
prog = 'print("The sum of 5 and 10 is"'+user_input+ ')'
exec(prog)
