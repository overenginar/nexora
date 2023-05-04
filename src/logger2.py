from abc import abstractmethod, ABC
import logging


class DummyLogger(ABC):
    @abstractmethod
    def log(self):
        pass


class NewLogger(DummyLogger):
    def log(self, new_var: str, new_var2: int) -> None:
        """
        log method

        Args:
            new_var (str): Dummy string variable
            new_var2 (int): dummy integer variable

        Returns:
            None
        """
        logging.getLogger().setLevel(logging.INFO)
        logging.info("New Log")
        logging.info(f"String var {new_var}")
        logging.info(f"String var {new_var2}")

    def new_method(self, a: str) -> str:
        """
        new method

        Args:
            a (str): Dummy String Variable

        Returns:
            str: Return dummy value
        """
        return a


if __name__ == "__main__":
    n = NewLogger()

    n.log("a", 1)
