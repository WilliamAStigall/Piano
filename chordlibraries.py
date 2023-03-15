def chords(Input):
    chords = {
        "C Major": ["C", "E", "G"],
        "C Minor": ["C", "D#", "G"],
        "C# Major": ["C#", "F", "G#"],
        "C# Minor": ["C#", "E", "G#"],
        "D Major": ["D", "F#", "A"],
        "D Minor": ["D", "F", "A"],
        "D# Major": ["D#", "G", "A#"],
        "D# Minor": ["D#", "F#", "A#"],
        "E Major": ["E", "G#", "B"],
        "E Minor": ["E", "G", "B"],
        "F Major": ["F", "A", "C"],
        "F Minor": ["F", "G#", "C"],
        "F# Major": ["F#", "A#", "C#"],
        "F# Minor": ["F#", "A", "C#"],
        "G Major": ["G", "B", "D"],
        "G Minor": ["G", "A#", "D"],
        "G# Major": ["G#", "C", "D#"],
        "G# Minor": ["G#", "B", "D#"],
        "A Major": ["A", "C#", "E"],
        "A Minor": ["A", "C", "E"],
        "A# Major": ["A#", "D", "F"],
        "A# Minor": ["A#", "C#", "F"],
        "B Major": ["B", "D#", "F#"],
        "B Minor": ["B", "D", "F#"]
    }
    return chords[Input]


def add_chord(chord_info):
    chord_name, notes = chord_info
    chords[chord_name] = notes

def input_validation(user_input):
    user_input = user_input.lower()
    user_input = user_input.replace("flat", "\u266d")
    user_input = user_input.replace("sharp")
    user_input = user_input.replace(" ", "-")