from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Define the Braille pattern dictionary
braille_dict = {
    'a': '⠁', 'b': '⠃', 'c': '⠉', 'd': '⠙', 'e': '⠑', 'f': '⠋', 'g': '⠛', 'h': '⠓',
    'i': '⠊', 'j': '⠚', 'k': '⠅', 'l': '⠇', 'm': '⠍', 'n': '⠝', 'o': '⠕', 'p': '⠏',
    'q': '⠟', 'r': '⠗', 's': '⠎', 't': '⠞', 'u': '⠥', 'v': '⠧', 'w': '⠺', 'x': '⠭',
    'y': '⠽', 'z': '⠵', '1': '⠁', '2': '⠃', '3': '⠉', '4': '⠙', '5': '⠑', '6': '⠋',
    '7': '⠛', '8': '⠓', '9': '⠊', '0': '⠚', ' ': ' ', ',': '⠂', ';': '⠆', ':': '⠒',
    '.': '⠲', '!': '⠖', '?': '⠦', '(': '⠶', ')': '⠶', '-': '⠤', "'": '⠄', '/': '⠌',

    # Music notes
    'C': '⠉', 'D': '⠙', 'E': '⠑', 'F': '⠋', 'G': '⠛', 'A': '⠁', 'B': '⠃',

    # Music symbols
    'sharp': '⠸',   # Sharp sign
    'flat': '⠡',    # Flat sign
    'natural': '⠷', # Natural sign
    'quarter_note': '⠈', # Quarter note
    'eighth_note': '⠘',  # Eighth note
    'repeat_sign': '⠦⠦'  # Repeat sign
}

# Convert text to Braille
def text_to_braille(text):
    braille_output = []
    for word in text.split():
        if word in braille_dict:
            braille_output.append(braille_dict[word])
        else:
            braille_output.append(''.join([braille_dict.get(char.lower(), '') for char in word]))
    return ' '.join(braille_output)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/convert', methods=['POST'])
def convert():
    try:
        data = request.get_json()
        input_text = data.get('text', '')

        if not input_text:
            return jsonify({'error': 'No input text provided'}), 400

        braille_text = text_to_braille(input_text)
        return jsonify({'braille': braille_text}), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)