## Reflections & Learning Notes

Day 03 wasn’t just about running commands — it was about developing intuition for how real systems behave.  
Here’s what I personally took away from the debugging and hands‑on scripting today:

### What I Learned
- How directory structure and relative paths actually work (several “no such file or directory” mistakes reinforced this).
- How execute permissions function, and why `chmod u+x` is required before a script can run.
- How to read permission bits like `rwxr--r--` and understand who can do what.
- How background processes behave, how PIDs are generated, and how to inspect or kill them.
- How ports and networking work at a basic level, and how to check if something is listening on a port.
- How logs are created, redirected, appended, and followed in real time.
- How to start a simple service, capture its PID, store it, and inspect it.

### What I Debugged / Struggled With
- Forgetting to save files before running them.
- Running scripts from the wrong directory.
- Mixing up absolute vs relative paths.
- Running `tail -f` with no target file.
- Creating files in the wrong folders (and learning why structure matters).
- Learning that zsh comments break commands unless there’s a space before the `#`.

These mistakes were useful — they forced me to understand how the shell actually interprets commands.

### What I Still Want to Improve
- Get faster at reading `ps aux` and recognizing patterns.
- Build stronger intuition around ports, sockets, and what “LISTEN” truly means.
- Understand how these same primitives translate into Docker, Kubernetes, and GPU job orchestration.
- Explore how logging, process management, and port inspection look inside containers and distributed systems.

This project isn't about memorizing Linux commands — it's about building the mental models that will support more advanced AI infra work later in the sprint.
