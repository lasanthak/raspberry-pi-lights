from bit_packing import pack_bits, unpack_bits


class PinPattern8:
    def __init__(self, state_ints_array, loop_count):
        self.loop_count = loop_count
        self.states = []
        for state_int in state_ints_array:
            self.states.append(state_int)


class PatternAlgorithm:
    def __init__(self, loop_count):
        self.prev_pattern_int = None
        self.cur_pattern = None
        self.cur_pattern_id = -1
        self.cur_pos_in_pattern = -1
        self.cur_pattern_loops_remaining = 0
        self.patterns = []
        # Organize patterns
        # -----------------------------------------------------------
        self.patterns.append(PinPattern8(PatternAlgorithm.INITIAL_STATE_PATTERN, 1))
        self.patterns.append(PinPattern8(PatternAlgorithm.KNIGHT_RIDER, loop_count))
        self.patterns.append(PinPattern8(PatternAlgorithm.KNIGHT_RIDER_TWO, loop_count))
        self.patterns.append(PinPattern8(PatternAlgorithm.KNIGHT_RIDER_SPLIT_MIDDLE, loop_count))
        self.patterns.append(PinPattern8(PatternAlgorithm.INVERTED_KNIGHT_RIDER, loop_count))
        self.patterns.append(PinPattern8(PatternAlgorithm.PROGRESS_3, 2*loop_count))
        # -----------------------------------------------------------

    def _next_pattern_int(self):
        if self.cur_pattern_loops_remaining > 0:
            self.cur_pos_in_pattern += 1
            if self.cur_pos_in_pattern >= len(self.cur_pattern.states):
                self.cur_pos_in_pattern = 0
                self.cur_pattern_loops_remaining -= 1

        if self.cur_pattern_loops_remaining <= 0:
            self.cur_pos_in_pattern = 0
            self.cur_pattern_id = (self.cur_pattern_id + 1) % len(self.patterns)
            self.cur_pattern = self.patterns[self.cur_pattern_id]
            self.cur_pattern_loops_remaining = self.cur_pattern.loop_count

        return self.cur_pattern.states[self.cur_pos_in_pattern]

    def next(self):
        new_pattern_int = self._next_pattern_int()
        if new_pattern_int == self.prev_pattern_int:
            # Skip one step if consecutive patterns are the same
            self.prev_pattern_int = self._next_pattern_int()
        else:
            self.prev_pattern_int = new_pattern_int

        return unpack_bits(self.prev_pattern_int)

    @staticmethod
    def inverse_initial_state():
        return unpack_bits(PatternAlgorithm.INVERSE_INITIAL_STATE)

    # Initial state of the pins
    INITIAL_STATE_PATTERN = [pack_bits([0, 0, 0, 0, 0, 0, 0, 0])]
    # Inverse of initial state
    INVERSE_INITIAL_STATE = pack_bits([1, 1, 1, 1, 1, 1, 1, 1])

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
