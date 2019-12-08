class DependencyException(BaseException):
    pass


class BaseClass:
    dependencies = []

    def __init__(self):
        self._live_dependencies = [x() for x in self.dependencies]

    def is_live(self):
        print(f'it is live {self.__class__.__name__}')
        return False

    def _activate_dependencies(self):
        for dep in self._live_dependencies:
            dep.activate()

    def _activate(self):
        self._activate_dependencies()
        print(f'activating for real {self.__class__.__name__}')

    def activate(self):
        print(f'activating {self.__class__.__name__}')

        if not self.is_live():
            self._activate()

    def _deactivate_dependencies(self):
        for dep in self._live_dependencies:
            dep.deactivate()

    def _deactivate(self):
        self._deactivate_dependencies()
        print(f'deactivating for real {self.__class__.__name__}')

    def deactivate(self):
        print(f'deactivating {self.__class__.__name__}')

        if self.is_live():
            self._deactivate()

    def _execute(self):
        print(f'executing for real {self.__class__.__name__}')

    def execute(self):
        print(f"executing {self.__class__.__name__}")

        if not self.is_live():
            raise
        self._execute()


class HDMIMonitor(BaseClass):
    pass


class XServer(BaseClass):
    dependencies = [
        HDMIMonitor
    ]


class ChromeKiosk(BaseClass):
    dependencies = [
        XServer
    ]


class OMXPlayer(BaseClass):
    dependencies = [
        HDMIMonitor
    ]


class DisplayImage(BaseClass):
    dependencies = [
        HDMIMonitor
    ]
