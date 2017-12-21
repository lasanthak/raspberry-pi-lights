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
        self.patterns.append(PinPattern8(PatternAlgorithm.ON_NOLASER, 12))
        self.patterns.append(PinPattern8(PatternAlgorithm.ON, 20))
        self.patterns.append(PinPattern8(PatternAlgorithm.ON_OFF, 1))
        self.patterns.append(PinPattern8(PatternAlgorithm.KR, 5))
        self.patterns.append(PinPattern8(PatternAlgorithm.KR_KR, 8))
        self.patterns.append(PinPattern8(PatternAlgorithm.FLIP_FLOP, 6))
        self.patterns.append(PinPattern8(PatternAlgorithm.ON_NOLASER, 20))
        self.patterns.append(PinPattern8(PatternAlgorithm.LASER_X, 16))
        self.patterns.append(PinPattern8(PatternAlgorithm.LASER, 14))
        self.patterns.append(PinPattern8(PatternAlgorithm.OFF, 8))
        self.patterns.append(PinPattern8(PatternAlgorithm.FLIP_FLOP, 6))
        self.patterns.append(PinPattern8(PatternAlgorithm.KR_KR, 8))
        self.patterns.append(PinPattern8(PatternAlgorithm.KR, 5))
        self.patterns.append(PinPattern8(PatternAlgorithm.LASER_X, 16))
        self.patterns.append(PinPattern8(PatternAlgorithm.LASER, 14))
        self.patterns.append(PinPattern8(PatternAlgorithm.OFF, 8))
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
        self.prev_pattern_int = self._next_pattern_int()
        return unpack_bits(self.prev_pattern_int)

    @staticmethod
    def inverse_initial_state():
        return unpack_bits(PatternAlgorithm.INVERSE_INITIAL_STATE)

    # 1 - garage
    # 2 - roof
    # 3 - front bush
    # 4 - rose bushes
    # 5 - white tree
    # 6 - multi color tree
    # 7 - x tree
    # 8 - laser

    # Initial state of the pins
    INITIAL_STATE_PATTERN = [pack_bits([0, 0, 0, 0, 0, 0, 0, 0])]
    # Inverse of initial state
    INVERSE_INITIAL_STATE = pack_bits([1, 1, 1, 1, 1, 1, 1, 1])

    # All On
    ON = [
        pack_bits([1, 1, 1, 1, 1, 1, 1, 1])
    ]

    # All Off
    OFF = [
        pack_bits([0, 0, 0, 0, 0, 0, 0, 0])
    ]

    # On - Off
    ON_OFF = [
        pack_bits([1, 1, 1, 1, 1, 1, 1, 0]),
        pack_bits([1, 1, 1, 1, 1, 1, 1, 0]),
        pack_bits([1, 1, 1, 1, 1, 1, 1, 0]),
        pack_bits([0, 0, 0, 0, 0, 0, 0, 0]),
        pack_bits([0, 0, 0, 0, 0, 0, 0, 0]),
        pack_bits([0, 0, 0, 0, 0, 0, 0, 0]),
        pack_bits([1, 1, 1, 1, 1, 1, 1, 0]),
        pack_bits([1, 1, 1, 1, 1, 1, 1, 0]),
        pack_bits([1, 1, 1, 1, 1, 1, 1, 0]),
        pack_bits([0, 0, 0, 0, 0, 0, 0, 0]),
        pack_bits([0, 0, 0, 0, 0, 0, 0, 0]),
        pack_bits([0, 0, 0, 0, 0, 0, 0, 0]),
        pack_bits([1, 1, 1, 1, 1, 1, 1, 0]),
        pack_bits([1, 1, 1, 1, 1, 1, 1, 0]),
        pack_bits([0, 0, 0, 0, 0, 0, 0, 0]),
        pack_bits([0, 0, 0, 0, 0, 0, 0, 0]),
        pack_bits([1, 1, 1, 1, 1, 1, 1, 0]),
        pack_bits([1, 1, 1, 1, 1, 1, 1, 0]),
        pack_bits([0, 0, 0, 0, 0, 0, 0, 0]),
        pack_bits([0, 0, 0, 0, 0, 0, 0, 0]),
        pack_bits([1, 1, 1, 1, 1, 1, 1, 0]),
        pack_bits([1, 1, 1, 1, 1, 1, 1, 0]),
        pack_bits([0, 0, 0, 0, 0, 0, 0, 0]),
        pack_bits([0, 0, 0, 0, 0, 0, 0, 0]),
        pack_bits([1, 1, 1, 1, 1, 1, 1, 0]),
        pack_bits([1, 1, 1, 1, 1, 1, 1, 0]),
        pack_bits([0, 0, 0, 0, 0, 0, 0, 0]),
        pack_bits([0, 0, 0, 0, 0, 0, 0, 0]),
        pack_bits([1, 1, 1, 1, 1, 1, 1, 0]),
        pack_bits([1, 1, 1, 1, 1, 1, 1, 0]),
        pack_bits([0, 0, 0, 0, 0, 0, 0, 0]),
        pack_bits([0, 0, 0, 0, 0, 0, 0, 0]),
        pack_bits([1, 1, 1, 1, 1, 1, 1, 0]),
        pack_bits([1, 1, 1, 1, 1, 1, 1, 0]),
        pack_bits([0, 0, 0, 0, 0, 0, 0, 0]),
        pack_bits([0, 0, 0, 0, 0, 0, 0, 0]),
        pack_bits([1, 1, 1, 1, 1, 1, 1, 0]),
        pack_bits([0, 0, 0, 0, 0, 0, 0, 0]),
        pack_bits([1, 1, 1, 1, 1, 1, 1, 0]),
        pack_bits([0, 0, 0, 0, 0, 0, 0, 0]),
        pack_bits([1, 1, 1, 1, 1, 1, 1, 0]),
        pack_bits([0, 0, 0, 0, 0, 0, 0, 0]),
        pack_bits([1, 1, 1, 1, 1, 1, 1, 0]),
        pack_bits([0, 0, 0, 0, 0, 0, 0, 0]),
        pack_bits([1, 1, 1, 1, 1, 1, 1, 0]),
        pack_bits([0, 0, 0, 0, 0, 0, 0, 0]),
        pack_bits([1, 1, 1, 1, 1, 1, 1, 0]),
        pack_bits([0, 0, 0, 0, 0, 0, 0, 0]),
        pack_bits([1, 1, 1, 1, 1, 1, 1, 0]),
        pack_bits([0, 0, 0, 0, 0, 0, 0, 0]),
        pack_bits([1, 1, 1, 1, 1, 1, 1, 0]),
        pack_bits([0, 0, 0, 0, 0, 0, 0, 0])
    ]

    # Knight Riders - Knight Riders
    KR_KR = [
        pack_bits([1, 0, 0, 0, 0, 1, 1, 1]),
        pack_bits([1, 0, 0, 0, 0, 1, 1, 1]),
        pack_bits([0, 1, 0, 0, 1, 0, 1, 1]),
        pack_bits([0, 1, 0, 0, 1, 0, 1, 1]),
        pack_bits([0, 0, 1, 1, 0, 0, 1, 1]),
        pack_bits([0, 0, 1, 1, 0, 0, 1, 1]),
        pack_bits([0, 1, 0, 0, 1, 0, 1, 1]),
        pack_bits([0, 1, 0, 0, 1, 0, 1, 1])
    ]

    # Knight Riders
    KR = [
        pack_bits([1, 0, 0, 0, 0, 0, 1, 1]),
        pack_bits([1, 0, 0, 0, 0, 0, 1, 1]),
        pack_bits([0, 1, 0, 0, 0, 0, 1, 1]),
        pack_bits([0, 1, 0, 0, 0, 0, 1, 1]),
        pack_bits([0, 0, 1, 0, 0, 0, 1, 1]),
        pack_bits([0, 0, 1, 0, 0, 0, 1, 1]),
        pack_bits([0, 0, 0, 1, 0, 0, 1, 1]),
        pack_bits([0, 0, 0, 1, 0, 0, 1, 1]),
        pack_bits([0, 0, 0, 0, 1, 0, 1, 1]),
        pack_bits([0, 0, 0, 0, 1, 0, 1, 1]),
        pack_bits([0, 0, 0, 0, 0, 1, 1, 1]),
        pack_bits([0, 0, 0, 0, 0, 1, 1, 1]),
        pack_bits([0, 0, 0, 0, 1, 0, 1, 1]),
        pack_bits([0, 0, 0, 0, 1, 0, 1, 1]),
        pack_bits([0, 0, 0, 1, 0, 0, 1, 1]),
        pack_bits([0, 0, 0, 1, 0, 0, 1, 1]),
        pack_bits([0, 0, 1, 0, 0, 0, 1, 1]),
        pack_bits([0, 0, 1, 0, 0, 0, 1, 1]),
        pack_bits([0, 1, 0, 0, 0, 0, 1, 1]),
        pack_bits([0, 1, 0, 0, 0, 0, 1, 1])

    ]

    # Flip - Flop - Swipe
    FLIP_FLOP = [
        pack_bits([1, 1, 0, 0, 0, 1, 1, 0]),
        pack_bits([1, 1, 0, 0, 1, 0, 1, 0]),
        pack_bits([0, 0, 1, 1, 0, 1, 1, 0]),
        pack_bits([0, 0, 1, 1, 1, 0, 1, 0]),
        pack_bits([1, 1, 0, 0, 0, 1, 0, 0]),
        pack_bits([1, 1, 0, 0, 1, 0, 0, 0]),
        pack_bits([0, 0, 1, 1, 0, 1, 0, 0]),
        pack_bits([0, 0, 1, 1, 1, 0, 0, 0]),
        pack_bits([1, 1, 0, 0, 0, 1, 1, 0]),
        pack_bits([1, 1, 0, 0, 1, 0, 1, 0]),
        pack_bits([0, 0, 1, 1, 0, 1, 1, 0]),
        pack_bits([0, 0, 1, 1, 1, 0, 1, 0]),
        pack_bits([1, 1, 0, 0, 0, 1, 0, 0]),
        pack_bits([1, 1, 0, 0, 1, 0, 0, 0]),
        pack_bits([0, 0, 1, 1, 0, 1, 0, 0]),
        pack_bits([0, 0, 1, 1, 1, 0, 0, 0]),
        pack_bits([1, 1, 0, 0, 0, 1, 1, 1]),
        pack_bits([1, 1, 0, 0, 1, 0, 1, 1]),
        pack_bits([0, 0, 1, 1, 0, 1, 1, 1]),
        pack_bits([0, 0, 1, 1, 1, 0, 1, 1]),
        pack_bits([1, 1, 0, 0, 0, 1, 0, 1]),
        pack_bits([1, 1, 0, 0, 1, 0, 0, 1]),
        pack_bits([0, 0, 1, 1, 0, 1, 0, 1]),
        pack_bits([0, 0, 1, 1, 1, 0, 0, 1]),
    ]

    # Fully On - No Laser
    ON_NOLASER = [
        pack_bits([1, 1, 1, 1, 1, 1, 1, 0])
    ]

    # Only Laser
    LASER = [
        pack_bits([0, 0, 0, 0, 0, 0, 0, 1])
    ]

    # Only Laser and X Tree
    LASER_X = [
        pack_bits([0, 0, 0, 0, 0, 0, 1, 1])
    ]
