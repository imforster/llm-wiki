---
title: "My Web Clipper Prompt"
source: "https://www.linkingyourthinking.com/thank-you/my-web-clipper-prompt"
author:
published:
created: 2026-05-02
description: "The Linking Your Thinking Workshop is a 6-week community driven learning experience. It will teach, train, and support you in building a custom knowledge management system you can trust. Learn how to never lose your ideas again. Connect and create meaningful insights."
tags:
  - "clippings"
---
We're thrilled to have you with us!

Below, you'll find my prompt for the Obsidian Web Clipper Interpreter, plus a quick setup guide so you can be processing articles in minutes. Again, this is an additional and optional layer that you can apply to your clippings whenever you'd like.

The prompt generates three layers above any article you clip: a plain text summary, the headlines, and things, a list of key people, terms, and ideas that are mentioned in the clipping.  
  
Let's get you set up.

#### Step 1

**Install the Obsidian Web Clipper**

It's a browser extension, so it works in all the major browsers. [Search for the Obsidian Web Clipper](https://obsidian.md/clipper) in your browser's extension store and install it.

![](https://cdn.prod.website-files.com/5fec91e1aac90836da5f8ed0/69f4a0ac22074895c2fe4fff_web-clipper-step-1.webp)

#### Step 2

**Open the Interpreter settings**

Click the Obsidian icon in your browser, then click the gear icon. From there, go to interpreter. Make sure to enable interpreter that this is toggled on.

![](https://cdn.prod.website-files.com/5fec91e1aac90836da5f8ed0/69f4a2077575e0afe081da5f_web-clipper-step-2-refined.webp)

#### Step 3

**Add your AI provider**

Add your provider of choice. After that, you can select your model.

Obsidian Web Clipper is completely model agnostic. It doesn't care what you use. You can use Claude, GPT, Gemini, DeepSeek, or local models through Ollama and a lot more. If a better model comes out tomorrow, you just switch.

Tip: For the smoothest experience, start with Claude. Most providers will need billing set up to get an API key and some may need extra configuration or some troubleshooting. Going local with Ollama is free, but heavier web pages can be hit-or-miss depending on your computer's specs.

![](https://cdn.prod.website-files.com/5fec91e1aac90836da5f8ed0/69f4a0b3b5dd6ae22d79ba15_web-clipper-step-3.webp)

#### Step 4

**Open or Create a Template**

Go to the **Templates** section in Web Clipper settings. Select an existing template to edit, or click **New template.**

![](https://cdn.prod.website-files.com/5fec91e1aac90836da5f8ed0/69f4a0ccb5ea33afbba695c4_web-clipper-step-4.webp)

#### Step 5

In the template’s **note content** area, paste the following exactly as-is:

```
{{"most interesting aspect, delivered as a statement, starting with the line: In summary, "}}

## Headlines

{{"bulleted headlines as one-line, boldly encapsulated, declarative statements or insights (in bold) ending in a period, followed by 1 (at most 2) supporting sentences"}}

## Things

{{"bulleted list of - People:, places, numbers, things & concepts."}}

---

{{content}}
```

What’s happening here:

The double curly braces `{{"..."}}` trigger the Interpreter.

Each one is treated as a separate AI prompt that runs against the page content when you clip.

![](https://cdn.prod.website-files.com/5fec91e1aac90836da5f8ed0/69f4a0ce76d3deabaecffa9c_web-clipper-step-5.webp)

#### Step 6

**(Optional) Improve Speed and Cost**

- You can limit how much content is sent to the AI to make processing faster and cheaper.
- If you’re comfortable experimenting, you can adjust the **Interpreter context** field.
- If you’re unsure, **skip this step for now** and use the default setup first.

#### Step 7

**Clip a Page Using This Template**

- Open any webpage you want to clip.
- Click the Obsidian Web Clipper icon.
- Select your template.

You’ll now see an **Interpreter section**.

- Click **Interpret.**
- Wait a few seconds (depending on the model and page length).
- Once complete, click **Add to Obsidian.**
![](https://cdn.prod.website-files.com/5fec91e1aac90836da5f8ed0/69f4a0dd6e4599991b4cfc92_web-clipper-step-7.webp)