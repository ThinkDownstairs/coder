
import state_manager

class Quit(state_manager.State):
    def __init__(self) -> None:
        super().__init__()


    def render(self) -> None:
        pass

    def input(self) -> None:
        pass


    def update(self, delta: int, fps: float) -> None:
        pass

    def leave(self, next_: state_manager.StateType) -> None:
        pass

    def enter(self, prev_: state_manager.StateType) -> None:
        self.state_manager.terminate_main_loop()
