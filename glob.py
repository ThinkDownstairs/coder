

_go_manager = None
def get_manager():
    import go_manager
    global _go_manager
    if _go_manager is None:
        _go_manager = go_manager.GoManager()
    return _go_manager
