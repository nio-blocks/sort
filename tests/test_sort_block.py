from threading import Event

from nio.testing.block_test_case import NIOBlockTestCase
from nio.signal.base import Signal
from nio.util.discovery import not_discoverable
from ..sort_block import Sort


@not_discoverable
class SortTest(Sort):

    def __init__(self, event):
        super().__init__()
        self._event = event
        self._sigs = None

    def process_signals(self, signals):
        super().process_signals(signals)
        self._event.set()

    def notify_signals(self, signals):
        self._sigs = signals


class TestSortBlock(NIOBlockTestCase):

    def setUp(self):
        super().setUp()
        self.signals = [
            Signal({'val': 3}),
            Signal({'val': 1}),
            Signal({'val': 2})
        ]

    def test_sort_signals(self):
        e = Event()
        blk = SortTest(e)
        self.configure_block(blk, {
            "sort_by": "{{$val}}"
        })
        blk.start()
        blk.process_signals(self.signals)
        blk.stop()
        self.assertEqual([s.val for s in blk._sigs], [1, 2, 3])

    def test_limit(self):
        e = Event()
        blk = SortTest(e)
        self.configure_block(blk, {
            "sort_by": "{{$val}}",
            "limit": 2
        })
        blk.start()
        blk.process_signals(self.signals)
        blk.stop()
        self.assertEqual([s.val for s in blk._sigs], [1, 2])

    def test_sort_reverse(self):
        e = Event()
        blk = SortTest(e)
        self.configure_block(blk, {
            "sort_by": "{{$val}}",
            "reverse": True
        })
        blk.start()
        blk.process_signals(self.signals)
        e.wait(1)
        blk.stop()
        self.assertEqual([s.val for s in blk._sigs], [3, 2, 1])

    def test_default_pass(self):
        e = Event()
        blk = SortTest(e)
        self.configure_block(blk, {})
        blk.start()
        blk.process_signals(self.signals)
        e.wait(1)
        blk.stop()
        self.assertEqual([s.val for s in blk._sigs], [3, 1, 2])
