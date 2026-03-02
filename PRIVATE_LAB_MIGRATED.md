# Private Lab Migration Notice

The `private_lab/` workspace has been moved out of this forked repository into a standalone repository at:

- `/workspace/aegis-asset-lab`

## Why
This repository is a fork and not ideal for private permission control. The private lab now lives in an independent repo so it can be managed and published privately.

## Rollback / Recovery
If needed, you can recover the previous in-repo version via git history:

- Restore folder from previous commit:
  - `git checkout HEAD~1 -- private_lab`

Or reset to a commit before this migration.
