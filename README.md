# GitLab SRE Environment Automation Reference

Runnable guard for ephemeral CI/SRE environments. It asserts immutable images, short-lived credentials, a provisioning SLO, and verified teardown before an environment is declared ready.

```bash
python3 environment_guard.py --self-test
python3 environment_guard.py profile.json
```

Independent demonstration; not GitLab internal software.

## Design review

The control makes ephemeral environments reproducible and safe: build images are immutable, credentials expire, provisioning has an SLO, and teardown is verified. A CI job can call this guard before reporting an environment URL to a developer, preventing leaked credentials and orphaned resources.
