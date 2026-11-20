import argparse, secrets, string
p=argparse.ArgumentParser(); p.add_argument('--length',type=int,default=24); a=p.parse_args()
if not 12<=a.length<=4096: p.error('Length must be 12–4096')
alphabet=string.ascii_letters+string.digits+'!@#$%&*_-='
print(''.join(secrets.choice(alphabet) for _ in range(a.length)))

