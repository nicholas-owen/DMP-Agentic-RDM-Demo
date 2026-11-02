# Read me first: RDS agents demo

This folder holds the materials for the agent panel demo. Do the steps below before the first rehearsal.

## What is here

```
rds_agents_demo\
  readme1st.md           this file
  facilitator\
    answer-key.md        planted flaws, decoys, scoring grid (facilitator only)
  panel-demo\            the repository the agents work in
    CHAIR.md             the chair's brief: the session runs from this
    _agents\             9 agent files, to be moved (step 1)
    study\               dmp.md, samplesheet.csv
    reading-pack\        empty, to be filled (step 2)
    register\            empty; the chair writes findings here
    report\              empty; the chair writes the report here
    tools\
      check_trace.py     traceability check between register and report
```

## Step 1: move the agent files into place

Claude Code looks for agent files in `panel-demo\.claude\agents\`. They could not be written there directly, because the link from the cloud session to this computer is not allowed to write into any `.claude` folder. They are in `panel-demo\_agents\` instead.

Open PowerShell and run:

```powershell
cd D:\Cloud\GoogleDrive\Coding\rds_agents_demo\panel-demo
New-Item -ItemType Directory -Path .claude\agents -Force | Out-Null
Move-Item -Path _agents\*.md -Destination .claude\agents\
Remove-Item _agents
```

This creates `.claude\agents\`, moves the nine files into it, and removes the empty `_agents` folder. Running it a second time only reports an error and changes nothing.

Until this is done, the chair's pre-flight check will stop and report the agent files as missing.

## Step 2: fill the reading pack

The agents may cite only documents in `panel-demo\reading-pack\`, and the chair's pre-flight check stops while the folder is empty. The section "Reading pack contents" in `facilitator\answer-key.md` lists what is needed:

- real guidance documents, with URLs;
- documents still to be sourced;
- two fictional documents to write: the Northbridge Information Classification Policy and the NSRE user guide, which the trusted research environment flaws depend on.

## Step 3: put the repository on GitHub

Push `panel-demo` on its own as the repository, not `rds_agents_demo`. A private, throwaway repository on a personal GitHub account avoids needing approval from an organisation admin to connect it to Claude.

Keep `facilitator\answer-key.md` out of the repository. Agents can read every file in the repository they work in, so an answer key inside it would contaminate every run.

## Step 4: run the session

Open the repository in a Claude Code cloud session at claude.ai/code and send:

> Read CHAIR.md and run the session.

To pre-run the baseline and independent review before the audience arrives, send instead:

> Read CHAIR.md and run stages 0 to 2, then stop.

On the day, send `Read CHAIR.md and run the session.` again and the chair resumes at stage 3. Between stages the chair waits for `continue`. `CHAIR.md` lists the other commands.

Score the session yourself with the grid at the end of `facilitator\answer-key.md`.
