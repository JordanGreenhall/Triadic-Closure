#!/usr/bin/env python3
"""
Verification script for the mathematical-domain walk (companion to verification-companion.md).
Deterministic; no dependencies beyond Python 3 stdlib. Each check prints PASS/FAIL.
Checks are finite-range lemma-grade evidence; see the companion for which claims
are additionally secured by induction arguments.
"""
from fractions import Fraction as Q
from itertools import product
RESULTS = []
def check(name, ok):
    RESULTS.append((name, ok)); print(f"[{'PASS' if ok else 'FAIL'}] {name}")

def refine(states, obs, succs, ordered=True):
    part = {s: obs(s) for s in states}
    for _ in range(len(states) + 1):
        if ordered:
            sig = {s: (obs(s), tuple(part[c] for c in succs(s))) for s in states}
        else:
            sig = {s: (obs(s), tuple(sorted(part[c] for c in succs(s)))) for s in states}
        blocks, new = {}, {}
        for s in states: new[s] = blocks.setdefault(sig[s], len(blocks))
        if new == part: break
        part = new
    return part

# V1 - Degeneracy of position-only ternary factors
X = [[()]]
for n in range(4): X.append(list(product(X[n], repeat=3)))
v1a = all(len(x) == 1 for x in X)
A = ['a','b']; alpha = {'a': ('a','b','a'), 'b': ('b','a','b')}
p = refine(A, obs=lambda s: 0, succs=lambda s: list(alpha[s]))
v1b = len(set(p.values())) == 1
check("V1 plain X^3: terminal sequence constant at 1; 2-state coalgebra collapses to 1 class", v1a and v1b)

# V2 - Signature observation: rigidity of pure office-recursion (exactly 3 classes)
states_b = [(s, i) for s in "FWT" for i in range(4)]
child = {"F": "TWF", "W": "FTW", "T": "FWT"}
succ_b = lambda s: [(c, (s[1]+k) % 4) for k, c in enumerate(child[s[0]])]
p = refine(states_b, obs=lambda s: s[0], succs=succ_b)
check("V2 rigidity: office-recursion with signature observed has exactly 3 classes", len(set(p.values())) == 3)

# V3 - Signature + horizontal variety: no collapse; control: signature stripped collapses
chars = {"d": ("d","d","d"), "m": ("d","d","m"), "h": ("d","m","h")}
states_c = [(s, ch) for s in "FWT" for ch in chars]
succ_c = lambda s: [(c, chars[s[1]][k]) for k, c in enumerate(child[s[0]])]
p1 = refine(states_c, obs=lambda s: s, succs=succ_c)
p2 = refine(states_c, obs=lambda s: s[1], succs=succ_c)
check("V3 signatures+variety: 9/9 distinct; control (signature stripped): collapse occurs",
      len(set(p1.values())) == 9 and len(set(p2.values())) < 9)

# V4 - Finite endpoint-bounded oriented chains. Direction + endpoint structure
#      distinguishes every role; stripping direction leaves exactly mirror classes.
v4_oriented = True
v4_mirrors = True
for n in range(2, 13):
    chain = list(range(n))
    po = refine(chain, obs=lambda s: 0,
                succs=lambda s, n=n: [s+1] if s+1 < n else [])
    ps = refine(chain, obs=lambda s: 0,
                succs=lambda s, n=n: [t for t in (s-1, s+1) if 0 <= t < n],
                ordered=False)
    mirror_role = {s: min(s, n-1-s) for s in chain}
    v4_oriented &= len(set(po.values())) == n
    v4_mirrors &= all((ps[i] == ps[j]) == (mirror_role[i] == mirror_role[j])
                      for i, j in product(chain, repeat=2))
check("V4 finite oriented chains n=2..12: all roles distinct; undirected controls = mirror classes",
      v4_oriented and v4_mirrors)

# V5 - Positive finite order-characters and additive group completion.
# Chain tokens are identical; concatenation preserves no summand tag.
chain_of = lambda n: ("x",) * n
concat = lambda a, b: a + b
v5_chain = all(
    concat(concat(chain_of(a), chain_of(b)), chain_of(c))
    == concat(chain_of(a), concat(chain_of(b), chain_of(c)))
    and len(concat(chain_of(a), chain_of(b))) == a + b
    for a, b, c in product(range(1, 7), repeat=3)
)
def norm(pr):
    m = min(pr)
    return (pr[0]-m, pr[1]-m)
def eqdiff(p, q):
    return p[0] + q[1] == p[1] + q[0]
def zadd(p, q):
    return norm((p[0]+q[0], p[1]+q[1]))
pairs = list(product(range(1, 7), repeat=2))
v5_quotient = all(eqdiff(p, q) == (norm(p) == norm(q))
                  for p, q in product(pairs, repeat=2))
v5_group = all(
    zadd(zadd(p, q), r) == zadd(p, zadd(q, r))
    and zadd(p, q) == zadd(q, p)
    and zadd(p, (p[1], p[0])) == (0, 0)
    and zadd(p, (1, 1)) == norm(p)
    for p, q, r in product(pairs, repeat=3)
)
check("V5 finite positive chains: tag-free concatenation; formal-difference quotient and additive laws",
      v5_chain and v5_quotient and v5_group)

