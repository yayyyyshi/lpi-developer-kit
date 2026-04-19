# HOW I DID IT (Level 2)

## Steps I followed
- First, I cloned the repository and installed all dependencies using npm install.
- Then I built the project and ran the test-client to check if everything was working properly.
- After confirming that all tools passed, I installed Ollama to try running a local LLM.
- I ran the llama3 model and asked it about SMILE to understand how it works.

## Problems I faced
- At first, I wasn’t very clear on how to run a local LLM since I hadn’t done it before.
- Also, the model download took quite a bit of time, which made me think something might be wrong.

## How I solved them
- I carefully followed the Ollama setup instructions and verified each step.
- For the download issue, I just waited patiently and let it complete, and then everything worked fine.

## What I learned
- I learned how to set up and run a local LLM using Ollama, which was new for me.
- I also understood that SMILE focuses a lot on explainability, not just giving answers.
- Overall, I got a better idea of how LPI combines multiple tools to generate more reliable outputs.

# HOW I DID IT (Level 3)

## Steps I followed
- I first understood the Level 3 requirements and studied the example agent.
- Instead of copying it directly, I decided to build a simpler version that I could fully understand.
- I designed a flow where the agent selects tools based on the user’s question.
- I implemented MCP tool calls and connected them with a local LLM using Ollama.
- I tested the agent with different questions to make sure it was working correctly.

## Problems I faced
- Initially, I was confused about how MCP communication works.
- I also struggled a bit with understanding how tool outputs are structured.

## How I solved them
- I broke down the example agent step by step and focused on the essential parts.
- I simplified the logic instead of trying to build something too complex.

## What I learned
- How to build an AI agent that uses multiple tools
- The importance of explainability in AI systems
- How local LLMs can be integrated with external tools
