import io
import sys

def get_object_info(obj):
    # Capture the output of help() function
    old_stdout = sys.stdout
    sys.stdout = buffer = io.StringIO()
    help(obj)
    sys.stdout = old_stdout
    
    # Get the first line of the help output
    doc_string = buffer.getvalue().split('\n')[0].strip()
    
    # Get the type of the object as a string
    type_string =  type(obj)

    return (doc_string, type_string)
