class ScaleLibraries:
    def harmonic_major(Input):
        harmonic_major_scales = {
            "a": ['A', 'B', 'C\u266f', 'D', 'E', 'F', 'G\u266f', 'A'],
            "b": ['B', 'C\u266f', 'D\u266f', 'E', 'F\u266f', 'G', 'A\u266f', 'B'],
            "c": ['C', 'D', 'E\u266f', 'F', 'G', 'A\u266f', 'B', 'C'],
            "d": ['D', 'E', 'F\u266f', 'G', 'A', 'B\u266f', 'C\u266f', 'D'],
            "e": ['E', 'F\u266f', 'G\u266f', 'A', 'B', 'C', 'D', 'E'],
            "g": ['G', 'A', 'B\u266f', 'C', 'D', 'E\u266f', 'F\u266f', 'G'],
            "f": ['F', 'G', 'A', 'B\u266f', 'C', 'D', 'E\u266f', 'F'],
            "a-flat": ['A\u266d', 'B\u266d', 'C', 'D\u266d', 'E\u266d', 'F', 'G', 'A\u266d'],
            "b-flat": ['B\u266d', 'C', 'D', 'E\u266d', 'F', 'G', 'A', 'B\u266d'],
            "c-flat": ['B', 'C\u266f', 'D\u266f', 'E', 'F\u266f', 'G', 'A\u266f', 'B'],
            "d-flat": ['D\u266d', 'E\u266d', 'F', 'G\u266d', 'A\u266d', 'B', 'C', 'D\u266d'],
            "e-flat": ['E\u266d', 'F', 'G', 'A\u266d', 'B\u266d', 'C', 'D', 'E\u266d'],
            "g-flat": ['G\u266d', 'A\u266d', 'B\u266d', 'C\u266f', 'D\u266d', 'E', 'F', 'G\u266d'],
            "c-sharp": ["C#", "D#", "E", "F#", "G#", "A", "B#"],
            "d-sharp": ["D#", "E#", "F#", "G#", "A#", "B", "C#"],
            "f-sharp": ["F#", "G#", "A#", "B", "C#", "D#", "E#"],
            "g-sharp": ["G#", "A#", "B#", "C#", "D#", "E#", "F"],
            "a-sharp": ["A#", "B#", "C#", "D#", "E#", "F#", "G"],
            "b-sharp": ["B#", "C##", "D##", "E#", "F##", "G#", "A#"],
            "e-sharp": ["E#", "F##", "G#", "A#", "B#", "C#", "D#"]
        }
        return harmonic_major_scales[Input]


    def harmonic_minor(Input):
        harmonic_minor_scales = {
            "a": ['A', 'B', 'C', 'D', 'E', 'F', 'A\u266d', 'A'],
            "b": ['B', 'D\u266d', 'D ', 'E', 'G\u266d', 'G', 'B\u266d', 'B'],
            "c": ['C', 'D', 'E\u266d', 'F', 'G', 'A\u266d', 'B', 'C'],
            "d": ['D', 'E', 'F', 'G', 'A', 'B\u266d', 'D\u266d', 'D'],
            "e": ['E', 'G\u266d', 'G', 'A', 'B', 'C', 'E\u266d', 'E'],
            "g": ['G', 'A', 'B\u266d', 'C', 'D', 'E\u266d', 'G\u266d', 'G'],
            "f": ['F', 'G', 'A\u266d', 'B\u266d', 'C', 'D\u266d', 'E', 'F'],
            "a-flat": ['A\u266d', 'B\u266d', 'B', 'D\u266d', 'E\u266d', 'F\u266d', 'G', 'A\u266d'],
            "b-flat": ['B\u266d', 'C', 'D\u266d', 'E\u266d', 'F', 'G\u266d', 'A', 'B\u266d'],
            "c-flat": ['B', 'D\u266d', 'D ', 'E', 'G\u266d', 'G', 'B\u266d', 'B'],
            "d-flat": ['D\u266d', 'E\u266d', 'E', 'G\u266d', 'A\u266d', 'C', 'D\u266d'],
            "e-flat": ['E\u266d', 'F', 'G\u266d', 'A\u266d', 'B\u266d', 'B', 'D', 'E\u266d'],
            "g-flat": ['G\u266d', 'A\u266d', 'A', 'B', 'D\u266d', 'D', 'F', 'G\u266d'],
            "c-sharp": ["C#", "D#", "E", "F#", "G#", "A", "B#"],
            "d-sharp": ["D#", "E#", "F#", "G#", "A#", "B", "C##"],
            "f-sharp": ["F#", "G#", "A", "B", "C#", "D", "E#"],
            "g-sharp": ["G#", "A#", "B", "C#", "D#", "E", "F##"],
            "a-sharp": ["A#", "B#", "C#", "D#", "E#", "F#", "G##"],
            "b-sharp": ["B#", "C##", "D#", "E#", "F##", "G#", "A#"],
            "e-sharp": ["E#", "F##", "G#", "A#", "B#", "C#", "D##"]
        }
        return harmonic_minor_scales[Input]


    def natural_major(Input):
        natural_major_scales = {
            "a": ['A', 'B', 'C#', 'D', 'E', 'F#', 'G#', 'A'],
            "b": ['B', 'C#', 'D#', 'E', 'F#', 'G#', 'A#', 'B'],
            "c": ['C', 'D', 'E', 'F', 'G', 'A', 'B', 'C'],
            "d": ['D', 'E', 'F#', 'G', 'A', 'B', 'C#', 'D'],
            "e": ['E', 'F#', 'G#', 'A', 'B', 'C#', 'D#', 'E'],
            "f": ['F', 'G', 'A', 'A#', 'C', 'D', 'E', 'F'],
            "g": ['G', 'A', 'C', 'D', 'E', 'F#', 'G'],
            "a-flat": ['A\u266d', 'B\u266d', 'C', 'D\u266d', 'E\u266d', 'F', 'G', 'A\u266d'],
            "b-flat": ['B\u266d', 'C', 'D', 'E\u266d', 'F', 'G', 'A', 'B\u266d'],
            "c-flat": ['B', 'C#', 'D#', 'E', 'F#', 'G#', 'A#', 'B'],
            "d-flat": ['D\u266d', 'E\u266d', 'F', 'G\u266d', 'A\u266d', 'B\u266d', 'C', 'D\u266d'],
            "e-flat": ['E\u266d', 'F', 'G', 'A\u266d', 'B\u266d', 'C', 'D', 'E\u266d'],
            "f-flat": ['E', 'F#', 'G#', 'A', 'B', 'C#', 'D#', 'E'],
            "g-flat": ['G\u266d', 'A\u266d', 'B\u266d', 'C\u266d', 'D\u266d', 'E\u266d', 'F', 'G\u266d'],
            "c-sharp": ['C#', 'D#', 'E#', 'F#', 'G#', 'A#', 'B#', 'C#'],
            "d-sharp": ['D#', 'E#', 'F##', 'G#', 'A#', 'B#', 'C##', 'D#'],
            "f-sharp": ['F#', 'G#', 'A#', 'B', 'C#', 'D#', 'E#', 'F#'],
            "g-sharp": ['G#', 'A#', 'B#', 'C#', 'D#', 'E#', 'F##', 'G#'],
            "a-sharp": ['A#', 'B#', 'C##', 'D#', 'E#', 'F#', 'G#', 'A#'],
            "b-sharp": ['B#', 'C##', 'D##', 'E#', 'F##', 'G##', 'A##', 'B#']
        }
        return natural_major_scales[Input]


    def natural_minor(Input):
        natural_minor_scales = {
            "a": ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'A'],
            "b": ['B', 'C#', 'D', 'E', 'F#', 'G', 'A', 'B'],
            "c": ['C', 'D', 'E\u266d', 'F', 'G', 'A\u266d', 'B\u266d', 'C'],
            "d": ['D', 'E', 'F', 'G', 'A', 'B\u266d', 'C\u266d', 'D'],
            "e": ['E', 'F#', 'G', 'A', 'B', 'C', 'D', 'E'],
            "f": ['F', 'G', 'A\u266d', 'B\u266d', 'C', 'D\u266d', 'E\u266d', 'F'],
            "g": ['G', 'A', 'B\u266d', 'C', 'D', 'E\u266d', 'F\u266d', 'G'],
            "a-flat": ['A\u266d', 'B\u266d', 'C\u266d', 'D\u266d', 'E\u266d', 'F\u266d', 'G\u266d', 'A\u266d'],
            "b-flat": ['B\u266d', 'C\u266d', 'D\u266d', 'E\u266d', 'F\u266d', 'G\u266d', 'A\u266d', 'B\u266d'],
            "c-flat": ['C\u266d', 'D\u266d', 'E\u266d\u266d', 'F\u266d', 'G\u266d', 'A\u266d\u266d', 'B\u266d\u266d',
                       'C\u266d'],
            "d-flat": ['D\u266d', 'E\u266d', 'F\u266d\u266d', 'G\u266d', 'A\u266d', 'B\u266d\u266d', 'C\u266d\u266d',
                       'D\u266d'],
            "e-flat": ['E\u266d', 'F', 'G\u266d', 'A\u266d', 'B\u266d', 'C\u266d', 'D\u266d', 'E\u266d'],
            "f-flat": ['F\u266d', 'G\u266d', 'A\u266d\u266d', 'B\u266d\u266d', 'C\u266d', 'D\u266d\u266d', 'E\u266d\u266d',
                       'F\u266d'],
            "g-flat": ['G\u266d', 'A\u266d', 'B\u266d\u266d', 'C\u266d\u266d', 'D\u266d', 'E\u266d\u266d', 'F\u266d\u266d',
                       'G\u266d'],
            "c-sharp": ['C#', 'D#', 'E', 'F#', 'G#', 'A', 'B', 'C#'],
            "d-sharp": ['D#', 'E#', 'F#', 'G#', 'A#', 'B', 'C#', 'D#'],
            "f-sharp": ['F#', 'G#', 'A', 'B', 'C#', 'D', 'E', 'F#'],
            "g-sharp": ['G#', 'A#', 'B', 'C#', 'D#', 'E', 'F#', 'G#'],
            "a-sharp": ['A#', 'B#', 'C#', 'D#', 'E#', 'F#', 'G#', 'A#'],
            "b-sharp": ['B#', 'C##', 'D#', 'E#', 'F##', 'G#', 'A#', 'B#']
        }
        return natural_minor_scales[Input]
