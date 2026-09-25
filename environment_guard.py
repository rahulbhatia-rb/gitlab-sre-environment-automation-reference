import json, sys
from pathlib import Path

def evaluate(e):
    reasons=[]
    if not e['immutable_image']: reasons.append('environment image is not immutable')
    if not e['ephemeral_credentials']: reasons.append('credentials are not ephemeral')
    if e['provision_minutes'] > e['max_provision_minutes']: reasons.append('provisioning SLO breached')
    if not e['teardown_verified']: reasons.append('teardown was not verified')
    return {'environment_ready':not reasons,'reasons':reasons}
def run(p): return evaluate(json.loads(Path(p).read_text())['environment'])
if __name__=='__main__':
    if sys.argv[1:]==['--self-test']:
        assert evaluate({'immutable_image':True,'ephemeral_credentials':True,'provision_minutes':4,'max_provision_minutes':10,'teardown_verified':True})['environment_ready'];print('environment automation: passed')
    else: print(json.dumps(run(sys.argv[1]),indent=2))
