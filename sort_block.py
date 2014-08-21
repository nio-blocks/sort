from nio.common.block.base import Block
from nio.common.discovery import Discoverable, DiscoverableType
from nio.metadata.properties.bool import BoolProperty
from nio.metadata.properties.int import IntProperty
from nio.metadata.properties.expression import ExpressionProperty


@Discoverable(DiscoverableType.block)
class Sort(Block):

    sort_by = ExpressionProperty(title="Sort Key")
    reverse = BoolProperty(title="Reverse", default=False)
    limit = IntProperty(title="Limit", default=0)

    def process_signals(self, signals):
        sigs = sorted(signals, key=self.sort_by, reverse=self.reverse)
        if self.limit > 0:
            size = len(sigs)
            sigs = sigs[:self.limit]
            new_size = len(sigs)
            self._logger.debug(
                "Limiting number of notified signals from "
                "{} to {}".format(size, new_size)
            )
        self.notify_signals(sigs)

