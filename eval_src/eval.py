# This script evaluates scoring results and outputs evaluation results.
import argparse
from pathlib import Path
from datetime import datetime

parser = argparse.ArgumentParser("score")
parser.add_argument("--scoring_result", type=str, help="Path of scoring result")
parser.add_argument("--eval_output", type=str, help="Path of output evaluation result")

args = parser.parse_args()

print("hello evaluation world...")

lines = [
    f"Scoring result path: {args.scoring_result}",
    f"Evaluation output path: {args.eval_output}",
]

for line in lines:
    print(line)

# Evaluate the incoming scoring result and output evaluation result.
# Here only output a dummy file for demo.
# Feature 1
# Feature 2
# Feature 3
# Bugfix 1
curtime = datetime.now().strftime("%b-%d-%Y %H:%M:%S")
eval_msg = f"Eval done at {curtime}\n"
(Path(args.eval_output) / "eval_result.txt").write_text(eval_msg)
