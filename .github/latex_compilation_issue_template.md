---
title: LaTeX Compilation Failed
labels: bug, latex
---

The LaTeX compilation process failed during the automated workflow.

**Triggering Event:** `${{ github.event_name }}`
**Actor:** `${{ github.actor }}`
**Commit:** `${{ github.sha }}` (if applicable)

Please find the compilation log attached as an artifact (`compilation-log.txt`) in the workflow run, or review the output below if it's short:

```
{{ env.COMPILATION_LOG_CONTENT }} <!-- We'll need to get this from the log file -->
```

Please investigate the errors in `compilation_log.txt` and fix the LaTeX source files.
