# Breaking the Black Box of AI and Human Experts: Pluggable Cognitive Frameworks for Human-machine Collaboration

>A story of independent exploration: This project was conceived and implemented independently by me as a sophomore in half a year, through deep meta-interactions with a large language model. After the release of DeepSeekMath-V2, I decided to open source this general cognitive architecture ahead of time in order to drive the paradigm revolution between humans and AI from "tools" to "partners".

>Urgent Release: In response to the recursive verification breakthrough of DeepSeekMath-V2, this proof-of-concept version was released early. The full documentation and use cases are being urgently refined, and the community is welcome to contribute!

Version Note: Currently in Beta (v0.1), it is a functional prototype version, and details will continue to be refined.
Risk Warning: Due to the urgent release time, some code details have not been carefully reviewed, so it is recommended to only be tested in non-production environment.
Future Optimization Plans:
1.Complete full code detail review and logic verification;
2.Add new scene test cases to improve stability;
3.Improve the exception handling mechanism and boundary scenario adaptation;
4.Add more cognitive framework cases in vertical fields.

All contents will continue to be updated iteratively. If any problems are found, you can feedback through Issue. Thank you for your understanding and support.

## Summary

I propose a new paradigm called "human-machine collaborative cognitive augmentation" to address the fundamental gap between the cognitive black box of human experts (where implicit intuitions are hard to pass on) and the computational black box of AI (where decision-making processes cannot be trusted). Through structured meta-interactions, I distill human tacit knowledge into a computable and portable pluggable cognitive framework, enabling bidirectional cognitive augmentation. This work marks a key transition for AI from "tool" to "thought partner".

## Core Contributions

1. Meta-Interaction Methodology: A recursive process (Build-Questioned-Observe) that guides deep collaboration between humans and AI, aiming to systematically extract and solidify an individual's unique system of strategic decisions.

2. RAMTN Architecture: RAMTN (Recursive Adversarial Meta-Thinking Network) is a revolutionary cognitive architecture whose core innovation is a pluggable cognitive framework. It can both actively extract an intuitive decision-making model from expert conversations, and load and augment other individuals or systems with that model as a "thinking engine".

3. Proof of Validity of the Paradigm: The feasibility of the paradigm is initially verified by the founder's original practice of constructing a complete strategy system.

## Fundamental Differences from Existing Approaches
| Methods               | Essence                     | Limitations               |                                                 
|-------------------------------------|----------------------------------------------|----------------------------------------|
| Tips for Engineering      | Optimize the input to the black box | AI's passive tool role was not changed  |
| Chain of Thought      | Linear reasoning process display | Lack of recursive self-criticism and frame generation                        |
| AI Agents             | Action-oriented task execution               | Decision logic is still encapsulated in a black box                         |
| My Meta-Interactions | Role transition: AI becomes an active "partner" in framework generation and critique | The fundamental problem of cognition extraction and transplantation is solved |

 *Table 1: A tabular comparison of the essence and limitations between traditional AI-assisted methods and the meta-interaction approach*

## RAMTN Architecture Core

![Figure 1: RAMTN Overall Architecture](assets/ramtn_architecture.png)

*Figure 1: Core input-process-output architecture of RAMTN, illustrating the cognitive framework-driven recursive thinking logic*

![Figure 2: RAMTN Flowchart Element Explanation](assets/ramtn_flowchart_elements.png)

*Figure 2: Flowchart Element Explanation for Core input-process-output architecture of RAMTN*

RAMTN is a recursive adversarial meta-thinking network with the following core process:

Input:User question + an optional, loaded "expert cognitive framework".

Process:Guided by the framework, perform a multiple recursive Construction-Question-Observe loop.

