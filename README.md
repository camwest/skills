# skills

Agent skills by [Cameron Westland](https://cameronwestland.com), installable individually via [skills.sh](https://skills.sh):

```bash
npx skills add camwest/skills --skill <name>
```

Works with Claude Code, Codex, and other agents that support the `SKILL.md` format.

## Skills

### [ground-in-priors](skills/ground-in-priors/SKILL.md)

```bash
npx skills add camwest/skills --skill ground-in-priors
```

Research and compare credible precedents before proposing or implementing fixes, features, dependencies, architecture, or product ideas.

Coding agents default to inventing solutions. This skill is a rigorous, fail-closed research gate that forces the question every good engineer asks by reflex: *what are the priors?* It requires a diagnosed problem before any solution search, multiple independent priors with explicit transferability arguments, and a decision ladder — reuse, configure, adapt, compose, invent — where each later step requires rejecting the earlier ones. `problem-not-understood` and `insufficient-evidence` are legal outputs. There is no quick mode, on purpose.

```text
Use $ground-in-priors to research and fix this viewport scrolling bug.
```

### [write-standalone-docs](skills/write-standalone-docs/SKILL.md)

```bash
npx skills add camwest/skills --skill write-standalone-docs
```

Turn chats, meetings, screenshots, and task context into durable reports, strategy documents, memos, specifications, and proposals that make sense to a cold reader.

This skill separates domain evidence from commissioning context and production residue. It catches ghost arguments, invisible interlocutors, leaked instructions, provenance laundering, dangling references, and substantive expansion disguised as cleanup. A bundled scanner surfaces likely residue without treating second person, negation, or disagreement as automatic errors.

```text
Use $write-standalone-docs to make this strategy memo fully standalone for a cold reader.
```

## License

[MIT](LICENSE)
