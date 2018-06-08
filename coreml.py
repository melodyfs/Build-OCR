import coremltools

output_labels = [
'あ', 'い', 'う', 'え', 'お',
'か', 'く', 'こ', 'し', 'せ',
'た', 'つ', 'と', 'に', 'ね',
'は', 'ふ', 'ほ', 'み', 'め',
'や', 'ゆ', 'よ', 'ら', 'り',
'る', 'わ', 'が', 'げ', 'じ',
'ぞ', 'だ', 'ぢ', 'づ', 'で',
'ど', 'ば', 'び',
'ぶ', 'べ', 'ぼ', 'ぱ', 'ぴ',
'ぷ', 'ぺ', 'ぽ',
'き', 'け', 'さ', 'す', 'そ',
'ち', 'て', 'な', 'ぬ', 'の',
'ひ', 'へ', 'ま', 'む', 'も',
'れ', 'を', 'ぎ', 'ご', 'ず',
'ぜ', 'ん', 'ぐ', 'ざ', 'ろ']

scale = 1/255.

coreml_model = coremltools.converters.keras.convert('./hiraganaModel.h5',
                                                    input_names='image',
                                                    image_input_names='image',
                                                    output_names='output',
                                                    class_labels= output_labels,
                                                    image_scale=scale)
coreml_model.author = 'Melody Yang & Kaichi Momose'
coreml_model.license = 'MIT'
coreml_model.short_description = 'Detect hiragana from handwriting'
coreml_model.input_description['image'] = 'Grayscale image contains a handwritten letter'
coreml_model.output_description['output'] = 'Output a letter in hiragana'
coreml_model.save('hiraganaModel.mlmodel')
