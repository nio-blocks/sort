from nio.common.block.base import Block
from nio.common.discovery import Discoverable, DiscoverableType
from nio.metadata.properties.bool import BoolProperty
from nio.metadata.properties.expression import ExpressionProperty


@Discoverable(DiscoverableType.block)
class Sort(Block):
    
    sort_by = ExpressionProperty(title="Sort Key")
    reverse = BoolProperty(title="Reverse", default=False)

    def process_signals(self, signals):
        self.notify_signals(
            sorted(signals, key=self.sort_by, reverse=self.reverse)
        )
    
