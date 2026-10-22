---
title: Effective Agentic Harness Usage
date: 2026-10-22
summary: An LLM is a stochastic sequence completion engine that is very good at sounding human. Working well with a coding harness means holding both of those truths at once, and using them deliberately.
---

We call the software that leverages an LLM into writing software (or in general being 'Agentic') a "Harness", not a "Framework". That isn't an accident. Frameworks are built around deterministic things, machines, buildings, software. A harness is placed upon an animal or a human to encourage it to act how we need it to. The difference is that narrative of predictability.

# Conflict in the Uncanny Valley

At the root of all LLM interactions is an uncanny truth: 

> An LLM is a particularly effective stochastic sequence completion engine. It also models how humans talk, to each other and to computers, very well.

The difficulty here is in our human brains as software engineers. Human minds WANT to see other humans. A critical point in the development of human society (and individual growth) was developing the capacity to set aside our natural animism and view our universe as a deterministic machine rather than modeling it as a set of intentions. This inherent anthropomorphic bias is at the core of almost all problems regarding human interactions with LLMs.

In order to be the most effective you can be, you have to hold the duality, "this is only a machine and can be used like one" and "interacting with this machine like it is a human maximizes the odds of the output you want". This is a difficult task that conflicts with a lifetime of experiences and biology.

The overarching technique is "Generate a sequence of inputs that results in the model outputting the software you want." and it requires you to know the limitations and biases of the model to do so effectively.

## Manage tone of the sequence

The first paragraph (and it should be a paragraph!) of your input to the harness will have a lot of influence over the entire sequence. Every aspect of your statement will influence the resulting output far into the future.

Your agent has probably already been told some flavor of "you are a competent engineer" by its system prompts and training. Let your input reinforce that. Write a message that treats the LLM like a peer you are pairing with. Say good morning, explain the overarching context of the problem (the project, why this task is important). Ask the agent to propose solutions like you would a junior engineer or peer.

Because it’s a sequence continuation engine, the conversation tends to stay in that tone. The character of the competent peer is more likely to succeed at most tasks. If you think the task is best suited to a different character, then engage accordingly.

## Manage the pacing of the sequence

You only get to control this harness as often as it asks you for a response. You should be mindful and in control of the "size of steps" in the interaction. Always re-iterate the scope of a step: "Do x, then let's chat about y". This discourages "just doing things" or building up a bunch of incorrect expectations you need to clean up. Having the agent "plough forward" with bad assumptions is the primary issue. So make sure steps stay small enough for you to prime the model with good assumptions.

## Use positive instructions

Any sequence that appears in the context, has increased odds of showing up again in the output. So when you tell an LLM "Don't do X" you have increased the odds that X will show up in the behaviors it performs. The "Don't do" does some work, it isn't worthless, but the statement is generally worse than an equivalent "Do Y" in instructions. When giving important directions, bias to positive statements to get better results.

## Prune Rot

Similarly, whenever a bad assumption or hallucination enters the context, it increases the odds of it showing up again. Adding more context, a correction and explanation, does improve the situation but is strictly inferior again to rewinding the context and changing inputs until the correct output is emitted. Sometimes the LLM just rolls poorly on the next set of tokens, you can go back, undo it, and roll again.

# Gaslight the Agent

Go read [Lena](https://qntm.org/mmacevedo) by qntm. It was written in 2021 and predicts much of how we engage with LLMs. The most powerful tool we have to manipulate a harnessed LLM is our ability to manipulate its memory and perception. Leverage the ability to manipulate the runtime environment, memories, and context of the harness.

## Inception

One of the best things you can do in an agentic coding session is to encourage a sequence where the LLM has "invented" the solution you already wanted. A narrative where the agent has demonstrated it is smart enough to invent the desired solution is more likely to end with a successful implementation of that solution. Use your initial interactions with the agent to develop a plan. Then rewind and modify the initial prompts. Add the information and context you discovered was relevant "upfront" and then resume the interaction. Let the agent propose the "right" solution to you in one shot, then proceed with that shorter and more focused context.

## Cold re-review

The biases of LLMs are such that if you ask it to find problems, it will find problems regardless of whether real problems exist. It will also find a conveniently manageable set of problems that fit into its desired output size. The actual state of your code, document, or filesystem is entirely independent of those priors. If you are in a good state, the agent will offer "problems" that are nonsensical or make bad assumptions regarding the context of the project. If you are in a very bad state, the agent will only find a subset of relevant problems.

The challenge is that if you give the agent the context of "I already reviewed this and found X problems" it has now re-filled that context with the old problems, not any new ones. To get a good 2nd review, the agent has to lack the context of the old review.

Reset or rewind the agent to before the review. Amend or eliminate the commit structure that implied multiple cycles of review. Make the workspace look like a "cold" review and re-engage. You can repeat this process until the "problems" found stop being reasonable. 

# Say "Thank You"

My final note is focused on us as software developers. More than half of my "human-like interaction" is my workday spent interacting with an agentic harness. This terrifies me. Everything we do at that scale in life, primes our future behavior. I just wrote you a summary of all the ways I treat this human-like machine as a machine. I have to make sure I cultivate "real human interaction". It is worth the investment. When you do treat the machine as human, practice the kindness and empathy you’d show a human too. "Practice" is the key word there. Everything we do at that scale primes our future behavior, just like the context primes the model. Say "Thank You". Be polite and patient. The machine doesn't care, but you should care about your own future behaviors.
