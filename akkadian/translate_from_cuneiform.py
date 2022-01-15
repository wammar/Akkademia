import subprocess
from pathlib import Path
from translation_tokenize import tokenize


def translate_from_cuneiform(file):
    tokenize("signs_char", file, False, Path("NMT_input/tokenization"), Path(""), Path("/tmp"))
    cmd = "../fairseq/fairseq_cli/interactive.py " \
          "data-bin-not-divided-by-three-dots/ " \
          "--path not_divided_by_three_dots_result.LR_0.1.MAX_TOKENS_4000/checkpoint_best.pt " \
          "--beam 5 " \
          "--input /tmp/" + file
    result = subprocess.run(cmd.split())
    print(result.stdout)


if __name__ == '__main__':
    cuneiform_file = input("Please enter the name of the Akkadian file for translation\n")
    translate_from_cuneiform(cuneiform_file)