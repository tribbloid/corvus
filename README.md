Disclaimer: None of us has played Call of Duty BlackOps 3

# corvus: A self-rewriting compiler

#### Building blocks

- Code(string): a code snippet

- State(dict): a state of the memory in the scope where Code is running

- Output(s: State, ee: Error)

- Oracle: an interpreter/compiler, convert a Code/State pair into
a sequence of states/Delta 

  - Oracle = (code: Code, s: State) => List[out: Output]

- Delta(dict): difference between 2 Outputs

  - Delta(out1: Output, out2: Output)

- Monkey: MOST IMPORTANT plugable component, randomly generate new code
based on a tuple of input.

  - by convention, a DNN-guided MCTS algorithm that can be trained
  by first order.

  - Monkey = (src: Code, tgt_hypothesis: Code, delta: Delta) => tgt_hypothesis_+: Code

