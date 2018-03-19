
import state_manager

ABOUT = [
    '


class About(state_manager.State):
    def __init__(self) -> None:
        super().__init__()
        self._surface = None


    def render(self) -> None:
        pass

    def input(self) -> None:
        pass

    def update(self, delta: int, fps: float) -> None:
        pass

    def leave(self) -> None:
        pass

    def enter(self) -> None:
        pass
