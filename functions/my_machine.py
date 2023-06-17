import platform


def my_machine_os(my_machine: str):
    """
    Get the operating system of my machine

    Parameters
    ----------
    my_machine : string
        my machine string

    Returns
    -------
    string
        my machine operating system
    """

    system = platform.system()
    if system == "Windows":
        return "Windows"
    elif system == "Darwin":
        return "Mac OS"
    elif system == "Linux":
        return "Linux"
    else:
        return "Unknown"
