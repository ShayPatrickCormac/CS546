import argparse
import numpy as np
from questiongenerator import QuestionGenerator
from questiongenerator import print_qa

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--text_dir",
        default=None,
        type=str,
        required=True,
        help="The text that will be used as context for question generation.",
    )
    parser.add_argument(
        "--model_dir",
        default=None,
        type=str,
        help="The folder that the trained model checkpoints are in.",
    )
    parser.add_argument(
        "--num_questions",
        default=10,
        type=int,
        help="The desired number of questions to generate.",
    )
    parser.add_argument(
        "--answer_style",
        default="all",
        type=str,
        help="The desired type of answers. Choose from ['all', 'sentences', 'multiple_choice']",
    )
    parser.add_argument(
        "--use_qa_eval",
        default=True,
        type=str,
        help="Whether or not you want the generated questions to be filtered for quality. Choose from ['True', 'False']",
    )
    args = parser.parse_args()

    with open(args.text_dir, 'r') as file:
        text_file = file.read()

    qg = QuestionGenerator(args.model_dir)

    qa_list = qg.generate(
        text_file,
        num_questions=int(args.num_questions),
        answer_style=args.answer_style,
        use_evaluator=np.where(args.use_qa_eval == 'True', True, False)
    )
    print_qa(qa_list)


if __name__ == "__main__":
    main()