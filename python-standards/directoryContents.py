def print_directory_contents(sPath):
    """
    This function takes the name of a directory
    and prints out the paths files within that
    directory as well as any files contained in
    contained directories.

    This function is similar to os.walk. Please don't
    use os.walk in your answer. We are interested in your
    ability to work with nested structures.
    """
    import os
    for dChild in os.listdir(sPath):
        dChildPath = os.path.join(sPath, dChild)
        if(os.path.isdir(dChildPath)):
            print_directory_contents(dChildPath)
        else:
            print(dChildPath)


print_directory_contents("/Users/eta/workspace/PythonDataStructures")
