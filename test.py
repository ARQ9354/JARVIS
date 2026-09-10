import torch
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
from IndicTransToolkit import IndicProcessor


MODEL_NAME = "ai4bharat/indictrans2-indic-en-dist-200M"

device = "cuda" if torch.cuda.is_available() else "cpu"

print("Device:", device)
print("Loading model...")

tokenizer = AutoTokenizer.from_pretrained(
    MODEL_NAME,
    trust_remote_code=True
)

model = AutoModelForSeq2SeqLM.from_pretrained(
    MODEL_NAME,
    trust_remote_code=True
).to(device)

ip = IndicProcessor(inference=True)

print("Model loaded!")


def translate_hindi_to_english(text):

    sentences = [text]

    batch = ip.preprocess_batch(
        sentences,
        src_lang="hin_Deva",
        tgt_lang="eng_Latn"
    )

    inputs = tokenizer(
        batch,
        truncation=True,
        padding="longest",
        return_tensors="pt",
        return_attention_mask=True
    ).to(device)

    with torch.no_grad():

        generated_tokens = model.generate(
            **inputs,
            max_length=256,
            num_beams=5,
            num_return_sequences=1
        )

    decoded = tokenizer.batch_decode(
        generated_tokens,
        skip_special_tokens=True
    )

    output = ip.postprocess_batch(
        decoded,
        lang="eng_Latn"
    )

    return output[0]


tests = [
    "मुझे मशीन लर्निंग समझाओ",
    "आज दिल्ली का तापमान बताओ",
    "कैलकुलेटर खोलो",
]

for text in tests:

    print("\nHindi:", text)

    result = translate_hindi_to_english(text)

    print("English:", result)