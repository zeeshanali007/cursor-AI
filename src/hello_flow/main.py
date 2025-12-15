#!/usr/bin/env python
from random import randint

from pydantic import BaseModel

from crewai.flow import Flow, listen, start

from hello_flow.crews.poem_crew.poem_crew import PoemCrew


class PoemState(BaseModel):
    # sentence_count of 0 means "not set yet" and will be randomized
    sentence_count: int = 0
    poem: str = ""


class PoemFlow(Flow[PoemState]):

    @start()
    def generate_sentence_count(self):
        if self.state.sentence_count > 0:
            print(f"Using provided sentence count: {self.state.sentence_count}")
            return

        print("Generating sentence count")
        self.state.sentence_count = randint(1, 5)

    @listen(generate_sentence_count)
    def generate_poem(self):
        print("Generating poem")
        result = (
            PoemCrew()
            .crew()
            .kickoff(inputs={"sentence_count": self.state.sentence_count})
        )

        print("Poem generated", result.raw)
        self.state.poem = result.raw

    @listen(generate_poem)
    def save_poem(self):
        print("Saving poem")
        return {
            "poem": self.state.poem,
            "sentence_count": self.state.sentence_count,
            "author": "Zeeshan Ali",
        }


def kickoff(sentence_count: int | None = None):
    poem_flow = PoemFlow()
    if sentence_count:
        poem_flow.state.sentence_count = max(1, int(sentence_count))
    poem_flow.kickoff()


def plot():
    poem_flow = PoemFlow()
    poem_flow.plot()


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Run the poem flow.")
    parser.add_argument(
        "--sentences",
        type=int,
        default=None,
        help="Number of sentences to generate (defaults to a random 1-5).",
    )
    parser.add_argument(
        "--plot",
        action="store_true",
        help="Render a mermaid diagram of the flow instead of running it.",
    )
    args = parser.parse_args()

    if args.plot:
        plot()
    else:
        kickoff(args.sentences)