# V6 - Same-summand: index-2 defect over Z; exact eigen-decomposition over Q; swap acts +1/-1
v6a = (1 + 0) % 2 != 0  # s = a = 1/2 not integral for the pair (1,0)
def dec(u, v): s = Q(1,2)*(u+v); a = Q(1,2)*(u-v); return s, a
v6b = all((lambda s,a: (s+a, s-a) == (Q(u), Q(v)))(*dec(Q(u), Q(v)))
          for u, v in product(range(-3,4), repeat=2))
s, a = dec(Q(2), Q(5)); sw = lambda p: (p[1], p[0])
v6c = sw((s,s)) == (s,s) and sw((a,-a)) == (-a,a)
check("V6 same-summand: Z-defect on (1,0); Q-exact sym/antisym; swap eigenvalues +1/-1", v6a and v6b and v6c)

# V7 - Free Z-module laws and J-compatible non-degenerate bi-additive pairing
add_ = lambda x,y: {g: x.get(g,0)+y.get(g,0) for g in set(x)|set(y)}
neg_ = lambda x: {g: -c for g,c in x.items()}
gens = ["gA","gB"]; elems = [{"gA":a,"gB":b} for a in range(-2,3) for b in range(-2,3)]
v7a = all(add_(x,add_(y,z)) == add_(add_(x,y),z) and add_(x,y) == add_(y,x)
          and all(v == 0 for v in add_(x,neg_(x)).values())
          for x in elems[:8] for y in elems[:8] for z in elems[:8])
Jm = lambda x: {"gA": x.get("gB",0), "gB": x.get("gA",0)}
P = {("gA","gB"):1, ("gB","gA"):1, ("gA","gA"):0, ("gB","gB"):0}
pair = lambda x,y: sum(x.get(g,0)*y.get(h,0)*P[(g,h)] for g in gens for h in gens)
v7b = all(pair(add_(x,y),z) == pair(x,z)+pair(y,z) for x in elems[:6] for y in elems[:6] for z in elems[:6])
v7c = all(any(pair(x,y) != 0 for y in elems) for x in elems if any(c != 0 for c in x.values()))
v7d = all(pair(Jm(x), Jm(y)) == pair(x,y) for x in elems[:10] for y in elems[:10])
check("V7 free Z-module laws; pairing bi-additive, non-degenerate, J-invariant", v7a and v7b and v7c and v7d)

# V8 - Rule-given reals: cut laws (witness-rule), entailment order, addition, definable sup, approximant
sqrt2 = lambda q: q < 0 or q*q < 2
one, two = (lambda q: q < 1), (lambda q: q < 2)
samples = [Q(i, d) for i in range(-8, 12) for d in range(1, 9)]
wit = lambda q: q + (2 - q*q)/4 if q >= 0 else Q(0)
v8a = all((not sqrt2(q)) or all(sqrt2(p) for p in samples if p < q) for q in samples)
v8b = all((not sqrt2(q)) or (wit(q) > q and sqrt2(wit(q))) for q in samples)
leq = lambda x,y: all((not x(q)) or y(q) for q in samples)
v8c = leq(one, sqrt2) and leq(sqrt2, two) and not leq(two, sqrt2)
sadd = lambda x,y: (lambda q: any(x(a) and y(q-a) for a in samples))
s2 = sadd(sqrt2, sqrt2); v8d = s2(Q(28,10)) and not s2(Q(29,10))
fam = [lambda q, k=k: q < 2 - Q(1,k) for k in range(1, 30)]
sup = lambda q: any(f(q) for f in fam)
v8e = all(sup(q) == two(q) for q in samples)
x = Q(3,2)
for _ in range(6): x = (x + 2/x)/2
v8f = abs(x*x - 2) < Q(1, 10**20)
check("V8 rule-given cuts: laws, entailment order, addition, definable sup, approximant", 
      v8a and v8b and v8c and v8d and v8e and v8f)

# V9 - Constitutive involution on formation terms: J^2 = id; sectors inhabited; orbits of size 1 or 2
def Jt(t):
    if t == ("d",): return t
    if t[0] == "m": return ("m", Jt(t[1]))
    if t[0] == "w": return ("w", frozenset(Jt(x) for x in t[1]))
    if t[0] == "wd": return ("wd", Jt(t[2]), Jt(t[1]))
d_ = ("d",)
terms = [d_, ("m", d_), ("m", ("m", d_)), ("wd", d_, ("m", d_)), ("wd", ("m", d_), d_),
         ("w", frozenset([d_, ("m", d_)])), ("wd", d_, Jt(("wd", d_, ("m", d_))))]
v9a = all(Jt(Jt(t)) == t for t in terms)
fixed = [t for t in terms if Jt(t) == t]; moved = [t for t in terms if Jt(t) != t]
v9b = len(fixed) > 0 and len(moved) > 0
v9c = all(Jt(Jt(t)) == t and (Jt(t) == t or Jt(Jt(t)) == t) for t in terms)
check("V9 J^2 = id on formation terms; both sectors inhabited; orbits size 1 or 2", v9a and v9b and v9c)

print(f"\n{sum(ok for _, ok in RESULTS)}/{len(RESULTS)} checks passed")
