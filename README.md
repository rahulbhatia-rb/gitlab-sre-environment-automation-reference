# GitLab SRE Environment Automation Reference

Runnable guard for ephemeral CI/SRE environments. It asserts immutable images, short-lived credentials, a provisioning SLO, and verified teardown before an environment is declared ready.

```bash
python3 environment_guard.py --self-test
python3 environment_guard.py profile.json
```

Independent demonstration; not GitLab internal software.
