from bit_packing import pack_bits, unpack_bits


class PinPattern8:
    def __init__(self, state_ints_array):
        self.states = []
        for state_int in state_ints_array:
            self.states.append(state_int)


class PatternAlgorithm:
    def __init__(self):
        self.prev_pattern_int = None
        self.cur_pattern_id = 0
        self.cur_pos_in_pattern = -1
        self.cur_pattern_loops_remaining = PatternAlgorithm._LOOP_COUNT_PER_PATTERN
        self.patterns = []
        # Organize patterns
        # -----------------------------------------------------------
        self.patterns.append(PatternAlgorithm.INITIAL_STATE_PATTERN)
        self.patterns.append(PatternAlgorithm.KNIGHT_RIDER)
        self.patterns.append(PatternAlgorithm.KNIGHT_RIDER_TWO)
        self.patterns.append(PatternAlgorithm.KNIGHT_RIDER_SPLIT_MIDDLE)
        self.patterns.append(PatternAlgorithm.INVERTED_KNIGHT_RIDER)
        self.patterns.append(PatternAlgorithm.PROGRESS_3)
        # -----------------------------------------------------------

    def _next_pattern_int(self):
        self.cur_pos_in_pattern += 1

        if self.cur_pos_in_pattern >= len(self.patterns[self.cur_pattern_id]):
            self.cur_pos_in_pattern = 0
            self.cur_pattern_loops_remaining -= 1

        if self.cur_pattern_loops_remaining <= 0:
            self.cur_pattern_id = (self.cur_pattern_id + 1) % len(self.patterns)
            self.cur_pos_in_pattern = 0
            self.cur_pattern_loops_remaining = PatternAlgorithm._LOOP_COUNT_PER_PATTERN

        return self.patterns[self.cur_pattern_id][self.cur_pos_in_pattern]

    def next(self):
        pattern_int = self._next_pattern_int()
        if pattern_int == self.prev_pattern_int:
            # Skip one step if consecutive patterns are the same
            self.prev_pattern_int = self._next_pattern_int()
        else:
            self.prev_pattern_int = pattern_int

        return unpack_bits(self.prev_pattern_int)

    # Loop count per pattern
    _LOOP_COUNT_PER_PATTERN = 4

    # Initial state of the pins
    INITIAL_STATE_PATTERN = [pack_bits([0, 0, 0, 0, 0, 0, 0, 0])]

    # Knight Rider
    KNIGHT_RIDER = [
        pack_bits([1, 0, 0, 0, 0, 0, 0, 0]),
        pack_bits([0, 1, 0, 0, 0, 0, 0, 0]),
        pack_bits([0, 0, 1, 0, 0, 0, 0, 0]),
        pack_bits([0, 0, 0, 1, 0, 0, 0, 0]),
        pack_bits([0, 0, 0, 0, 1, 0, 0, 0]),
        pack_bits([0, 0, 0, 0, 0, 1, 0, 0]),
        pack_bits([0, 0, 0, 0, 0, 0, 1, 0]),
        pack_bits([0, 0, 0, 0, 0, 0, 0, 1]),
        pack_bits([0, 0, 0, 0, 0, 0, 1, 0]),
        pack_bits([0, 0, 0, 0, 0, 1, 0, 0]),
        pack_bits([0, 0, 0, 0, 1, 0, 0, 0]),
        pack_bits([0, 0, 0, 1, 0, 0, 0, 0]),
        pack_bits([0, 0, 1, 0, 0, 0, 0, 0]),
        pack_bits([0, 1, 0, 0, 0, 0, 0, 0]),
        pack_bits([1, 0, 0, 0, 0, 0, 0, 0])
    ]

    # Inverted Knight Rider
    INVERTED_KNIGHT_RIDER = [
        pack_bits([0, 1, 1, 1, 1, 1, 1, 1]),
        pack_bits([1, 0, 1, 1, 1, 1, 1, 1]),
        pack_bits([1, 1, 0, 1, 1, 1, 1, 1]),
        pack_bits([1, 1, 1, 0, 1, 1, 1, 1]),
        pack_bits([1, 1, 1, 1, 0, 1, 1, 1]),
        pack_bits([1, 1, 1, 1, 1, 0, 1, 1]),
        pack_bits([1, 1, 1, 1, 1, 1, 0, 1]),
        pack_bits([1, 1, 1, 1, 1, 1, 1, 0]),
        pack_bits([1, 1, 1, 1, 1, 1, 0, 1]),
        pack_bits([1, 1, 1, 1, 1, 0, 1, 1]),
        pack_bits([1, 1, 1, 1, 0, 1, 1, 1]),
        pack_bits([1, 1, 1, 0, 1, 1, 1, 1]),
        pack_bits([1, 1, 0, 1, 1, 1, 1, 1]),
        pack_bits([1, 0, 1, 1, 1, 1, 1, 1]),
        pack_bits([0, 1, 1, 1, 1, 1, 1, 1])
    ]

    # Knight Rider by 2 positions
    KNIGHT_RIDER_TWO = [
        pack_bits([1, 1, 0, 0, 0, 0, 0, 0]),
        pack_bits([0, 1, 1, 0, 0, 0, 0, 0]),
        pack_bits([0, 0, 1, 1, 0, 0, 0, 0]),
        pack_bits([0, 0, 0, 1, 1, 0, 0, 0]),
        pack_bits([0, 0, 0, 0, 1, 1, 0, 0]),
        pack_bits([0, 0, 0, 0, 0, 1, 1, 0]),
        pack_bits([0, 0, 0, 0, 0, 0, 1, 1]),
        pack_bits([0, 0, 0, 0, 0, 1, 1, 0]),
        pack_bits([0, 0, 0, 0, 1, 1, 0, 0]),
        pack_bits([0, 0, 0, 1, 1, 0, 0, 0]),
        pack_bits([0, 0, 1, 1, 0, 0, 0, 0]),
        pack_bits([0, 1, 1, 0, 0, 0, 0, 0]),
        pack_bits([1, 1, 0, 0, 0, 0, 0, 0])
    ]

    # Knight Rider split from middle to both directions
    KNIGHT_RIDER_SPLIT_MIDDLE = [
        pack_bits([0, 0, 0, 1, 1, 0, 0, 0]),
        pack_bits([0, 0, 1, 0, 0, 1, 0, 0]),
        pack_bits([0, 1, 0, 0, 0, 0, 1, 0]),
        pack_bits([1, 0, 0, 0, 0, 0, 0, 1]),
        pack_bits([0, 1, 0, 0, 0, 0, 1, 0]),
        pack_bits([0, 0, 1, 0, 0, 1, 0, 0]),
        pack_bits([0, 0, 0, 1, 1, 0, 0, 0]),
        pack_bits([0, 0, 1, 0, 0, 1, 0, 0]),
        pack_bits([0, 1, 0, 0, 0, 0, 1, 0]),
        pack_bits([1, 0, 0, 0, 0, 0, 0, 1]),
        pack_bits([0, 1, 0, 0, 0, 0, 1, 0]),
        pack_bits([0, 0, 1, 0, 0, 1, 0, 0]),
        pack_bits([0, 0, 0, 1, 1, 0, 0, 0])
    ]

    # Progress skipping 3
    PROGRESS_3 = [
        pack_bits([1, 0, 0, 0, 0, 0, 0, 0]),
        pack_bits([0, 1, 0, 0, 0, 0, 0, 0]),
        pack_bits([0, 0, 1, 0, 0, 0, 0, 0]),
        pack_bits([1, 0, 0, 1, 0, 0, 0, 0]),
        pack_bits([0, 1, 0, 0, 1, 0, 0, 0]),
        pack_bits([0, 0, 1, 0, 0, 1, 0, 0]),
        pack_bits([0, 0, 0, 1, 0, 0, 1, 0]),
        pack_bits([0, 0, 0, 0, 1, 0, 0, 1]),
        pack_bits([0, 0, 0, 0, 0, 1, 0, 0]),
        pack_bits([0, 0, 0, 0, 0, 0, 1, 0]),
        pack_bits([0, 0, 0, 0, 0, 0, 0, 1]),
        pack_bits([1, 0, 0, 0, 0, 0, 0, 0])
    ]
