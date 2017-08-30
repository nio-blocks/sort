from nio.block.base import Block
from nio.properties import Property, VersionProperty, IntProperty, BoolProperty


class Sort(Block):

    sort_by = Property(title="Sort Key", default="")
    reverse = BoolProperty(title="Reverse", default=False)
    limit = IntProperty(title="Limit", default=0)
    version = VersionProperty("0.1.0")

    def process_signals(self, signals):
        sigs = sorted(signals, key=self.sort_by, reverse=self.reverse())
        if self.limit() > 0:
            size = len(sigs)
            sigs = sigs[:self.limit()]
            new_size = len(sigs)
            self.logger.debug(
                "Limiting number of notified signals from "
                "{} to {}".format(size, new_size)
            )
        self.notify_signals(sigs)
