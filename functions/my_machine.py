import platform


def my_machine_os(not_used: str):
    """
    Get the operating system of my machine

    Parameters
    ----------
    not_used : string
        parameter not used

    Returns
    -------
    string
        my machine operating system
    """

    system = platform.system()
    print(f"My system is: {system}")

    if system == "Windows":
        return "Windows"
    elif system == "Darwin":
        return "Mac OS"
    elif system == "Linux":
        return "Linux"
    else:
        return "Unknown"