Output:Structured analysis with three levels of confidence (I know for sure, I suspect, I don't know) to produce a trusted cognitive output.

Here's how RAMTN works:

![Figure 3: RAMTN Three-Layer Adversarial Loop](assets/ramtn_three_layer_loop.png)

*Figure 3: Three-layer Constructor-Questioner-Observer loop process of RAMTN, including intra-layer interaction and inter-layer data transmission logic*

![Figure 4: Three-Layer Structure Element Explanation](assets/three_layer_elements.png)

*Figure 4: Flowchart Element Explanation for Three-layer Constructor-Questioner-Observer loop process of RAMTN*

RAMTN uses a three-layer Constructor-Questioner-Observer adversarial structure:

1.Process within each layer: Constructor generates responses labeled "sure/speculation/unknown" + source (demoting to "speculation" if knowledge is insufficient); The Questioner checks the "sure" facts/logic, the "speculative" logic; The Constructor needs to respond with the factual logic (failing to meet the criteria, the label will be downgraded), and finally the Observer will re-evaluate the classification.

2.Inter-layer flow: The content of the Constructor + Questioner of this layer is passed to the next layer Constructor and the Observer of this layer, completing the three layers of iteration.

3.Classification of results: "Convinced" needs to be agreed by both sides; "Speculative" if not all responses were accepted; "Unknown" is unable to prove/not responded.

4.Utility and Transfer: I transfer the adversarial mechanism of the original mathematical problem to the medical domain, using a unified fact/logic standard for hallucination detection, and output a structured classification result.

## A Note about DeepSeekMath-V2

I noticed that the recently released DeepSeekMath-V2 is a brilliant demonstration of the power of the "recursive self-verification" paradigm in its domain. I congratulate and am excited about it. DeepSeekMath-V2's "generator-verifier-meta-verifier" self-verification framework provides a paradigm for the procedural rigor of mathematical reasoning (Shao et al., 2025). The model iterates reasoning ability through automated loop closure, reaching gold level in IMO 2025. Its technical details may refer to the open source report (https://github.com/deepseek-ai/DeepSeek-Math-V2/blob/main/DeepSeekMath_V2.pdf).

I must point out:
The architectural design of this work (RAMTN) was formed independently from the core ideas, with an early exploration timestamp predating the release of DeepSeekMath-V2. Far from undercutting my work, the success of DeepSeek in mathematics strongly confirms the foresight and correctness of the path I have chosen.

Our goal is different: DeepSeekMath-V2 is a perfect example of this paradigm in closed mathematics. RAMTN, on the other hand, aims to build a general cognitive architecture to solve open, ambiguous human-level strategic decision problems.

## Conclusions and the Future

This work provides a technical foundation for breaking knowledge monopoly and realizing "cognitive equality". I have open sourced the RAMTN core engine and invited the community to explore its infinite possibilities in education, consulting, medical care and other fields together.

## References

1. Shao, Z., Luo, Y., Lu, C., Ren, Z.Z., Hu, J., Ye, T., Gou, Z., Ma, S., & Zhang, X. (2025). DeepSeekMath-V2: Towards Self-Verifiable Mathematical Reasoning. Open-source technical report. Retrieved from
https://github.com/deepseek-ai/DeepSeek-Math-V2/blob/main/DeepSeekMath_V2.pdf

## AI-Assisted Statement

AI tools (DeepSeek, Doubao) were used to improve efficiency during the development of this project. The specific collaboration methods are as follows:

• Code Level: The design of the core architecture and strategic cognitive framework of the project is controlled by human authors, the detailed implementation of the code (such as API call encapsulation, data parsing logic) is generated by AI, and all AI-generated code is verified by artificial logic and adapted to the architecture;

• Documentation Level: The first draft of README and related instructions are generated by AI and reviewed by human authors, adjusted in structure, supplemented in content, and verified for technical accuracy;

• Future Improvements: Due to the urgency of the release, code details and documentation will be continuously reviewed and refined in subsequent releases (the current version is in beta).

The final intellectual property of the project belongs to the human author, and the integrity, security, and functionality of all content are the ultimate responsibility of the human author.
