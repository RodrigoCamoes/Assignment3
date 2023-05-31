from idlelib import debugger
import List
from types import FrameType
from typing import Any, Optional


class ContinuousSpectrumDebugger:
    def suspiciousness(self, event: Any) -> Optional[float]:
        hue = self.hue(event)
        if hue is None:
            return None
        return 1 - hue

    def tooltip(self, event: Any) -> str:
        return self.percentage(event)


class RankingDebugger:

    def rank(self) -> List[Any]:
        def susp(event: Any) -> float:
            suspiciousness = self.suspiciousness(event)
            assert suspiciousness is not None
            return suspiciousness

        events = list(self.all_events())
        events.sort(key=susp, reverse=True)
        return events

    def __repr__(self) -> str:
        return repr(self.rank())


class StatRepair:

    def collect(self, frame: FrameType, event: str, arg: Any) -> None:
        name = frame.f_code.co_name
        function = self.search_func(name, frame)

        if function is None:
            function = self.create_function(frame)

        location = (function, frame.f_lineno)
        self._coverage.add(location)

    def mostsimilarstmt(self, targetloc):
        if targetloc > self.collect():
            targetloc - self.collect()
        elif targetloc < self.collect():
            self.collect()- targetloc
        return debugger.rank()






